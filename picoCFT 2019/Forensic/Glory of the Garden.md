
## Descripción
This garden contains more than it seems.

## Pistas
- What is a hex editor?

## Solución
- Para resolver este reto, se nos da un archivo.jpg, pero ante de abrir `hezeditor` probe utilizando el comando `strings | grep picoCTF` para ver si la imagen tenia tan obivio el mensaje oculto, lo que si fue el caso, por lo que me dio la flag.

```bash()
picoCTF{more_than_m33ts_the_3y33dd2eEF5}
```

## Notas adicionales
- El reto tambien se puede resolver a traves de `hexeditor`, ya que al ejecutarlo junto con la imagen nos da caracteres en hexadeciamal y su traducción a ASCII, teniendo la flag hasta el final de el texto.

## Referencias 
