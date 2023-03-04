
## Descripción
What integer does this program print with arguments 266134863 and 1592237099? File: chall.S Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})

## Solución
- Para relizar esta actividad de la manera mas facil sin necesidad de conocer sobre `ARM` . Para empezar se nos dan dos numeros enteros decimales `266134863` and `1592237099`.
- Se nos da la pista de que la flag es un numero hexadecimal, en minusculas y de 32 bits. Por lo que se procede a convertir las cadenas decimales a cadenas hexadecimales. Por lo que unsando [rapidtables](https://www.rapidtables.com/convert/number/decimal-to-binary.html)
- Al obtener las cadenas, utilizando el python de la consola de comandos, imprimi la cadena en minusculas usando el metodo `.lowercase()`.

```bash()
>>> argument1 = "0FDCE54F"
>>> argument2 = "5EE79C2B"
>>> print (argument1.lower() + "\n" + argument2.lower())
0fdce54f
5ee79c2b
```

- Probe ambos resultados con el formato de la FLAG hasta obtener la flag correcta, por lo que la solución a este problema es: 

```bash()
picoCFT{5ee79c2b}
```

## Notas adicionales
- Hay una manera de obtener que numero convertir en decimal exactamente. Esto requiere de conocimiento basico en ARM Assembly. por lo que es un poco tardado obtener este resultado de esta manera. Si se desea hacer asi, [github.com/xnom](https://github.com/xnomas/PicoCTF-2021-Writeups/tree/main/ARMssembly-0) lo hace de una manera facil de entender. 

## Referencias 