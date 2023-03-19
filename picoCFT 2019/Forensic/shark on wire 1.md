
## Descripción
We found this packet capture. Recover the flag.

## Pistas
- Try using a tool like Wireshark
- What are streams?

## Solución
- Para obtener la solución a este reto, necesitamos abrir el archivo desde `wireshark`, donde encontraremos una captura de peticiones.
- Para obtener la respuesta, analizamos una por una el codigo hexadecimal transformado a ASCII en las peticiones para ver si encontrabamos algo interesante. 
- Despues de un rato, vimos que en el protocolo UDP aparcia constantemete "pico" por lo que lo filtre ene l buscador.
- Despues de analizar una por una en las peticiones filtradas, se empieza a ver que la flag esta descompuesta en caracacteres, donde todos estaban destinados a una sola direccion ip.
- Por lo que dandole click derecho a una de esas peticiones e ir a `follow - UDP streams`, me mostro la flag completa.

```bash()
picoCTF{StaT31355_636f6e6e}
```

## Notas adicionales
- Seguir un flujo de protocolo aplica un filtro de visualización que selecciona todos los paquetes en el flujo actual. Algunas personas abren el cuadro de diálogo "Seguir transmisión TCP" e inmediatamente lo cierran como una forma rápida de aislar una transmisión en particular. Cerrar el cuadro de diálogo con el botón "Atrás" restablecerá el filtro de visualización si no se desea este comportamiento.

## Referencias 
- [Following Protocol Streams](https://www.wireshark.org/docs/wsug_html_chunked/ChAdvFollowStreamSection)