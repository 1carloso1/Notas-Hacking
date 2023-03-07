## Descripción
Can you get the flag?Run this [Python program](https://artifacts.picoctf.net/c/386/patchme.flag.py) in the same directory as this [encrypted flag](https://artifacts.picoctf.net/c/386/flag.txt.enc).

## Solución
- Para poder obtener la solución es necesario analizar bien el codigo fuente para saber en que parte se encuentra el codigo. Al hacerlo podemos encontrar lo siguiente:

```python()
def level_1_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    if( user_pw == "ak98" + \
                   "-=90" + \
                   "adfjhgj321" + \
                   "sleuth9000"):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), "utilitarian")
        print(decryption)
        return
    print("That password is incorrect")

```

- Podemos ver que un condicional compara si la contraseña ingresada es igual a la cadena dentro del condicional. Para ahorrarnos el paso de ver cual es la cadena del condicional, borramos la cadena y la remplazamos por cualquier digito, por lo que lo cambie por `"1"` paa hacerlo facil, despues de que compruebe esto, nos dara la flag.

```python()
def level_1_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    if( user_pw == "1"):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), "utilitarian")
        print(decryption)
        return
    print("That password is incorrect")
```

```bash()
picoCTF{p47ch1ng_l1f3_h4ck_c4a4688b}
```

## Notas adicionales
- El problema es muy sencillo, solo hay que tener una compresion basica de programación basica al momento de leer el codigo

## Referencias 