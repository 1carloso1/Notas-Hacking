## Descripción
Decode this [message](https://jupiter.challenges.picoctf.org/static/fc1edf07742e98a480c6aff7d2546107/message.wav) from the moon.

## Pistas
- How did pictures from the moon landing get sent back to Earth?
- What is the CMU mascot?, that might help select a RX option

## Solución
- No se puede identificar nada significativo al escuchar el archivo. Además, visualizar el archivo no conducía a ninguna parte. La pista sugiere que esto está relacionado con la forma en que las imágenes del alunizaje se transmitieron a la Tierra. Algunas investigaciones conducen a SSTV:

`La televisión de exploración lenta (SSTV) es un método de transmisión de imágenes utilizado principalmente por radioaficionados para transmitir y recibir imágenes estáticas por radio en monocromo o en color. Las cámaras de televisión del Apolo utilizaron SSTV para transmitir imágenes desde el interior del Apolo 7, el Apolo 8 y el Apolo 9, así como la televisión del Módulo Lunar del Apolo 11 desde la Luna.`

- Este [tutorial](https://ourcodeworld.com/articles/read/956/how-to-convert-decode-a-slow-scan-television-transmissions-sstv-audio-file-to-images-using-qsstv-in-ubuntu-18-04) explica cómo usar un programa llamado qsstv para convertir los archivos de audio a imágenes.
- La pista preguntaba "¿Cuál es la mascota de CMU?" - la respuesta es "Scotty the Scottie Dog". Esto insinuó que deberíamos seleccionar "Scottie 1" como "Modo" de QSSTV. También tuve que seleccionar "Auto Slant" a través de prueba y error.

- En este punto, podemos hacer clic en el botón "Reproducir" en QSSTV para iniciar el receptor y luego reproducir el archivo de audio:

```bash()
└─$ paplay -d virtual-cable message.wav  
```

- La imagen es recibida y decodificada por el programa:

![[Pasted image 20230319104035.png]]


```bash()
picoCTF{beep_boop_im_in_space}
```

## Notas adicionales
- Para poder realizar el reto, hay que seguir el [tutorial](https://ourcodeworld.com/articles/read/956/how-to-convert-decode-a-slow-scan-television-transmissions-sstv-audio-file-to-images-using-qsstv-in-ubuntu-18-04) para configurar la herramienta
- Una vez finalizada la transmisión, podemos limpiar usando los siguientes comandos:

```bash()
root@kali:/media/sf_CTFs/pico# pactl list short modules | grep null
22      module-null-sink        sink_name=virtual-cable
root@kali:/media/sf_CTFs/pico# pactl unload-module 22
```

## Referencias 
- [github.com/Dvd848/](https://github.com/Dvd848/CTFs/blob/master/2019_picoCTF/m00nwalk.md)
- [How to convert (decode) a Slow-Scan Television transmissions (SSTV) audio file to images using QSSTV in Ubuntu 18.04](https://ourcodeworld.com/articles/read/956/how-to-convert-decode-a-slow-scan-television-transmissions-sstv-audio-file-to-images-using-qsstv-in-ubuntu-18-04)