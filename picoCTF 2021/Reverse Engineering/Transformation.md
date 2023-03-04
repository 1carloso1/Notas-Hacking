
## Descripción
I wonder what this really is... enc ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

## Solución
- Para poder resolver este reto, es ver el contenido del documento para ver de que manera se puede encontrar la FLAG.
```bash()
└─$ cat enc      
灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彤㔲挶戹㍽
```

- En un traductor no encontraras la respuesta, asi que probaremos en python si los simbolos del archivo estan de alguna manera codificados.
```bash()
└─$ python3          
Python 3.10.9 (main, Dec  7 2022, 13:47:07) [GCC 12.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> enc=open("enc").read()
>>> print(enc)
灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彤㔲挶戹㍽
>>> print(hex(ord(enc[0])))
0x7069
```

- Vemos que el primer simbolo del archivo tiene un valor en hexadecimal, por lo que decodificaremos toda la cadena para tratar de decodificarla a ASCII.
```bash()
>>> for i in enc:
...     print(hex(ord(i)).lstrip("0x"),end='')
... 
7069636f4354467b31365f626974735f696e73743334645f6f665f385f64353263366239337d>>>
```

- Utilizaremos [apidtables](https://www.rapidtables.com/convert/number/hex-to-ascii.html) para decodificar la cadena ASCII. Lo que nos dara la bandera:
```bash()
picoCTF{16_bits_inst34d_of_8_d52c6b93}
```

## Notas adicionales
- `ord()` es una función incorporada en Python 3, para convertir la cadena que representa un carácter Unicode en un entero que representa el código Unicode del carácter.
- El `end=''`sirve para que el for imprima todo en una sola linea.
- `lstrip()` en Python se utiliza para cortar espacios o una cadena de caracteres especificada a la izquierda.

## Referencias 
[# Guía de funciones de Python](https://www.freecodecamp.org/espanol/news/guia-de-funciones-de-python-con-ejemplos/#:~:text=ord()%20es%20una%20funci%C3%B3n,el%20c%C3%B3digo%20Unicode%20del%20car%C3%A1cter.)
[# lstrip Python método ()](http://www.w3big.com/es/python/att-string-lstrip.html#gsc.tab=0)