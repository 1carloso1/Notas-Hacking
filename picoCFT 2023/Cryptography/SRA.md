## Descripción
I just recently learnt about the SRA public key cryptosystem... or wait, was it supposed to be RSA? Hmmm, I should probably check...Connect to the program on our server: `nc saturn.picoctf.net 59952` Download the program: [chal.py](https://artifacts.picoctf.net/c/299/chal.py)

## Pistas
- (None)

## Solución
-La secuencia de comandos a continuación lo hará sin problemas y es importante recordar ingresar el número de puerto para su instancia.

```python()
from sage.all import *
from pwn import *
from gmpy2 import is_prime
from string import ascii_letters, digits
from Crypto.Util.number import bytes_to_long, long_to_bytes, inverse

r = remote('saturn.picoctf.net', 59952)

def is_printable(text):
    alphabet = ascii_letters + digits
    for i in text:
        if i not in alphabet:
            return False
    return True

e = 65537
r.recvuntil(b'anger = ')
c = int(r.recvline().strip().decode())
r.recvuntil(b'envy = ')
d = int(r.recvline().strip().decode())
r.recvline()
print(c)
print(d)

K = divisors(d*e - 1)
print("Done")

list_prime = []
for k in K:
    pp = ((d*e - 1)//k) + 1

    if is_prime(pp) and int(pp).bit_length() == 128:
        list_prime.append(pp)

list_text = []
for p in list_prime:
    for q in list_prime:
        try:
            if inverse(e, (p - 1) * (q - 1)) == d:
                n = p*q
                list_text.append(long_to_bytes(int(pow(c, d, n))))
        except:
            pass


list_text = set(list_text)

for text in list_text:
    try:
        text = text.decode()
        if is_printable(text):
            print(text)
            r.recvuntil(b'> ')
            r.sendline(text.encode())
            print(r.recvline())
            print(r.recvline())
            print(r.recvline())
            break
    except:
        continue
r.close()
```

- Lo que nos da como salida y flag:

```
picoCTF{7h053_51n5_4r3_n0_m0r3_3858bd66}
```

## Notas adicionales
- Para correr el programa se necesita instalar:

```
sudo apt install sagemath
sage-python -m pip install pwn
sage-python -m pip install pycryptodome
```

## Referencias 
- https://dev.to/brunoblaise/sra-picoctf-2023-278b
