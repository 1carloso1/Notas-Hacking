## Descripción
Download the packet capture file and use packet analysis software to find the flag.
- Download packet capture

## Pistas
- Wireshark, if you can install and use it, is probably the most beginner friendly packet analysis software product.

## Solución
- Como nos dice la pista, para resolver este reto necesitaremos utilizar `Wireshark` para poder analizar el archivo de paquetes de red.
- Al estar dentro del software, vemos solo 5 paquetes, por lo que sera facil encontrar la flag.
- Al darle click derecho a un paquete TCP, le damos en `follow` -> `TCP stream`, donde podremos ver la flag:

```
p i c o C T F { p 4 c k 3 7 _ 5 h 4 r k _ b 9 d 5 3 7 6 5 }
```

- Al utilizar un codigo en python para eliminar los espacios sin tener que hacerlo manual, podemos obtener la flag sin espacios.

```shell()
└─$ python3            
Python 3.11.2 (main, Feb 12 2023, 00:48:52) [GCC 12.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> c = "p i c o C T F { p 4 c k 3 7 _ 5 h 4 r k _ b 9 d 5 3 7 6 5 }"
>>> c = c.replace(' ', '')
>>> print(c)
picoCTF{p4ck37_5h4rk_b9d53765}
>>> exit()
```

- La flag es: 

```bash()
picoCTF{p4ck37_5h4rk_b9d53765}
```

## Notas adicionales
- Un reto muy sencillo.

## Referencias
- Sin referencias.