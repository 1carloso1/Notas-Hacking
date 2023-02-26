## Descripción
Can you look at the data in this binary: [static](https://mercury.picoctf.net/static/0f6ea599582dcce7b4f1ba94e3617baf/static)? This [BASH script](https://mercury.picoctf.net/static/0f6ea599582dcce7b4f1ba94e3617baf/ltdis.sh) might help!

## Solución
```bash()
┌──(kali㉿kali)-[~/Downloads]
└─$ ./ltdis.sh static
Attempting disassembly of static ...
Disassembly successful! Available at: static.ltdis.x86_64.txt
Ripping strings from binary with file offsets...
Any strings found in static have been written to static.ltdis.strings.txt with file offset                     
┌──(kali㉿kali)-[~/Downloads]
└─$ ls
ltdis.sh  static  static.ltdis.strings.txt  static.ltdis.x86_64.txt
┌──(kali㉿kali)-[~/Downloads]
└─$ strings static.ltdis.strings.txt | grep pico
   1020 picoCTF{d15a5m_t34s3r_6f8c8200}
```

## Notas adicionales
Al ver el nombre strings en el archivo, intui que con el comando strings obtendria algo, y a la primera obtuve la bandera.

## Referencias 
