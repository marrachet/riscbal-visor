#!/usr/bin/env python3
"""Robot de RiscBal: comprueba si el EGMS tiene versión nueva para Baleares y,
si es así, descarga los datos y prepara los archivos del visor (web/datos/)."""
import os, sys, json, time, zipfile, tempfile, glob
from datetime import datetime, timezone
import requests, jwt
import numpy as np
import pandas as pd

API = "https://egms.land.copernicus.eu/insar-api/archive"
BBOX = [[1.10, 38.50], [4.50, 40.20]]          # Illes Balears (máx. permitido: 5 grados)
LIM = (1.10, 38.50, 4.50, 40.20)               # lon_min, lat_min, lon_max, lat_max
NIVEL, TIPO = "L3", "ORTHO-UP"                 # Nivel 3, movimiento vertical, rejilla de 100 m
SALIDA = os.path.join("web", "datos")


def log(m):
    print(m, flush=True)


def fallar(m):
    print("\nERROR: " + m, flush=True)
    sys.exit(1)


def token_acceso():
    raw = os.environ.get("EGMS_TOKEN", "").strip()
    if not raw:
        fallar("falta el secreto EGMS_TOKEN en GitHub (Settings > Secrets and variables > Actions).")
    try:
        k = json.loads(raw)
        clave = k["private_key"].encode("utf-8")
        ahora = int(time.time())
        claims = {"iss": k["client_id"], "sub": k["user_id"], "aud": k["token_uri"],
                  "iat": ahora, "exp": ahora + 3600}
        grant = jwt.encode(claims, clave, algorithm="RS256")
    except Exception as e:
        fallar("el secreto EGMS_TOKEN no tiene el formato esperado. Debe contener TODO el texto del "
               f"archivo token.jwt. Detalle técnico: {type(e).__name__}")
    r = requests.post(k["token_uri"],
                      headers={"Accept": "application/json", "Content-Type": "application/x-www-form-urlencoded"},
                      data={"grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer", "assertion": grant},
                      timeout=60)
    at = r.json().get("access_token") if r.ok else None
    if not at:
        fallar(f"el servicio rechazó el token (código {r.status_code}). Puede haber caducado: "
               f"genera uno nuevo en la web del CLMS y actualiza el secreto. Respuesta: {r.text[:200]}")
    return at


def buscar_producto(cab):
    rel = os.environ.get("RELEASE", "").strip()
    if not rel:
        lista = requests.get(f"{API}/releases", headers=cab, timeout=60).json()
        if not isinstance(lista, list) or not lista:
            fallar(f"no pude obtener la lista de versiones del EGMS: {str(lista)[:200]}")
        rel = sorted(lista)[-1]
    q = {"id": None, "bbox": BBOX, "levels": [NIVEL], "releases": [rel], "productType": TIPO}
    r = requests.post(f"{API}/search", headers={**cab, "Content-Type": "application/json"},
                      data=json.dumps(q), timeout=120)
    res = r.json()
    if not res.get("hits"):
        fallar(f"la búsqueda no devolvió datos para {rel}. Mensaje del servicio: {res.get('message', '-')}")
    return rel, res


def descargar(url, destino, cab):
    for intento in range(1, 4):
        try:
            for h in (None, cab):   # primero como en el ejemplo oficial; si falla, con identificación
                with requests.get(url, headers=h, stream=True, timeout=300) as r:
                    if r.status_code in (401, 403) and h is None:
                        continue
                    r.raise_for_status()
                    with open(destino, "wb") as f:
                        for trozo in r.iter_content(1 << 20):
                            f.write(trozo)
                    return
        except Exception as e:
            log(f"   intento {intento} fallido: {type(e).__name__}")
            time.sleep(10 * intento)
    fallar(f"no se pudo descargar {url.split('?')[0]}")


def leer_csv(ruta):
    """Devuelve array N x 4 (lon, lat, velocidad, desviación). Detecta las columnas por nombre."""
    cols = list(pd.read_csv(ruta, nrows=0).columns)
    low = {c.lower().strip(): c for c in cols}
    buscar = lambda *ns: next((low[n] for n in ns if n in low), None)
    clon, clat = buscar("longitude", "lon"), buscar("latitude", "lat")
    ce, cn = buscar("easting"), buscar("northing")
    cv = buscar("mean_velocity", "velocity")
    cs = next((low[c] for c in low if "std" in c and "vel" in c), None)
    if cv is None or not ((clon and clat) or (ce and cn)):
        fallar(f"no reconozco las columnas de {os.path.basename(ruta)}. Columnas: {cols[:15]}")
    usar = [c for c in (clon, clat, ce, cn, cv, cs) if c]
    trans = None
    if not (clon and clat):
        from pyproj import Transformer
        trans = Transformer.from_crs(3035, 4326, always_xy=True)
    partes = []
    for ch in pd.read_csv(ruta, usecols=usar, chunksize=500_000):
        if trans is not None:
            lon, lat = trans.transform(ch[ce].to_numpy(float), ch[cn].to_numpy(float))
        else:
            lon, lat = ch[clon].to_numpy(float), ch[clat].to_numpy(float)
        v = ch[cv].to_numpy(float)
        s = ch[cs].to_numpy(float) if cs else np.zeros(len(ch))
        ok = (np.isfinite(lon) & np.isfinite(lat) & np.isfinite(v) &
              (lon >= LIM[0]) & (lon <= LIM[2]) & (lat >= LIM[1]) & (lat <= LIM[3]))
        partes.append(np.column_stack([lon[ok], lat[ok], v[ok], s[ok]]).astype(np.float32))
    return np.vstack(partes) if partes else np.zeros((0, 4), np.float32)


def main():
    os.makedirs(SALIDA, exist_ok=True)
    ruta_estado = os.path.join(SALIDA, "estado.json")
    estado = json.load(open(ruta_estado)) if os.path.exists(ruta_estado) else {}
    forzar = os.environ.get("FORZAR", "false").lower() == "true"

    at = token_acceso()
    cab = {"Authorization": f"Bearer {at}", "Accept": "application/json"}
    rel, res = buscar_producto(cab)
    hits = res["hits"]
    firma = sorted(f"{h['filename']}|{h.get('version')}" for h in hits)
    log(f"Versión del EGMS: {rel} · {len(hits)} archivos")
    if firma == estado.get("firma") and not forzar:
        log("Sin cambios desde la última actualización. No hay nada que hacer.")
        return

    log("Hay datos nuevos (o se forzó la descarga). Descargando...")
    partes = []
    with tempfile.TemporaryDirectory() as tmp:
        for i, h in enumerate(hits, 1):
            log(f" [{i}/{len(hits)}] {h['filename']} ({h.get('filesize', 0) / 1e6:.0f} MB)")
            zip_ruta = os.path.join(tmp, h["filename"])
            descargar(f"{API}/download/{h['filename']}?id={res['id']}", zip_ruta, cab)
            carpeta = os.path.join(tmp, f"t{i}")
            with zipfile.ZipFile(zip_ruta) as z:
                z.extractall(carpeta)
            os.remove(zip_ruta)
            for csv in glob.glob(os.path.join(carpeta, "**", "*.csv"), recursive=True):
                partes.append(leer_csv(csv))
                log(f"    {os.path.basename(csv)}: {len(partes[-1])} puntos en Baleares")
    datos = np.vstack(partes) if partes else np.zeros((0, 4), np.float32)
    if len(datos) < 100:
        fallar(f"solo se obtuvieron {len(datos)} puntos en Baleares; no sobrescribo los datos anteriores.")

    datos.astype("<f4").tofile(os.path.join(SALIDA, "puntos.bin"))
    meta = {"release": rel, "version": max(str(h.get("version")) for h in hits),
            "n_puntos": int(len(datos)), "nivel": NIVEL, "tipo": TIPO,
            "generado": datetime.now(timezone.utc).strftime("%Y-%m-%d")}
    json.dump(meta, open(os.path.join(SALIDA, "meta.json"), "w"))
    json.dump({"firma": firma, "release": rel}, open(ruta_estado, "w"))
    log(f"Listo: {len(datos)} puntos guardados.")


if __name__ == "__main__":
    main()
