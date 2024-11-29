## Descripción
A new modular challenge!Download the message [here](https://artifacts.picoctf.net/c/179/message.txt).Take each number mod 41 and find the modular inverse for the result. Then map to the following character set: 1-26 are the alphabet, 27-36 are the decimal digits, and 37 is an underscore.Wrap your decrypted message in the picoCTF flag format (i.e. `picoCTF{decrypted_message}`)

## Pistas
- Do you know what the modular inverse is?
- The inverse modulo _z_ of _x_ is the number, _y_ that when multiplied by _x_ is 1 modulo _z_
- It's recommended to use a tool to find the modular inverses

## Solución
- Segun la descripción, tenemos que seguir las siguientes reglas:



```
A: 1
B: 2
C: 3
D: 4
E: 5
F: 6
G: 7
H: 8
I: 9
J: 10
K: 11
L: 12
M: 13
N: 14
O: 15
P: 16
Q: 17
R: 18
S: 19
T: 20
U: 21
V: 22
W: 23
X: 24
Y: 25
Z: 26
0: 27
1: 28
2: 29
3: 30
4: 31
5: 32
6: 33
7: 34
8: 35
9: 36
_: 37
```

- Despues tenemos que encontrar el modulo 41 de un numero y luego tenga el modulo inverso de la siguiente cadena de numeros:

```
104 372 110 436 262 173 354 393 351 297 241 86 262 359 256 441 124 154 165 165 219 288 42 
```

- Para sacar el modulo inverso, utilice esta [herramienta](https://planetcalc.com/3311/), que nos da los siguientes resultados:

```
28 14 22 30 18 32 30 12 25 37 8 31 18 4 37 4 1 4 1 1 3 1 1
```

- Solo sustituimos los numeros por la lista que tenemos mas arriba, y obtenemos la flag: `1nv3r53ly_h4rd_dadaacaa`.

```
picoCTF{1nv3r53ly_h4rd_dadaacaa}
```


## Notas adicionales
- Sin notas adicionales

## Referencias
- Sin referencias