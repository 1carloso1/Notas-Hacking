## Descripción
To get truly 1337, you must understand different data encodings, such as hexadecimal or binary. Can you get the flag from this program to prove you are on the way to becoming 1337? Connect with `nc jupiter.challenges.picoctf.org 29956`.

## Solución
```bash()
(kali㉿kali)-[~]
└─$ nc jupiter.challenges.picoctf.org 29956
Let us see how data is stored
animation
Please give the 01100001 01101110 01101001 01101101 01100001 01110100 01101001 01101111 01101110 as a word.
...
you have 45 seconds.....

Input:
animation
Please give me the  154 151 155 145 as a word.
Input:
lime
Please give me the 616e696d6174696f6e as a word.
Input:
animation
Youve beaten the challenge
Flag: picoCTF{learning_about_converting_values_b375bb16}

```

```bash()
┌──(kali㉿kali)-[~/Desktop]
└─$ python3 based.py
Ingrese la cadena binaria: 01100001 01101110 01101001 01101101 01100001 01110100 01101001 01101111 01101110
word: animation

Ingrese la cadena octal: 154 151 155 145
word: lime

Ingrese la cadena hexadecimal: 616e696d6174696f6e
word: animation

```

## Notas adicionales
Como pedia rapido la decodificacion de las cadenas dadas, <b>invente</b> un programa en python que decodificara en los diferentes tipos de base solicitados las cadenas de texto.
El codigo se llama <b>based.py</b> y se encuentra en la carpeta "codigos".

## Referencias