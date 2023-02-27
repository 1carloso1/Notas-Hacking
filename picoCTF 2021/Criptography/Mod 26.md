## Descripción
Cryptography can be easy, do you know what ROT13 is? `cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_hyLicInt}`

## Solución
```bash()
┌──(kali㉿kali)-[~]
└─$ echo "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_hyLicInt}" > flag.txt                                                                          
┌──(kali㉿kali)-[~]
└─$ cat flag.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
picoCTF{next_time_I'll_try_2_rounds_of_rot13_ulYvpVag}
```

## Notas adicionales
La flag fue ocultada, las palabras fueron rotadas 13 veces, es decir, la letra original fue cambiada por la letra que esta 13 lugares despues (rot13)
<b>tr</b>: se utiliza para traducir/transformar datos de una forma a otra

## Referencias 