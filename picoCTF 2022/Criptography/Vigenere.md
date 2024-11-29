## Descripción
Can you decrypt this message?Decrypt this [message](https://artifacts.picoctf.net/c/159/cipher.txt) using this key "CYLAB".

## Pistas
- https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher

## Solución
- Como dice el titulo, este reto se trata de `Encripción Vigenere`. Por lo que usando el decodificador online [dcode](https://www.dcode.fr/vigenere-cipher) pude desencriptar facilmente el mensaje utilizando la clave proporcionada.

```bash()
picoCTF{D0NT_US3_V1G3N3R3_C1PH3R_d85729g7}
```

## Notas adicionales
- El cifrado Vigenère es un algoritmo de cifrado polialfabético inventado por el criptólogo francés Blaise de Vigenère en el siglo XVI. Se basa en un cifrado de turno al que se le agrega el uso de una palabra clave que cambia el turno en cada paso.

## Referencias 
- https://www.dcode.fr/vigenere-cipher