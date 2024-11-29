## Descripción
Can you get the flag?Reverse engineer this [Python program](https://artifacts.picoctf.net/c/464/unpackme.flag.py).

## Solución
- Para poder realizar este reto es necesario checar a detalle el codigo fuente, ya que sabiendo de que manera esta codificada la flag, podemos aplicar la ingenieria reversa para poder obtener la solución.
- Para poder desencriptar una cadena de texto con la libreria Fernet es necesario tener una llave unica. Como se ve en el codigo, dicha llave se codifica en base 64.

```python()
key_str = 'correctstaplecorrectstaplecorrec'
key_base64 = base64.b64encode(key_str.encode)
```

- Despues podemos ver que en la variable f, se podria decir que se guarda la "Confirmación de que la contraseña es correcta".

```python()
f = Fernet(key_base64)
```

- Despues, se procede a desencriptar el payload dado y se guarda en la variable plain, por lo que agregaremos una linea nueva que imprima esta variable y obtendremos la flag.

```python()
plain = f.decrypt(payload)
print(plain)
```

```bash()
picoCTF{175_chr157m45_5274ff21}
```

## Notas adicionales


## Referencias 
[# Fernet (symmetric encryption) using Cryptography module in Python](https://www.geeksforgeeks.org/fernet-symmetric-encryption-using-cryptography-module-in-python/)