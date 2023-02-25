
## Descripción
Sometimes you need to handle process data outside of a file. Can you find a way to keep the output from this program and search for the flag? Connect to jupiter.challenges.picoctf.org 4427.

## Solución
```bash()
┌──(kali㉿kali)-[~]
└─$ nc jupiter.challenges.picoctf.org 4427 | grep pico
picoCTF{digital_plumb3r_5ea1fbd7}
```

## Notas adicionales
Al conctarme al servidor me arrojó varias lineas de texto, por lo que utilizando <b>grep</b> filtre el formato que tiene la flag para obtener el resultado correcto.
## Referencias 
