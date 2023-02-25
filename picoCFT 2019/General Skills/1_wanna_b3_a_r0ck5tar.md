## Descripción
I wrote you another [song](https://jupiter.challenges.picoctf.org/static/62f0cc3605aaf108a4f743b5b7f0dac4/lyrics.txt). Put the flag in the picoCTF{} flag format.

NOTE: The Rockstar language has changed since this problem was released! Use this Wayback Machine URL to use an older version of Rockstar, [here](https://web.archive.org/web/20190522020843/https://codewithrockstar.com/online).
## Solución
```bash()
picoCTF{BONJOVI}
```

## Notas adicionales
Al escribir la canción en [codewithrockstar.com](https://codewithrockstar.com/online) no me daba ninguna salida, asi que leyendo la documentación de la pagina, encontre en el aparatado <b>### Flow Control and Block Syntax</b> que el  "Las expresiones condicionales comienzan con la palabra clave If, seguida de una expresión. Si la expresión se evalúa como verdadera, se ejecuta el siguiente bloque de código. Opcionalmente, se puede escribir un bloque Else después de un bloque If. El bloque de código que sigue a la palabra clave Else se ejecutaría si la expresión If se evaluara como falsa." Por lo que si o si se tenian que borrar completamente las lineas que contenian estas palabras clave.
Despues de editar la canción, la pagina me arrojo una cadena de numeros decimales, la cual traduje en  [rapidtables.com](https://www.rapidtables.com/convert/number/ascii-hex-bin-dec-converter.html).

## Referencias 
[codewithrockstar.com/docs](https://web.archive.org/web/20190521190259/https://codewithrockstar.com/docs)