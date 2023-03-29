## Descripción
Try reversing this file? Can ya? I forgot the password to this file. Please find it for me?

## Solución
- Para obtener la flag de este reto, vemos que se nos da un archivo llamado `ret`.
- Al ver su contenido con el comando `cat`, podemos ver que nos da muchos signos extraños, lo que automáticamente nos da a entender que con el comando `strings` podremos obtener el contenido.
- Agregando `| grep pico` al comando, podremos encontrar la flag sin necesidad de buscar en todo el archivo

```bash()
picoCTF{3lf_r3v3r5ing_succe55ful_3f1331e7}
```

## Notas adicionales

## Referencias 