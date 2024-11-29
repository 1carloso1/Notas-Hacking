## Descripción
Decrypt this message.

## Pistas
- caesar cipher tutorial

## Solución
- Para resolver este reto, la pista nos da mucha informacion, ya que nos habla de `caesar cipher`.
- El texto que se nos da es  `picoCTF{gvswwmrkxlivyfmgsrhnrisegl} `
- Por lo que si lo hacemos a mano, podria ser muy exhausto, por lo que lo haremos con [Caesar Cipher Decoder](https://www.dcode.fr/caesar-cipher)
- Si ponemos solo los caracteres que no se pueden leer, el decodificador nos dara `crossingtherubicondjneoach`, lo que suena logico al leerlo, por lo que la flag es:

```bash()
picoCTF{crossingtherubicondjneoach}
```

## Notas adicionales
- El cifrado César, también conocido como cifrado por desplazamiento, es una de las formas más antiguas y sencillas de cifrar un mensaje.
- Es un tipo de cifrado de sustitución en el que cada letra del mensaje original (que en criptografía se llama texto sin formato) se reemplaza con una letra correspondiente a un cierto número de letras desplazadas hacia arriba o hacia abajo en el alfabeto.

## Referencias 
- [Caesar Cipher](https://privacycanada.net/classical-encryption/caesar-cipher/)