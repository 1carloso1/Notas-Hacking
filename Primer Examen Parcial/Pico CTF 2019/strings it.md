## Descripción
Can you find the flag in [file](https://jupiter.challenges.picoctf.org/static/fae9ac5267cd6e44124e559b901df177/strings) without running it?

## Solución
```bash()
┌──(kali㉿kali)-[~/Downloads]
└─$ strings strings | grep pico
picoCTF{5tRIng5_1T_7f766a23}
```

## Notas adicionales
Como no se podia ejecutar el archivo, busque otras alternativas, por lo que vi las pistas del reto y me mandaba a la documentacion del comando 'strings'. Por lo que intuitivamente se me ocurrio utilizar el comando con el archivo descargado. Asi que la primera vez que lo probe me salieron muchas lineas de texto, por lo que reduje los resultados utilizando el formato de la flag.
## Referencias 