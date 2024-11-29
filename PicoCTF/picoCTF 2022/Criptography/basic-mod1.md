## Descripción
We found this weird message being passed around on the servers, we think we have a working decryption scheme.Download the message [here](https://artifacts.picoctf.net/c/129/message.txt).Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore.Wrap your decrypted message in the picoCTF flag format (i.e. `picoCTF{decrypted_message}`)

## Pistas
- Do you know what `mod 37` means?
- `mod 37` means modulo 37. It gives the remainder of a number after being divided by 37.

## Solución
- Segun la descripción, tenemos que seguir las siguientes reglas:

```
A: 0
B: 1
C: 2
D: 3
E: 4
F: 5
G: 6
H: 7
I: 8
J: 9
K: 10
L: 11
M: 12
N: 13
O: 14
P: 15
Q: 16
R: 17
S: 18
T: 19
U: 20
V: 21
W: 22
X: 23
Y: 24
Z: 25
0: 26
1: 27
2: 28
3: 29
4: 30
5: 31
6: 32
7: 33
8: 34
9: 35
_: 36
```

- Despues tenemos que encontrar el modulo 37 de los siguinetes valores:

```
messaje = "350 63 353 198 114 369 346 184 202 322 94 235 114 110 185 188 225 212 366 374 261 213"
```

- Para obtener el modulo de manera facil, creé el siguiente programa en python:

```python()
messaje = "350 63 353 198 114 369 346 184 202 322 94 235 114 110 185 188 225 212 366 374 261 213"
lista_modulos = messaje.split(" ")

nuevos_modulos = []
for n in lista_modulos:
    n = int(n)
    n = n % 37
    nuevos_modulos.append(n)
lista_modulos = nuevos_modulos

print(lista_modulos)
```

- Lo que nos da como salida:}

```
[17, 26, 20, 13, 3, 36, 13, 36, 17, 26, 20, 13, 3, 36, 0, 3, 3, 27, 33, 4, 2, 28]
```

- Solo queda sustituir los numeros por los valores dados en la descripción, lo que nos da como resultado `R0UND_N_R0UND_ADD17EC2`

```
picoCTF{R0UND_N_R0UND_ADD17EC2}
```

## Notas adicionales
- Sin notas adicionales

## Referencias
- Sin referencias