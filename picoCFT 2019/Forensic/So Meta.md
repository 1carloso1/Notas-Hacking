
## Descripción
Find the flag in this picture.

## Pistas
- What does meta mean in the context of files?
-  Ever heard of metadata?

## Solución
- Para resolver este reto, las pistas son de mucha ayuda, ya que nos habla sobre la metadata.
- El comando `exiftool` nos muestra la metadata de algun archivo, por lo que sera de mucha ayuda.
- Al ejecutar el comando `exiftool` + la imagen dada, nos muestra sus metadatos, teniendo la flag en el apartado `artist`.

```bash()
picoCTF{s0_m3ta_d8944929}
```

## Notas adicionales
- Los metadatos, literalmente «sobre datos», son datos que describen otros datos. En general, un grupo de metadatos se refiere a un grupo de datos que describen el contenido informativo de un objeto al que se denomina recurso.

## Referencias 
- [Metadatos](https://es.wikipedia.org/wiki/Metadatos)