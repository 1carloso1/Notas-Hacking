## Descripción:
How about some hide and seek heh?Look at this image [here](https://artifacts.picoctf.net/c/237/atbash.jpg).

**Hints:**
1. Download the image and try to extract it.

## Solución:

```bash
┌──(kali㉿kali)-[~/picoCTF-2023/Cryptography/HideToSee]
└─$ ls
atbash.jpg
                                                                                                                                                 
┌──(kali㉿kali)-[~/picoCTF-2023/Cryptography/HideToSee]
└─$ steghide info atbash.jpg                     
"atbash.jpg":
  formato: jpeg
  capacidad: 2.4 KB
�Intenta informarse sobre los datos adjuntos? (s/n) s
Anotar salvoconducto: 
  archivo adjunto "encrypted.txt":
    tama�o: 31.0 Byte
    encriptado: rijndael-128, cbc
    compactado: si
                                                                                                                                                 
┌──(kali㉿kali)-[~/picoCTF-2023/Cryptography/HideToSee]
└─$ steghide extract -sf atbash.jpg -xf datos.txt
Anotar salvoconducto: 
anot� los datos extra�dos e/"datos.txt".
                                                                                                                                                 
┌──(kali㉿kali)-[~/picoCTF-2023/Cryptography/HideToSee]
└─$ cat datos.txt 
krxlXGU{zgyzhs_xizxp_05y2z65z}
                                                                                                                                                 
┌──(kali㉿kali)-[~/picoCTF-2023/Cryptography/HideToSee]
└─$
```

Usando la herramienta https://www.dcode.fr/atbash-cipher desencriptamos el mensaje **krxlXGU{zgyzhs_xizxp_05y2z65z}** para obtener la bandera: 

### Flag: picoCTF{atbash_crack_05b2a65a}

## Notas adicionales:

### Esteganografía:
- La **esteganografía**, la práctica de ocultar información, ha existido durante siglos. Y en paralelo a los avances tecnológicos, la esteganografía también ha evolucionado y se ha adaptado con el advenimiento de las computadoras e Internet.
- La **esteganografía online** generalmente implica ocultar datos dentro de archivos inocuos como imágenes, vídeos y audio.

### ¿Qué es Steghide?
- **Steghide** es un programa de esteganografía que permite ocultar datos en varios tipos de imagen y archivos de audio.
- Sus características incluyen el compactado y encriptado de los datos adjuntos, y la revisión automática de integridad usando un checksum.
- Se reconocen los formatos de archivo JPEG, BMP, WAV y AU para usar como archivos de portada.
- El algoritmo de encriptado por omisión es el Rijndael, o EAE (Encrip­tado Avanzado Estándar),  con clave de 128 bits de tamaño en la modalidad de encadenado de bloques de cifras.

## Referencias:
- https://www.dcode.fr/atbash-cipher
- https://steghide.sourceforge.net/documentation/manpage_es.php 
