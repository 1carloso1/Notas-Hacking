## Objetivo
The password for the next level is stored **somewhere on the server** and has all of the following properties:
-   owned by user bandit7
-   owned by group bandit6
-   33 bytes in size

## Datos de acceso al nivel
**bandit.labs.overthewire.org**
**bandit4**
P4L4vucdmLnm8I7Vl7jG1ApGSfjYKqJU

## Solución
```bash()
bandit6@bandit:~$ ls
bandit6@bandit:~$ find /  -user bandit7 -group bandit6 -size 33c 2>/dev/null
/var/lib/dpkg/info/bandit7.password
bandit6@bandit:~$ cat /var/lib/dpkg/info/bandit7.password
z7WtoNQU2XfjmMtWA8u5rN4vzqu4v99S
```

## Notas adicionales
**2>/dev/null** elimina los mensaje de "Permiso denegado"
El comando <b>find</b> nos ayuda a buscar cualquier archivo, donde se pueden especificar propiedades especificas, como:
<b>/</b>: El diagonal se utiliza por que buscamos la ruta donde se encuentra el archivo, ya que no tenemos mas información
<b>-user</b>: El usuario al que pertenece
<b>-group</b>: el grupo al que pertenece
<b>-size</b>: especifica el tamaño del archivo

## Referencias 
[información mas detallada sobre el nivel](https://medium.com/@theGirlWhoEncrypts/overthewire-bandit-level-6-level-7-e1930ac68a54)