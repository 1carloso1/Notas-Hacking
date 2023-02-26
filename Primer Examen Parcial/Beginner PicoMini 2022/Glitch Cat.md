
## Descripción
Our flag printing service has started glitching! 

$ nc saturn.picoctf.net 65353

## Solución
```bash()
┌──(kali㉿kali)-[~]
└─$ nc saturn.picoctf.net 65353
'picoCTF{gl17ch_m3_n07_' + chr(0x39) + chr(0x63) + chr(0x34) + chr(0x32) + chr(0x61) + chr(0x34) + chr(0x35) + chr(0x64) + '}'

┌──(kali㉿kali)-[~]
└─$ python3          
Python 3.10.9 (main, Dec  7 2022, 13:47:07) [GCC 12.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> print('picoCTF{gl17ch_m3_n07_' + chr(0x39) + chr(0x63) + chr(0x34) + chr(0x32) + chr(0x61) + chr(0x34) + chr(0x35) + chr(0x64) + '}')
picoCTF{gl17ch_m3_n07_9c42a45d}
>>> exit()
```

## Notas adicionales
Al ver el formato de lo que obtuve con netcat, me di cuenta que tenia la estructura del contenido de un print()  en python, por lo que intente meterlo en la funcion print(), y me dio la flag.
## Referencias 
