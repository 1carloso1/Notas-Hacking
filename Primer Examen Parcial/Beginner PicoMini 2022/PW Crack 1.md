## Descripción
Can you crack the password to get the flag? Download the password checker here and you'll need the encrypted flag in the same directory too.

## Solución
```bash()
┌──(kali㉿kali)-[~/Downloads]
└─$ emacs level1.py

┌──(kali㉿kali)-[~/Downloads]
└─$ python3 level1.py
Please enter correct password for flag: 8713
Welcome back... your flag, user:
picoCTF{545h_r1ng1ng_1b2fd683}
```

## Notas adicionales
Para resolver este reto, analice la fuente del codigo, encontrando que la contraseña que pide el mismo programa estaba ahi. Por lo que fue demasiado facil obtener la flag.

```python()
if( user_pw == "8713"):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
```

## Referencias 
