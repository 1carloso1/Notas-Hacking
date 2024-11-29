## Descripción
Can you find the flag? shark1.pcapng.

## Pistas
- (None)

## Solución
- Para resolver este reto, se nos da un archivo de paquetes de red, y como dice el nombre del reto, utilizaremos `Wireshark`.
- Para empezar, analizaremos los diferentes streams de los paquetes TCP, ya que en general, ahi encontramos la flag.
- Al llegar al stream 5, encontramos la flag codificada en ROT13

```bash()
Gur synt vf cvpbPGS{c33xno00_1_f33_h_qrnqorrs}
```

- Despues de decodificarlo con [Cyberchef](https://gchq.github.io/CyberChef/#recipe=ROT13(true,true,false,13)&input=R3VyIHN5bnQgdmYgY3ZwYlBHU3tjMzN4bm8wMF8xX2YzM19oX3FybnFvcnJzfQ), encontramos que la flag es:

```bash()
picoCTF{p33kab00_1_s33_u_deadbeef}
```

## Notas adicionales
- Solo hay que ser pacientes y atentos al buscar entre los streams.

## Referencias
- Sin referencias.