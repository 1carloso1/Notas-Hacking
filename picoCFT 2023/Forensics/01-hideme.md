## Descripción:
Every file gets a flag.The SOC analyst saw one image been sent back and forth between two people. They decided to investigate and found out that there was more than what meets the eye [here](https://artifacts.picoctf.net/c/490/flag.png).

**Hints:**

## Solución:
1. En este reto se nos proporciona una imagen: 

```bash
┌──(kali㉿kali)-[~/picoCTF-2023/forensics/hideme]
└─$ ls
flag.png

┌──(kali㉿kali)-[~/picoCTF-2023/forensics/hideme]
└─$ 
```

2. Al analizar la imagen podemos darnos cuenta que la imagen contiene una carepeta oculta dentro de ella:

```bash
┌──(kali㉿kali)-[~/picoCTF-2023/forensics/hideme]
└─$ strings flag.png | grep secret
secret/UT
secret/flag.pngUT
secret/UT
secret/flag.pngUT

┌──(kali㉿kali)-[~/picoCTF-2023/forensics/hideme]
└─$
```

3. Al extraer el contenido de la imagen obtenemos lo siguiente:

```bash
┌──(kali㉿kali)-[~/picoCTF-2023/forensics/hideme]
└─$ binwalk -e flag.png  

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 512 x 504, 8-bit/color RGBA, non-interlaced
41            0x29            Zlib compressed data, compressed
39739         0x9B3B          Zip archive data, at least v1.0 to extract, name: secret/
39804         0x9B7C          Zip archive data, at least v2.0 to extract, compressed size: 2861, uncompressed size: 3010, name: secret/flag.png
42900         0xA794          End of Zip archive, footer length: 22
                                                             
┌──(kali㉿kali)-[~/picoCTF-2023/forensics/hideme]
└─$ ls
flag.png  _flag.png.extracted

┌──(kali㉿kali)-[~/picoCTF-2023/forensics/hideme]
└─$ 
```

4. Vemos que se extrajo una carpeta que estaba oculta en la imagen al revisar la carpeta encontramos el siguiente contenido: 

```bash
┌──(kali㉿kali)-[~/picoCTF-2023/forensics/hideme/_flag.png.extracted]
└─$ ls
29  29.zlib  9B3B.zip  secret
                                                                                                                                                             
┌──(kali㉿kali)-[~/picoCTF-2023/forensics/hideme/_flag.png.extracted]
└─$ 
```

5. vemos que dentro se la carpeta existe otra carpeta llamada `secret` la cual tiene una imagen en dicha imagen podemos observar la flag:  

```bash
┌──(kali㉿kali)-[~/…/forensics/hideme/_flag.png.extracted/secret]
└─$ ls
flag.png
                                                                                                                                                             
┌──(kali㉿kali)-[~/…/forensics/hideme/_flag.png.extracted/secret]
└─$ 
```

### Flag: picoCTF{Hiddinng_An_imag3_within_@n_ima9e_81cc7947}

## Notas adicionales:
| Comando | Descripción |
| --- | --- |
| binwalk | Binwalk es una herramienta rápida y fácil de usar para analizar, realizar ingeniería inversa y extraer imágenes de firmware. |

## Referencias :
- https://www.kali.org/tools/binwalk/