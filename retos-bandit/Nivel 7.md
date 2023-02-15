## Objetivo
The password for the next level is stored in the file **data.txt** next to the word **millionth**

## Datos de acceso al nivel
**bandit.labs.overthewire.org**  

**bandit7**  

z7WtoNQU2XfjmMtWA8u5rN4vzqu4v99S

## Solución
```bash()
bandit7@bandit:~$ ls
data.txt
bandit7@bandit:~$ cat data.txt | grep millionth
millionth       TESKZC0XvTetK0S9xNwm25STk5iWrBvP

```

## Notas adicionales
El comando <b>grep</b> me ayuda a buscar palabras clave dentro de un texto
|: me ayuda a poner varios comandos en una sola linea de texto

## Referencias 