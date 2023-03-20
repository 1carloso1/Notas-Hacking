## Descripción
I stopped using YellowPages and moved onto WhitePages... but the page they gave me is all blank!

## Pistas
- (None)

## Solución
- Para resolver este reto, se necesita abrir el archivo en un editor de  texto, ya que el archivo no esta totalmente en blanco, esta lleno de espacios  y luego se separan, los que podriamos representar como 1 y 0 en terminos binarios.
- Teniendo esto en mente, podemos escribir un codigo en python que reemplace estos espacios por una cadena de numeros binarios que podremos traducir a carácteres ASCII.
- El codigo en python es el siguiente:

```python()
#Podemos representar los espacios con 1 y 0 para asi poder encontrar el mensaje

text = '                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                '

  

firstType = ' '

binaryString = ''
for char in text: #Foreach char
    if char == firstType: #Check if it is the first type
        binaryString += '0' #Mark it as 0
    else:
        binaryString += '1' #Mark it as 1
print(binaryString) #Print result
```

- Lo que nos da como salida:

```bash()
00001010000010010000100101110000011010010110001101101111010000110101010001000110000010100000101000001001000010010101001101000101010001010010000001010000010101010100001001001100010010010100001100100000010100100100010101000011010011110101001001000100010100110010000000100110001000000100001001000001010000110100101101000111010100100100111101010101010011100100010000100000010100100100010101010000010011110101001001010100000010100000100100001001001101010011000000110000001100000010000001000110011011110111001001100010011001010111001100100000010000010111011001100101001011000010000001010000011010010111010001110100011100110110001001110101011100100110011101101000001011000010000001010000010000010010000000110001001101010011001000110001001100110000101000001001000010010111000001101001011000110110111101000011010101000100011001111011011011100110111101110100010111110110000101101100011011000101111101110011011100000110000101100011011001010111001101011111011000010111001001100101010111110110001101110010011001010110000101110100011001010110010001011111011001010111000101110101011000010110110001011111001101110011000100110000001100000011100000110110001100000110001000110000011001100110000100110111001101110011100101100001001101010110001001100100001110000110001101100101001100100011100101100110001100100011010001100110001101010011100000110110011001000110001101111101000010100000100100001001
```

- Utlizando [rapidtables.com](https://www.rapidtables.com/convert/number/ascii-hex-bin-dec-converter.html) podremos encontrar el mensaje traducido a ASCII:

```bash()
picoCTF{not_all_spaces_are_created_equal_7100860b0fa779a5bd8ce29f24f586dc}
```

## Notas adicionales
- El sistema binario, también llamado sistema diádico​ en ciencias de la computación, es un sistema de numeración en el que los números son representados utilizando únicamente dos cifras: 0 y 1

## Referencias 
- [Sistema binario](https://es.wikipedia.org/wiki/Sistema_binario)