## Descripción
Can you crack the password to get the flag? Download the password checker here and you'll need the encrypted flag in the same directory too.

## Solución
```bash()
┌──(kali㉿kali)-[~/Downloads]
└─$ emacs level2.py

┌──(kali㉿kali)-[~/Downloads]
└─$ python3
Python 3.10.9 (main, Dec  7 2022, 13:47:07) [GCC 12.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> print(chr(0x64) + chr(0x65) + chr(0x37) + chr(0x36))
de76
>>> exit()                                                            

┌──(kali㉿kali)-[~/Downloads]
└─$ python3 level2.py 
Please enter correct password for flag: de76
Welcome back... your flag, user:
picoCTF{tr45h_51ng1ng_489dea9a}
```

## Notas adicionales
Para resolver este reto, analice la fuente del codigo, encontrando que la contraseña que pide el mismo programa estaba ahi, pero de manera "encriptada", ya que solo mostraba la posicion del simbolo en la tablas ASCII. 

```python()
if( user_pw == chr(0x64) + chr(0x65) + chr(0x37) + chr(0x36)):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
```

## Referencias 
