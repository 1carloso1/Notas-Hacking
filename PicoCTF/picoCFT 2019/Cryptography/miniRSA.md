## Descripción
Let's decrypt this: [ciphertext](https://jupiter.challenges.picoctf.org/static/eb5e6df8e14c52873cf88c582a1a4008/ciphertext)? Something seems a bit small.

## Pistas
- RSA [tutorial](https://en.wikipedia.org/wiki/RSA_(cryptosystem))
- How could having too small an e affect the security of this 2048 bit key?
- Make sure you don't lose precision, the numbers are pretty big (besides the e value)
- 
## Solución
- Debido a que no se tienen las variables necesarias para desencriptar el texto plano, se podria decir que este reto no tiene solución, pero como nos indica la pista; si "e" es demasiado pequeño, puede haber problemas de seguridad al desencriptar el texto cifrado. Un atacante podría calcular fácilmente la clave privada a partir de la clave pública y la variable "e" pequeña.
- Entonces en la formula para obtener el texto plano `c^d mod n / pow(c, d, n)`, se modifica a  `m = c^(1/e)`
- El codigo en python seria el siguiente:

```python()
from gmpy2 import iroot

from Crypto.Util.number import long_to_bytes

n = 29331922499794985782735976045591164936683059380558950386560160105740343201513369939006307531165922708949619162698623675349030430859547825708994708321803705309459438099340427770580064400911431856656901982789948285309956111848686906152664473350940486507451771223435835260168971210087470894448460745593956840586530527915802541450092946574694809584880896601317519794442862977471129319781313161842056501715040555964011899589002863730868679527184420789010551475067862907739054966183120621407246398518098981106431219207697870293412176440482900183550467375190239898455201170831410460483829448603477361305838743852756938687673

e = 3

c = 2205316413931134031074603746928247799030155221252519872650080519263755075355825243327515211479747536697517688468095325517209911688684309894900992899707504087647575997847717180766377832435022794675332132906451858990782325436498952049751141

m = int(iroot(c,e)[0])

print(long_to_bytes(m))
```

- La flag seria:

```bash()
b'picoCTF{n33d_a_lArg3r_e_d0cd6eae}'
```

## Notas adicionales
-  "iroot" es una función que calcula la raíz "e"-ésima de un número "c" y devuelve una tupla con dos elementos. El primer elemento es el resultado de la operación, es decir, la raíz "e"-ésima de "c". El segundo elemento es un valor booleano que indica si el resultado es exacto o aproximado.
	-   En este caso, se toma el primer elemento de la tupla devuelta por "iroot", que es el resultado de la raíz "e"-ésima de "c".
	-   Se utiliza la función "int" para convertir este resultado en un número entero.
	-   El resultado se asigna a la variable "m".

## Referencias 
- [función iroot](https://docs.sympy.org/latest/modules/mpmath/functions/roots.html#mpmath.iroot)