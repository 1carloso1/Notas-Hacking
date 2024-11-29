
## Descripción
This is a really weird text file TXT? Can you find the flag?

## Pistas
- How do operating systems know what kind of file it is? (It's not just the ending!
- Make sure to submit the flag as picoCTF{XXXXX}

## Solución
- Para resolver el reto las pistas son importantes, ya que nos habla de las extensiones de un archivo.
- Como el archivo dado es `.txt` lo primero que hice fue usar el comando `cat`, pero al mostrar carácteres extraños pase a usar el comando `strings` pero siguio sin dar algun resultado.
- Gracias a las pistas, me dio curiosidad ver los metadatos del archivo para ver si en realidad es un archivo `.txt`, pero los datos decian que era un archivo `.png`, por lo que con el comando `mv` le cambie el nombre de la extensión.
- Ya estando el archivo corregido, procedi a abrir la imagen y encontrar ahi la flag:

```bash()
picoCTF{now_you_know_about_extensions}
```

## Notas adicionales
- En informática, el término extensión del fichero es una cadena de caracteres anexada al nombre de un archivo, habitualmente predicha por un punto. Su función principal es distinguir el contenido del archivo, de modo que el sistema operativo disponga del procedimiento necesario para ejecutarlo o interpretarlo.

## Referencias 
- [Extensión de archivo](https://es.wikipedia.org/wiki/Extensi%C3%B3n_de_archivo)
