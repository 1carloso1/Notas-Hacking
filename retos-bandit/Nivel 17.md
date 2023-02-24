## Objetivo
There are 2 files in the homedirectory: **passwords.old and passwords.new**. The password for the next level is in **passwords.new** and is the only line that has been changed between **passwords.old and passwords.new**


**NOTE: if you have solved this level and see ‘Byebye!’ when trying to log into bandit18, this is related to the next level, bandit19**

## Datos de acceso al nivel
-   Username: bandit17

-   Password: VwOSWtCA7lRKkTfbr2IDh6awj9RNZM5e

-   Host: bandit.labs.overthewire.org

-   Port: 2220

## Solución
```bash()
bandit17@bandit:~$ ls
passwords.new  passwords.old
bandit17@bandit:~$  diff passwords.old passwords.new
42c42
< f9wS9ZUDvZoo3PooHgYuuWdawDFvGld2
---
> hga5tuuCLF6fFzUpnagiMN8ssu9LFrdg

```

## Notas adicionales
El comando `diff` en Linux es una herramienta de línea de comandos que se utiliza para comparar dos archivos y mostrar las diferencias entre ellos. El comando `diff` puede comparar dos archivos y mostrar las diferencias entre ellos línea por línea o en bloques de texto. Esto puede ser útil para encontrar cambios en un archivo, verificar la integridad de los datos y fusionar cambios de archivos.


El comando `diff` es muy útil en las siguientes situaciones:


1.  Comprobar si dos archivos son iguales: Si tiene dos archivos y desea saber si son idénticos o no, puede usar el comando `diff` para comparar los dos archivos. Si no hay ninguna diferencia, el comando no devuelve ninguna salida.


2.  Encontrar diferencias entre dos versiones de un archivo: Si tiene dos versiones diferentes de un archivo, puede usar el comando `diff` para compararlas y mostrar las diferencias entre ellas. Esto puede ser útil para identificar los cambios que se han realizado en un archivo desde la última vez que se revisó.

## Referencias 
[Página de manual de diff](https://linux.die.net/man/1/diff)