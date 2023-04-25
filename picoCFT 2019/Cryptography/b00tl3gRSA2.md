
## Descripción
In RSA d is a lot bigger than e, why don't we use d to encrypt instead of e? Connect with `nc jupiter.challenges.picoctf.org 57464`.

## Pistas
- What is e generally?

## Solución
- Para resolver este reto, utilizaremos la formula para desencriptar un texto plano en el algoritmo de RSA `m = c^d mod n / pow(c, d, n)`. Y coimo nos sugiere la pista, usaremos la variable de `e` en lugar de despejar la de `d`. A continuación muestro el programa realizado en python para obtener la respuesta:

```python()
from gmpy2 import iroot
from Crypto.Util.number import long_to_bytes

e = 65537
c = 51805591590047156747485835844273608068590015401543479648551692485432833033993144525496875170923042701019145341253607785338864620499864572765054905868662420052105673961977892979926257615474919581948724432916120418548182033422704510131254717288903944356133040000115575192739012300016903615074591511195017839349
n = 157730223633018751118472114865485422854496553704947256745937296764879184982686087739229680197918806188078065679829521655844028517287799379465284586465676510322981915045485568642003597858961902725893643010913023734722493981646831266305859920467737529295570460656260532261147696677203081351446178984983391212331

m = pow(c,e,n)
print(long_to_bytes(m))
```

```bash()
picoCTF{bad_1d3a5_2152720}
```

## Notas adicionales
- La `e` generalmente vale 65537.

- c - texto cifrado
- m - mensaje de texto plano
- p - primo 1
- q - primo 2
- n - modulo (llave publica) 
- tn - totient n (euler)
- e - exponente (llave publica) 
- d - llave privada

- n = p * q
- tn = (p-1) * (q-1)
- d = e mod inv tn / inverse(e, tn)
- Encriptar, c = m^e mod n / pow(m, e, n)
- Desencriptar, m = c^d mod n / pow(c, d, n)
## Referencias 
- [RSA info](https://simple.wikipedia.org/wiki/RSA_algorithm)