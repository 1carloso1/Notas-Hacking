## Descripción
We found this file. Recover the flag.

## Pistas
-Weird that it won't display right...

## Solución
-Para resolver este reto, el primer paso fue cambiarle el nombre del archivo `tunn3l_v1s10n` a `tunn3l_v1s10n.bmp`, ya que le faltaba la extension al archivo. Esto se puede comprobar tambien con el comando `exiftool`.
- Como la imagen no se puede abrir, iremos a la herramienta `HxD` para ver su composicion en hexadecimal. Analizandola, vemos que tiene varios fallos en su cabecera. Por lo wir cambiamos la primera fila por:

```bash()
offset   00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15
00000000 42 4D 8E 26 2C 00 00 00 00 00 28 00 00 00 28 00
```

- Despues de corregir esto, ya podemos abrir la imagen, pero esta incompleta, por lo que ahora tenemos que modificar el tamaño para obtener la imagencompleta:

```bash()
offset   00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15
00000016 00 00 6E 04 00 00 42 03 00 00 01 00 18 00 00 00
```

- Despues de modificar esto, podremos ver la bandera hasta arriba de la imagen:

```bash()
picoCTF{qu1t3_a_v13w_2020}
```

## Notas adicionales
- Es parecido al reto donde modificamos la cabecera a un archivo .PNG

## Referencias 
- [WIKIPEDIA](https://en.wikipedia.org/wiki/BMP_file_format)