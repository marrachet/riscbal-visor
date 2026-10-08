Ë
    m†Çj:  ã                   ó  — d Z ddlZddlZddlZddlZddlZddlZddl Z ddlmZm	Z	 ddl
Z
ddl
Z
ddlZ
ddlZdZddgd dggZd	Zd
\  ZZej*                  j-                  d
d«      Zd
„ Zd„ Zd„ Zd„ Zd„ Zd„ Zd„ Zedk(  r e«        yy)uš   Robot de RiscBal: comprueba si el EGMS tiene versiÃ³n nueva para Baleares y,
si es asÃ­, descarga los datos y prepara los archivos del visor (web/datos/).é    N)ÚdatetimeÚtimezonez1https://egms.land.copernicus.eu/insar-api/archiveçš™™™™™ñ?ç     @C@ç      @çš™™™™D@)r   r   r    r   )ÚL3zORTHO-UPÚwebÚdatosc                 ó   — t        | d¬«       y )NT©Úflush)Úprint©Úms    úscripts/actualizar.pyÚlogr      s   € Ü	ˆ!4Öó    c                 óN   — t        d| z   d¬«       t        j                  d«       y )Nz
ERROR: Tr
   é   )r   ÚsysÚexitr   s    r   Úfallarr      s   € Ü	ˆ+˜‰/ Õ&Ü ‡HHˆQ…Kr   c                  óÂ  — t         j                  j                  dd«      j                   «       } | s
t	        d«       	 t
        j                  | «      }|d   j                  d«      }t        t        j                  «       «      }|d   |d    |d   ||d	z   d
œ}t        j                  ||d
¬«      }t        j                  d   dddœddœd¬«      } | j                   r| j
                  «       j                  d«      nd }|s(t	        d| j"                  › d| j$                  d d › «       |S # t        $ r+}t	        d
t        |«      j                  › «       Y d }~Œªd }~ww xY w)NÚ
EGMS_TOKENÚ zSfalta el secreto EGMS_TOKEN en GitHub (Settings > Secrets and variables > Actions).Ú
private_keyzutf-8Ú	client_idÚ user_idÚ	token_urii  )ÚissÚsubÚaudÚiatÚexpÚRS256)Ú	algorithmuy   el secreto EGMS_TOKEN no tiene el formato esperado. Debe contener TODO el texto del archivo token.jwt. Detalle tÃ©cnico: úapplication/jsonz!application/x-www-form-urlencoded)ÚAcceptúContent-Typez+urn:ietf:params:oauth:grant-type:jwt-bearer)Ú
grant_typeÚ	assertioné<   ©Ú headersÚdataÚ timeoutÚaccess_tokenu'   el servicio rechazÃ³ el token (cÃ³digo z`). Puede haber caducado: genera uno nuevo en la web del CLMS y actualiza el secreto. Respuesta: éÈ   )ÚosÚ environÚgetÚstripr   ÚjsonÚloadsÚencodeÚintÚtimeÚjwtÚ	ExceptionÚtypeÚ__name__ÚrequestsÚpostÚokÚ
status_codeÚtext)	ÚrawÚkÚclaveÚahoraÚclaimsÚgrantÚeÚrÚats	            r   Útoken_accesorO      s]  € Ü
*‰*.‰.˜ rÓ
*×
0Ñ
0Ó
2€CÙ
ÜÐdÔeð	KÜJ‰Js‹OˆØ-Ñ ×'Ñ'¨ Ó0ˆÜ”D—I‘I“KÓ ˆØ˜;™°°)±ÀQÀ{Á^Ø u¨t¡|ñ5ˆä—
‘
˜6 5°GÔ<ˆô 	
‰
a˜
‘nØ);ÐMpÑqØ*WÐfkÑlØ ô 	"€Að *+¯ªˆ‰‹‰nÔ	%°4€BÙ

ÜÐ8¸¿¹¸ð HYØYZ×Y_ÑY_Ð`dÐadÐYeÐXfðhô 	ià

€Iøô ò KÜð 7Ü7;¸A³w×7GÑ7GÐ6HðJ÷ 	Kñ 	KûðKús   ½A2D* Ä*	EÄ3!EÅEc           	      óZ  — t         j                  j                  dd«      j                   «       }|sgt	        j                  t
        › d| d¬«      j
                  «       }t        |t        «      r|st        dt        |«      d d  › «       t        |«      d   }d t        t        g|gt        d	œ}t	        j                  t
        › d
i | ¥d
di¥t
        j                   |«      d
¬«      }|j
                  «       }|j                  d«      s!t        d|› d|j                  dd«      › «       ||fS )NÚ RELEASEr   z	/releasesr-   )r/   r1   z0no pude obtener la lista de versiones del EGMS: r3   éÿÿÿÿ)ÚidÚbboxÚlevelsÚreleasesÚ
productTypez /searchr*   r(   éx   r.   Úhitsu%   la bÃºsqueda no devolviÃ³ datos para z. Mensaje del servicio: Ú messageú-)r4   r5   r6   r7   rA   ÚAPIr8   Ú
isinstanceÚlistr   ÚstrÚsortedÚBBOXÚNIVELÚTIPOrB   Údumps)ÚcabÚrelÚlistaÚqrM   Úress         r   Úbuscar_productorj   3   s
  € Ü
*‰*.‰.˜ BÓ
'×
-Ñ
-Ó
/€CÙ
Ü—‘¤˜u IÐ.¸ÀRÔH×MÑMÓOˆÜ˜%¤Ô&©eÜÐEÄcÈ%ÃjÐQUÐRUÐFVÐEWÐXÔYÜU‹m˜BÑˆØœT¬e¨WÀ3À%ÔX\Ñ]€AÜ
‰
œ˜˜WoÐ/Z°#Ð/Z°~ÐGYÑ/ZÜŸ:™: a›=°#ô	7€Aà

&‰&‹(€CØ
7‰76Œ?ÜÐ6°s°eÐ;SÐTW×T[ÑT[Ð\eÐgjÓTkÐSlÐmÔnØ
ˆ8€Or   c           
      óh  — t        dd«      D ]˜  }	 d |fD ]Ž  }t        j                  | |dd¬«      5 }|j                  dv r|€
	 d d d «       Œ7|j	                  «        t
        |d «      5 }|j
                  d«      D ]  } |j                  | «       Œ 	 d d d «       	 d d d «         y  Œš t        d| j                  d
«      d   › «       y # 1 sw Y   Œ9xY w# 1 sw Y   ŒÉxY w# t        $ rG}t        d	|› d
t        |«      j                  › «       t        j                  d
|z  «       Y d }~Œd }~ww xY w)Nr   é   Ti,  )r/   Ústreamr1   )i‘  i“  Úwbi   z
   intento z
 fallido: é
   zno se pudo descargar ú?r   )ÚrangerA   r6   rD   Úraise_for_statusÚopenÚiter_contentÚwriter>   r   r?   r@   r<   Úsleepr   Úsplit)	ÚurlÚ destinore   Ú intentoÚhrM   ÚfÚtrozorL   s	            r   Ú	descargarr~   C   s5  € Ü˜˜A“;ò 
%ˆ ð	%Ø˜C[ò 
Ü—\‘\ #¨q¸ÀsÔKð  ÈqØ—}‘}¨
Ñ2°q°yØ ÷ ð  ð ×&Ñ&Ô(Ü˜g tÓ,ð +°Ø%&§^¡^°GÓ%<ò +˜EØŸG™G ENñ+÷+ð ÷ ò  ñ
ð
%ô 
Ð
" 3§9¡9¨S£>°!Ñ#4Ð"5Ð
6Õ7÷+ð +ú÷	 ð  ûô ò 	%Ü+˜g˜Y j´°a³×1AÑ1AÐ0BÐCÔDÜJ‰Jr˜G‘|×$Ò$ûð	%úsX   ‘ C!±C Á	C!ÁC Á((C		Â	C Â	C!Â%C!Ã	C
Ã C ÃC
Ã C!Ã!	D1Ã*<D,Ä,D1c           
      ó  ‡— t        t        j                  | d¬«      j                  «      }|D ci c]!  }|j	                  «       j
                  «       |“Œ# c}Šˆfd„} |dd«       |dd «      }} |d«       |d	«      } } |d
d
«      }t
        ˆfd„‰D «       d
«      }	||r|s5|r| s1t        dt        j                  j                  | «      › d|d
d › «       |||| ||	fD cg c]   }|sŒ|‘Œ	 }
}d
}
|r|sddl
m} |j                  ddd¬«      }
g }
t        j                  | |
d¬«      D ]  }|
B|
j                  ||   j                  t         «      ||    j                  t         «      «      \  }}n0||   j                  t         «      ||   j                  t         «      }}||   j                  t         «      }|	r||	   j                  t         «      nt#        j$                  t'        |«      «      }t#        j(                  |«      t#        j(                  |«      z  t#        j(                  |«      z  |t*        d   k\  z  |t*        d   k  z  |t*        d   k\  z  |t*        d   k  z  }|
j-                  t#        j.                  ||   ||   ||   ||   g«      j1                  t"        j2                  «      «       Œ |
rt#        j4                  |
«      S t#        j$                  dt"        j2                  «      S c c}w c c}w )uY   Devuelve array N x 4 (lon, lat, velocidad, desviaciÃ³n). Detecta las columnas por nombre.r   )Únrowsc                  ó.   •— t        ˆfd„| D «       d «      S )Nc              3   ó2   •K  — | ]  }|‰v sŒ‰|   –— Œ y ­w)N© )Ú.0ÚnÚlows     €r   ú	<genexpr>z-leer_csv.<locals>.<lambda>.<locals>.<genexpr>Y   s   øè ø€ Ò>¨!°Q¸#²X˜s 1vÑ>ùs   ƒ	
)Únext)Únsr†   s    €r   ú<lambda>zleer_csv.<locals>.<lambda>Y   s   ø€ œÓ>¨rÔ>ÀÓE€ r   Ú	longitudeÚlonÚlatitudeÚlatÚ eastingÚnorthingÚ
mean_velocityÚvelocityc              3   ó<   •K  — | ]  }d |v sŒd|v sŒ
‰|   –— Œ y­w)ÚstdÚvelNrƒ   )r„   Úcr†   s     €r   r‡   zleer_csv.<locals>.<genexpr>]   s!   øè ø€ Ò@˜! e¨q¢j°U¸a²Zˆs1vÑ@ùs   ƒ	’
Nzno reconozco las columnas de z. Columnas: é   )Ú
TransformeriÛ
  iæ  T)Ú	always_xyi ¡  )Ú usecolsÚ	chunksizeé   r   é   ©r   rl   )r^   ÚpdÚread_csvÚ columnsÚlowerr7   rˆ   r   r4   ÚpathÚbasenameÚpyprojr˜   Úfrom_crsÚ	transformÚto_numpyÚfloatÚnpÚzerosÚlenÚisfiniteÚLIMÚappendÚcolumn_stackÚastypeÚ float32Úvstack)ÚrutaÚcolsr–   ÚbuscarÚclonÚclatÚceÚcnÚcvÚcsÚusarÚtransr˜   ÚpartesÚchrŒ   rŽ   ÚvÚsrC   r†   s                       @r   Úleer_csvrÃ   U   sž  ø€ ä
”—
‘
˜D¨Ô*×2Ñ2Ó
3€DØ)-Ö
. Aˆ17‰7‹9?‰?Ó
˜aÑ
Ò
.€CÛ
E€FÙ˜
 UÓ+©V°JÀÓ-Fˆ$€DÙ
IÓ
¡ zÓ 2ˆ€BÙ	 Ó	,€BÜ	
Ó@˜sÔ@À$Ó	G€BØ 	€z™4¡D©b±RÜÐ.¬r¯w©w×/?Ñ/?ÀÓ/EÐ.FÀlÐSWÐX[ÐY[ÐS\ÐR]Ð^Ô_Ø˜d B¨¨B°Ð3Ö
9!²qŠAÐ
9€DÐ
9Ø€EÙ‘TÝ&Ø×$Ñ$ T¨4¸4Ð$Ó@ˆØ
€FÜk‰k˜$¨¸ Ô@ó 	\ˆØ
Ð
Ø—‘ r¨"¡v§¡´uÓ'=¸rÀ"¹v¿¹ÌuÓ?UÓV‰HˆC‘à˜$‘x×(Ñ(¬Ó/°°D±×1BÑ1BÄ5Ó1IˆCØˆr‰FO‰OœEÓ"ˆÙ&(ˆBˆr‰FO‰OœEÔ"¬b¯h©h´s¸2³wÓ.?ˆÜk‰k˜#Ó¤§¡¨SÓ!1Ñ1´B·K±KÀ³NÑBØ”c˜!‘f‰}ñØ!$¬¨A©¡ñ0Ø36¼#¸a¹&±=ñBØEHÌCÐPQÉFÁ]ñTˆà
‰
”b—o‘o s¨2¡w°°B± ¸¸2¹ÀÀ"ÁÐ&FÓG×NÑNÌrÏzÉzÓZÖ[ð	\ñ !'Œ29‰9VÓ
ÐH¬B¯H©H°V¼R¿Z¹ZÓ,HÐHùò1 
/ùò :s   °&K7Ã# K<Ã+K<c                  óè  — t        j                  t        d¬«       t         j                  j	                  t        d«      } t         j                  j
                  | «      rt
        j                  t        | «      «      ni }t         j                  j                  dd«      j                  «       dk(  }t        «       }d |› dd	œ}t        |«      \  }}|d
   } t        d
„ | D «       «      }t        d|› d
t!        | «      › d«       ||j                  d«      k(  r|st        d«       y t        d«       g }	t#        j$                  «       5 }
t'        | d«      D ]w  \  }
}t        d|
› dt!        | «      › d|d   › d|j                  dd«      dz
  d›d	«       t         j                  j	                  |
|d   «      }
t)        t*        › d|d   › d|d   › |
|«       t         j                  j	                  |
d |
› «      }t-        j.                  |
«      5 }|j1                  |«       d d d «       t        j2                  |
«       t5        j4                  t         j                  j	                  |d!d"«      d¬#«      D ]W  }|	j7                  t9        |«      «       t        d$t         j                  j;                  |«      › d%t!        |	d&   «      › d'«       ŒY Œz 	 d d d «       |	rt=        j>                  |	«      n#t=        j@                  d(t<        jB                  «      }t!        |«      d)k  rtE        d*t!        |«      › d+«       |jG                  d,«      jI                  t         j                  j	                  t        d-«      «       |tK        d.„ | D «       «      tM        t!        |«      «      tN        tP        tS        jT                  tV        jX                  «      j[                  d/«      d0œ}t
        j\                  |t        t         j                  j	                  t        d1«      d2«      «       t
        j\                  ||d3œt        | d2«      «       t        d4t!        |«      › d5«       y # 1 sw Y   Œ?xY w# 1 sw Y   Œ›xY w)6NT)Úexist_okz
estado.jsonÚFORZARÚfalseÚtruez Bearer r(   )Ú
Authorizationr)   rY   c              3   óN   K  — | ]  }|d    › d|j                  d«      › –— Œ y­w)Úfilenameú|Ú versionN)r6   ©r„   r{   s     r   r‡   zmain.<locals>.<genexpr>}   s)   è ø€ ÒG¸Qa˜
‘m_ A a§e¡e¨IÓ&6Ð%7Ô8ÑGùs   ‚#%u   VersiÃ³n del EGMS: u    Â· z	 archivosÚfirmauC   Sin cambios desde la Ãºltima actualizaciÃ³n. No hay nada que hacer.u:   Hay datos nuevos (o se forzÃ³ la descarga). Descargando...r   z [ú/z] rË   z (Úfilesizer   g    €„.Az.0fz MB)z
/download/z?id=rS   Útz**z*.csv)Ú	recursivez    z: rR   z puntos en Balearesrž   éd   zsolo se obtuvieron z9 puntos en Baleares; no sobrescribo los datos anteriores.z<f4z
puntos.binc              3   óP   K  — | ]  }t        |j                  d «      «      –— Œ  y­w)rÍ   N)r_   r6   rÎ   s     r   r‡   zmain.<locals>.<genexpr>–   s   è ø€ Ò*OÀQ¬3¨q¯u©u°YÓ/?×+@Ñ*Oùs   ‚$&z%Y-%m-%d)Ú releaserÍ   Ún_puntosÚnivelÚtipoÚgeneradoz	meta.jsonÚw)rÏ   rÖ   z Listo: z puntos guardados.)/r4   ÚmakedirsÚSALIDAr£   ÚjoinÚexistsr8   Úloadrs   r5   r6   r¢   rO   rj   r`   r   r¬   ÚtempfileÚTemporaryDirectoryÚ	enumerater~   r\   Ú zipfileÚ ZipFileÚ
extractallÚremoveÚglobr¯   rÃ   r¤   rª   r³   r«   r²   r   r±   ÚtofileÚmaxr;   rb   rc   r   Únowr   ÚutcÚstrftimeÚdump)Ú
ruta_estadoÚestadoÚforzarrN   re   rf   ri   rY   rÏ   r¿   ÚtmpÚir{   Úzip_rutaÚ carpetaÚzÚcsvr
   Úmetas                      r   Úmainrù   s   s{  € Ü‡KK” Õ&Ü—'‘'—,‘,œv }Ó5€KÜ-/¯W©W¯^©^¸KÔ-HŒTY‰Y”t˜KÓ(Ô
)Èb€FÜ
Z‰Z^‰^˜H gÓ
.×
4Ñ
4Ó
6¸&Ñ
@€Fä	‹€BØ% b T˜NÐ6HÑ
I€CÜ˜sÓ#H€CˆØ
ˆv‰;€DÜÑGÀ$ÔGÓG€EÜ Ð
˜c˜U $¤s¨4£y k°Ð;Ô<Ø —
‘
˜7Ó#Ò #©FÜ
ÐQÔRØä ÐDÔEØ
€FÜ	×	$Ñ	$Ó	&ð 
Z¨#Ü˜d AÓ&ó 
	Z‰DˆAˆqÜ"QCqœ˜T›˜
 2 a¨
¡m _°B°q·u±u¸ZÈÓ7KÈcÑ7QÐRUÐ6VÐVZÐ[Ô\Ü—w‘w—|‘| C¨¨:©Ó7ˆHÜœ˜˜Z¨¨*©
 °d¸3¸t¹9¸+ÐFÈÐRUÔVÜ—g‘g—l‘l 3¨!¨A¨3¨ Ó0ˆGÜ—‘ Ó*ð 
&¨aØ—‘˜WÔ%÷
&äI‰IhÔÜ—y‘y¤§¡§¡¨g°t¸WÓ!EÐQUÔVò 
ZØ—
‘
œh s›mÔ,Üdœ2Ÿ7™7×+Ñ+¨CÓ0Ð1°´C¸¸r¹
³OÐ3DÐDWÐXÕYò
Zñ
	Z÷
Zñ "(ŒBI‰IfÔ¬R¯X©X°f¼b¿j¹jÓ-I€EÜ 
ˆ5ƒzCÒ ÜÐ$¤S¨£Z LÐ0iÐjÔkà	‡LLÓ×ÑœrŸw™wŸ|™|¬F°LÓAÔBØ¤sÑ*OÈ$Ô*OÓ'OÜœC ›J›´%ÄÜ Ÿ™¤X§\¡\Ó2×;Ñ;¸JÓGñI€Dô 	‡IIˆd”DœŸ™Ÿ™¤f¨kÓ:¸CÓ@ÔAÜ‡II˜¨#Ñ.´°[À#Ó0FÔGÜ ˆ'”#e“*Ð/Ð0Õ1÷!
&ñ 
&ú÷

Zñ 
Zús&   ÅCQ'È
Q ÈB0Q'ÑQ$
ÑQ'Ñ'Q1 Ú__main__) Ú __doc__r4   r   r8   r<   rä   rá   rè   r   r   rA   r=   Únumpyrª   ÚpandasrŸ   r\   ra   r®   rb   rc   r£   rÞ   rÝ   r   r   rO   rj   r~   rÃ   rù   r@   rƒ   r   r   ú<module>rþ      s•   ðñQç 3× 3× 3Ó 3ß 'ß Û Û à9€Ø	
ˆuˆ
˜˜e}Ð %€Ø €Ø
€€tØ	
‰‰e˜WÓ	%€òòò
ò2
ò 8ò$Iò<(2ðV ˆzÒÙ…Fð r   
