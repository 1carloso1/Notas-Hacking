## Descripción
I have these 2 images, can you make a flag out of them? [scrambled1.png](https://mercury.picoctf.net/static/e8054e22552c6aba591cdf7440eb25e4/scrambled1.png) [scrambled2.png](https://mercury.picoctf.net/static/e8054e22552c6aba591cdf7440eb25e4/scrambled2.png)

## Pistas
- [https://en.wikipedia.org/wiki/Visual_cryptography](https://en.wikipedia.org/wiki/Visual_cryptography)
- Think of different ways you can "stack" images

## Solución
- Segun el criptografia visual, al sobre poner una imagen sobre otra nos da un mensaje, por lo que el primer metodo que intente fue sobre poner una imagen arriba de otra utilizando photoshop, pero esto no dio ningun resultado.
- El metodo que procedi a utilizar es crear un código que combina las dos imágenes de la misma resolución pixel a pixel y crea una nueva imagen con los valores de los canales de color de los píxeles sumados y reducidos módulo 256. La explicación del codigo es la siguiente:
	1.  Importa la biblioteca PIL para permitir que el código manipule imágenes.
	2.  Abre dos imágenes con la función `Image.open()`: `scrambled1.png` y `scrambled2.png`.
	3.  Carga los píxeles de las dos imágenes usando el método `load()` y las asigna a las variables `pixels1` y `pixels2`.
	4.  Crea una nueva imagen `flag` del mismo tamaño que las dos imágenes originales, con el modo RGB.
	5.  Carga los píxeles de la nueva imagen usando el método `load()` y los asigna a la variable `flagpix`.
	6.  Recorre cada píxel de las dos imágenes originales usando dos bucles for anidados.
	7.  Suma los valores de los tres canales de colores (rojo, verde, azul) de los píxeles de las dos imágenes originales en cada posición `(col, row)` y se toma el resto de 256 para evitar que los valores excedan el rango de 0 a 255.
	8.  Asigna los valores de los canales de colores resultantes a los píxeles de la nueva imagen `flag` en la misma posición `(col, row)`.
	9.  Guarda la nueva imagen combinada en un archivo llamado `flag.png` utilizando el método `save()`.
- El codigo es:

```python()
from PIL import Image # pip install Pillow

img1 = Image.open("scrambled1.png")
pixels1 = img1.load()
img2 = Image.open("scrambled2.png")
pixels2 = img2.load()

flag = Image.new("RGB" ,img1.size)
flagpix = flag.load()

for row in range(img1.size[1]):
     for col in range(img1.size[0]):
           flagpix[col,row]=(
                        (pixels1[col,row][0]+pixels2[col,row][0])%256, #RED
                        (pixels1[col,row][1]+pixels2[col,row][1])%256, #GREEN
                        (pixels1[col,row][2]+pixels2[col,row][2])%256) #BLUE

flag.save("flag.png") #Se guarda una imagen con la flag
```

- La imagen tiene la siguiente flag: 

```bash()
picoCTF{d72ea4af}
```

## Notas adicionales
- La biblioteca PIL se utiliza para manipular imágenes y el código en sí mismo realiza las siguientes acciones

## Referencias 
- [Video de referencia](https://www.youtube.com/watch?v=e7Yx2nxGcqU)