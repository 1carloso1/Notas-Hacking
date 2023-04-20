## Descripción
Download this image and find the flag.

-   [Download image](https://artifacts.picoctf.net/c/216/pico.flag.png)

## Pistas
-We know the end sequence of the message will be `$t3g0`.

## Solución
- Para realizar este actividad, el nombre nos da una pista, ya que el nombre St3go hace referencia a la esteganografía.
- La herramienta principal que queria utilizar para la esteganografía es `steghide`, pero no es posible usarlo ya que el formato .PNG es incompatible con esta herramienta.
- Investigando en foros, la herramienta para este caso es `zsteg`, ya que acepta tanto .PNG como .BMP.
- Para obtener la flag, utilice el siguiente comando:

```shell()
─$ zsteg pico.flag.png 
b1,rgb,lsb,xy       .. text: "picoCTF{7h3r3_15_n0_5p00n_a1062667}$t3g0"
b1,abgr,lsb,xy      .. text: "E2A5q4E%uSA"
b2,b,lsb,xy         .. text: "AAPAAQTAAA"
b2,b,msb,xy         .. text: "HWUUUUUU"
b2,a,lsb,xy         .. file: Matlab v4 mat-file (little endian) >\004<\305P, numeric, rows 0, columns 0
b2,a,msb,xy         .. file: Matlab v4 mat-file (little endian) | <\243, numeric, rows 0, columns 0
b3,r,lsb,xy         .. file: gfxboot compiled html help file
b4,r,lsb,xy         .. file: Targa image data (16-273) 65536 x 4097 x 1 +4352 +4369 - 1-bit alpha - right "\021\020\001\001\021\021\001\001\021\021\001"                                                                                                                                        
b4,g,lsb,xy         .. file: 0420 Alliant virtual executable not stripped
b4,b,lsb,xy         .. file: Targa image data - Map 272 x 17 x 16 +257 +272 - 1-bit alpha "\020\001\021\001\021\020\020\001\020\001\020\001"
b4,bgr,lsb,xy       .. file: Targa image data - Map 273 x 272 x 16 +1 +4113 - 1-bit alpha "\020\001\001\001"
b4,rgba,lsb,xy      .. file: Novell LANalyzer capture file
b4,rgba,msb,xy      .. file: Applesoft BASIC program data, first line number 8
b4,abgr,lsb,xy      .. file: Novell LANalyzer capture file

```

- Donde podemos obsevar que la flag es:

```bash()
picoCTF{7h3r3_15_n0_5p00n_a1062667}
```

## Notas adicionales
- zsteg es una herramienta que puede detectar datos ocultos en archivos png y bmp.

## Referencias 
- [El foro donde encontre la herramienta](https://book.hacktricks.xyz/crypto-and-stego/stego-tricks)
