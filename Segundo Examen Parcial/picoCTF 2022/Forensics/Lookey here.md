## Descripción
Attackers have hidden information in a very large mass of data in the past, maybe they are still doing it.Download the data [here](https://artifacts.picoctf.net/c/125/anthem.flag.txt).

## Pistas
- Download the file and search for the flag based on the known prefix.

## Solución
- Para resolver este reto, se nos da el archivo `anthem.flag.txt|. 
- Como es un archivo .txt, por intuición utilizo el comando `cat`.
- Al ver que es un texto comun, utilice el comando `grep` con la palabra clave `pico`. para ver si la flag esta en el archivo. Asi sucedio, la flag es:

```bash()
picoCTF{gr3p_15_@w3s0m3_58f5c024}
```

## Notas adicionales
- Es un reto muy facil sabiendo lo basico para analizar un .txt

## Referencias
- Sin referencias.