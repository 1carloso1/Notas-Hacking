## Descripción
Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. What's the final one? Image: [this](https://mercury.picoctf.net/static/b6205dd933ec01c022c4e6acbdf11116/dolls.jpg)

## Solución
```bash()
┌──(kali㉿kali)-[~/Downloads]
└─$ binwalk -e dolls.jpg 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 594 x 1104, 8-bit/color RGBA, non-interlaced
3226          0xC9A           TIFF image data, big-endian, offset of first image directory: 8
272492        0x4286C         Zip archive data, at least v2.0 to extract, compressed size: 378950, uncompressed size: 383938, name: base_images/2_c.jpg
651608        0x9F158         End of Zip archive, footer length: 22

┌──(kali㉿kali)-[~/Downloads]
└─$ ls   
dolls.jpg  _dolls.jpg.extracted

┌──(kali㉿kali)-[~/Downloads]
└─$ cd _dolls.jpg.extracted  

┌──(kali㉿kali)-[~/Downloads/_dolls.jpg.extracted]
└─$ ls    
4286C.zip  base_images  

┌──(kali㉿kali)-[~/Downloads/_dolls.jpg.extracted]
└─$ cd base_images              

┌──(kali㉿kali)-[~/Downloads/_dolls.jpg.extracted/base_images]
└─$ ls
2_c.jpg     

┌──(kali㉿kali)-[~/Downloads/_dolls.jpg.extracted/base_images]
└─$ binwalk -e 2_c.jpg  

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 526 x 1106, 8-bit/color RGBA, non-interlaced
3226          0xC9A           TIFF image data, big-endian, offset of first image directory: 8
187707        0x2DD3B         Zip archive data, at least v2.0 to extract, compressed size: 196043, uncompressed size: 201445, name: base_images/3_c.jpg
383805        0x5DB3D         End of Zip archive, footer length: 22
383916        0x5DBAC         End of Zip archive, footer length: 22

┌──(kali㉿kali)-[~/Downloads/_dolls.jpg.extracted/base_images]
└─$ ls
2_c.jpg  _2_c.jpg.extracted

┌──(kali㉿kali)-[~/Downloads/_dolls.jpg.extracted/base_images]
└─$ cd _2_c.jpg.extracted  

┌──(kali㉿kali)-[~/Downloads/_dolls.jpg.extracted/base_images/_2_c.jpg.extracted]
└─$ ls
2DD3B.zip  base_images

┌──(kali㉿kali)-[~/Downloads/_dolls.jpg.extracted/base_images/_2_c.jpg.extracted]
└─$ cd base_images       

┌──(kali㉿kali)-[~/…/_dolls.jpg.extracted/base_images/_2_c.jpg.extracted/base_images]
└─$ ls
3_c.jpg

┌──(kali㉿kali)-[~/…/_dolls.jpg.extracted/base_images/_2_c.jpg.extracted/base_images]
└─$ binwalk -e 3_c.jpg 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 428 x 1104, 8-bit/color RGBA, non-interlaced
3226          0xC9A           TIFF image data, big-endian, offset of first image directory: 8
123606        0x1E2D6         Zip archive data, at least v2.0 to extract, compressed size: 77651, uncompressed size: 79809, name: base_images/4_c.jpg
201423        0x312CF         End of Zip archive, footer length: 22

┌──(kali㉿kali)-[~/…/_dolls.jpg.extracted/base_images/_2_c.jpg.extracted/base_images]
└─$ ls
3_c.jpg  _3_c.jpg.extracted

┌──(kali㉿kali)-[~/…/_dolls.jpg.extracted/base_images/_2_c.jpg.extracted/base_images]
└─$ cd _3_c.jpg.extracted 

┌──(kali㉿kali)-[~/…/base_images/_2_c.jpg.extracted/base_images/_3_c.jpg.extracted]
└─$ ls
1E2D6.zip  base_images

┌──(kali㉿kali)-[~/…/base_images/_2_c.jpg.extracted/base_images/_3_c.jpg.extracted]
└─$ cd base_images       

┌──(kali㉿kali)-[~/…/_2_c.jpg.extracted/base_images/_3_c.jpg.extracted/base_images]
└─$ ls
4_c.jpg

┌──(kali㉿kali)-[~/…/_2_c.jpg.extracted/base_images/_3_c.jpg.extracted/base_images]
└─$ binwalk -e 4_c.jpg 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 320 x 768, 8-bit/color RGBA, non-interlaced
3226          0xC9A           TIFF image data, big-endian, offset of first image directory: 8
79578         0x136DA         Zip archive data, at least v2.0 to extract, compressed size: 65, uncompressed size: 81, name: flag.txt
79787         0x137AB         End of Zip archive, footer length: 22
   
┌──(kali㉿kali)-[~/…/_2_c.jpg.extracted/base_images/_3_c.jpg.extracted/base_images]
└─$ cd _4_c.jpg.extracted 

┌──(kali㉿kali)-[~/…/base_images/_3_c.jpg.extracted/base_images/_4_c.jpg.extracted]
└─$ ls
136DA.zip  flag.txt

┌──(kali㉿kali)-[~/…/base_images/_3_c.jpg.extracted/base_images/_4_c.jpg.extracted]
└─$ cat flag.txt         
picoCTF{4f11048e83ffc7d342a15bd2309b47de} 
```

## Notas adicionales
- `exiftool`: Leer y escribir metainformación en archivos
- `binwalk`: es una herramienta para buscar una imagen binaria dada para archivos incrustados y código ejecutable. Específicamente, está diseñado para identificar archivos y códigos incrustados dentro de imágenes de firmware.
- `binwalk -e`: --extract Extrae automáticamente tipos de archivos conocidos.
- Para relizar esta actividad, primero checamos los metadatos de la imagen original con `exiftool`, al no encontrar nada, utilizamos el comando `binwalk -e` para ver si encontraba alguna imagen incrustada, al ver que si, volvimos a repetir el procedimiento con cada imagen nueva hasta toparnos con loa flag.,
## Referencias 
- [Documentación Binwalk](https://www.kali.org/tools/binwalk/)
- [Documentación Exiftool](https://exiftool.org/exiftool_pod.html)