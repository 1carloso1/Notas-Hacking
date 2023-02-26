## Descripción
Can you crack the password to get the flag?Download the password checker [here](https://artifacts.picoctf.net/c/81/level5.py) and you'll need the encrypted [flag](https://artifacts.picoctf.net/c/81/level5.flag.txt.enc) and the [hash](https://artifacts.picoctf.net/c/81/level5.hash.bin) in the same directory too. Here's a [dictionary](https://artifacts.picoctf.net/c/81/dictionary.txt) with all possible passwords based on the password conventions we've seen so far.

## Solución
```bash()
eee0. The password is correct
Welcome back... your flag, user:
picoCTF{h45h_sl1ng1ng_fffcda23}
```

## Notas adicionales
Para poder obtener la contraseña, modifique el metodo <b>level_5_pw_check()</b> del programa, ya que este metodo es el que comprobaba la contraseña y dependiendo de si era correcta o no te daba la flag. Un archivo que se proporciono contiene miles de lineas , por lo que seria impsoible probar una por una. Con la funcion open().read(), hice que se leyera el archvio, y con un split() se guardara cada contraseña en una posicion de una lista, por lo que he creando un ciclo for que recorriera y comprobara una por una hasta allar la correcta.

Original:

```python()
def level_5_pw_check():

    user_pw = input("Please enter correct password for flag: ")

    user_pw_hash = hash_pw(user_pw)

    if( user_pw_hash == correct_pw_hash ):

        print("Welcome back... your flag, user:")

        decryption = str_xor(flag_enc.decode(), user_pw)

        print(decryption)

        return

    print("That password is incorrect")
```

Modificado:

```python()
diccionario = open("dictionary.txt","r").read()

lista_psswd = diccionario.split()


def level_5_pw_check():

    for psswd in lista_psswd:

        user_pw = psswd

        user_pw_hash = hash_pw(user_pw)

        if( user_pw_hash == correct_pw_hash ):

            print(f"{psswd}. The password is correct")

            print("Welcome back... your flag, user:")

            decryption = str_xor(flag_enc.decode(), user_pw)

            print(decryption)

            return
```

## Referencias 