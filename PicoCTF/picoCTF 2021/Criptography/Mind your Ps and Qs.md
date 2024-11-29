## Descripción
In RSA, a small `e` value can be problematic, but what about `N`? Can you decrypt this? [values](https://mercury.picoctf.net/static/2604f8b51a5cc62d38a3736938f19cef/values)

## Pistas
- Bits are expensive, I used only a little bit over 100 to save money

## Solución
- Del archvio, obtenemos los sihuinetes valores:

```
Decrypt my super sick RSA:
c: 861270243527190895777142537838333832920579264010533029282104230006461420086153423
n: 1311097532562595991877980619849724606784164430105441327897358800116889057763413423
e: 65537 
```

- Para poder obtener el texto plano, necesitamos de las variables `p` y `q`, para asi poder obtener `tn` y despues `d` y poder sustituirlos en las formula que nos da el texto plano: `m = c^d mod n`
- Para poder obtener estas variables, utilizaremos [Factordb](http://factordb.com/). Los valores que nos da son:

```
p = 1955175890537890492055221842734816092141
q = 670577792467509699665091201633524389157003
p * q = n
```

- Sabiendo esto, podemos sustituir los valores para obtener el valor de `tn` y `d` y asi sustituir todas estas variables en la formula para obtener el texto plano. Para eso cree un programa en python que nos diera la bandera sabiendo todo esto.

```python()
from Crypto.Util.number import inverse, long_to_bytes

c = 861270243527190895777142537838333832920579264010533029282104230006461420086153423
n = 1311097532562595991877980619849724606784164430105441327897358800116889057763413423
e = 65537

p = 1955175890537890492055221842734816092141
q = 670577792467509699665091201633524389157003
tn = (p-1) * (q-1)
d = inverse(e, tn)
m = pow(c, d, n)
print(long_to_bytes(m))
```

- La salida es:

```
picoCTF{sma11_N_n0_g0od_13686679}
```

## Notas adicionales
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
- Sin referencias