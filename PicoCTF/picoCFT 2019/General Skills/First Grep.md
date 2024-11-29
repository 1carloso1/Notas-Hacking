## Descripción
Can you find the flag in [file](https://jupiter.challenges.picoctf.org/static/515f19f3612bfd97cd3f0c0ba32bd864/file)? This would be really tedious to look through manually, something tells me there is a better way.

## Solución
```bash()
┌──(kali㉿kali)-[~/Downloads]
└─$ ls -la
total 800
drwxr-xr-x  2 kali kali   4096 Feb 24 19:05 .
drwxr-xr-x 30 kali kali   4096 Feb 24 18:59 ..
-rw-r--r--  1 kali kali  14551 Feb 24 19:05 file
┌──(kali㉿kali)-[~/Downloads]
└─$ cat file| grep pico
picoCTF{grep_is_good_to_find_things_5af9d829}
```

## Notas adicionales
Utilice cat por que el archivo descargado tiene las propiedades read-write

## Referencias 