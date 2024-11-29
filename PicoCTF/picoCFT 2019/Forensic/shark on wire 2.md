## Descripción
We found this packet capture. Recover the flag that was pilfered from the network.

## Pistas
- (None)

## Solución
- Para resolver este reto, tenemos que analizarel contenido de paquetes, al analizar paquete por paquete, vemos que en la ip 10.0.0.66 a traves del protoclo `UDP` hay dos archivos muy curiosos, uno donde dice `start` y despues de algunos paquetes hay otro mas que dice `end`.
- Por lo que a traves de la barra de busqueda iremos a los paquetes que ha enviado la ip `10.0.0.66` digitando `ip.addr ==10.0.0.66`.
- Estando en los paquetes filtrados, podemos ver que entre los paquetes que dicen `start` y  `end` hay paquetes que en su información pareciera que fueran numeros decimales que podrian seguir un orden si los traducimos a ASCII, por lo que recopile esa lista de numeros para ver si transformandolos a ASCII podria darnos la bandera.

```bash()
112 105 99 111 67 84 70 123 112 49 76 76 102 51 114 51 100 95 100 97 116 97 95 118 49 97 95 115 116 51 103 48 125
```

- Lo que transformandolo a ASCII si nos da la flag: 

```bash()
picoCTF{p1LLf3r3d_data_v1a_st3g0}
```

## Notas adicionales
- Con [rapidtables.com](https://www.rapidtables.com/convert/number/ascii-hex-bin-dec-converter.html) logre la conversión de decimal a ASCII.

## Referencias 