## Descripción
There is something on my shop network running at `nc mercury.picoctf.net 53740`, but I can't tell what it is. Can you?

## Solución
- Para poder obtener la flag de este problema, ejecutamos el comando dado en la descripción, el cual nos abrira un archivo con codigo en `G-code`.
- Pero, ¿Cómo deduje que el archivo estaba en este lenguaje?. Leyendo la pista `What language does a CNC machine use?`, pude encontrar muy facilmente la respueta en google.
- Entonces sabiendo esto, busque un interpretador para GC, por lo que encontre [ncviewer.com](https://ncviewer.com/).
- Poniendo los datos que recibimos, nos da como resultado una grafica en 3D donde podemos visualizar la flag.

```bash()
picoCTF{num3r1cal_c0ntr0l_775375c7}
```

## Notas adicionales


## Referencias 
- [What is G-code?](https://www.mastercam.com/news/blog/what-coding-language-is-used-on-cnc-machines/#:~:text=G%2Dcode%2C%20simply%20put%2C,G%3A%20machine%20motion)