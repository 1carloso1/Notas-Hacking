
## Objetivo
The password for the next level is stored in a hidden file in the **inhere** directory.

## Datos de acceso al nivel
**bandit.labs.overthewire.org**
**bandit3**
aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG

## Solución
```bash()
bandit3@bandit:~$ pwd
/home/bandit3
bandit3@bandit:~$ ls
inhere
bandit3@bandit:~$ cd inhere/
bandit3@bandit:~/inhere$ ls
bandit3@bandit:~/inhere$ cd ..
bandit3@bandit:~$ cat inhere/.hidden 
2EW7BBsr6aMMoJ2HjW067dm8EgX26xNe
```

## Notas adicionales
Como no se encontro un archivo a simple vista dentro de la carpeta inhere/, intente ver si aparecia un archivo al escribir la ruta

## Referencias 