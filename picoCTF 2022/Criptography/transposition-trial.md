## Descripción
Our data got corrupted on the way here. Luckily, nothing got replaced, but every block of 3 got scrambled around! The first word seems to be three letters long, maybe you can use that to recover the rest of the message.Download the corrupted message [here](https://artifacts.picoctf.net/c/192/message.txt).

## Pistas
- Split the message up into blocks of 3 and see how the first block is scrambled

## Solución
- Para resolver el reto, se nos da la siguinete cadena de texto: `heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V091B0AE}2`.
- Como nos dice la descripcion, en un grupo de 3 caracteres (incluyendo el espacio), se pondra el ultimo char al principio y se recorreran los primeros dos un espacio. Lo explico de la siguiente forma:

```python()
c0 = "heTfl g as iicpCTo" #Texto original
c1 = "heT|fl |g a|s i|icp|CTo" #Lo dividimos en grupos
c2= "The| fl|ag |is |pic|oCT" #Se cambia el orden
```

- Para cambiarlo de una manera facil, cree el siguinete programa en python:

```python()
c = "`heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V091B0AE}2"
cList = list(c)
nList = []
nc = ""
for i, char in enumerate(cList):
    if ((i + 1) % 3 == 0):
        nList.append(cList[i])
        nList.append(cList[i-2])
        nList.append(cList[i-1])
        
for char in nList:
    nc += char

print(nc)
```

- Lo que nos da como salida:

```bash()
The flag is picoCTF{7R4N5P051N6_15_3XP3N51V3_109AB02E}
```

## Notas adicionales
- No recordaba como recorrer los valores char en un arreglo, pero con este reto refresque mi memoria.

## Referencias
- Sin referencias. 