## Objetivo
The password for the next level is stored in a file called **spaces in this filename** located in the home directory

## Datos de acceso al nivel
**bandit.labs.overthewire.org**  

**bandit2**  

rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi

## Solución
```bash()
bandit2@bandit:~$ ls
spaces in this filename
bandit2@bandit:~$ cat "spaces in this filename"
aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG
bandit2@bandit:~$ 

```

## Notas adicionales
Cuando el nombre de un archivo tiene espacios en el nombre, hay que escribirlo entre " " ya que es una cadena de texto, si se escribe sin eso, la consola reconocera cada palabra como individuales.

## Referencias 

