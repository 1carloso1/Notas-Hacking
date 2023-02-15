## Objetivo
The password for the next level is stored in the file **data.txt** in one of the few human-readable strings, preceded by several ‘=’ characters.

## Datos de acceso al nivel
**bandit.labs.overthewire.org**
**bandit9**
EN632PlfYiZbn3PhVK3XOGSlNInNE00t

## Solución
```bash()
bandit9@bandit:~$ ls
data.txt
bandit9@bandit:~$ strings data.txt | grep ===
c========== the
h;========== password
========== isT
n.E========== G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s
bandit9@bandit:~$ 

```

## Notas adicionales
<b>strings: </b>Imprime las cadenas de caracteres imprimibles en archivos

## Referencias 
[Información sobre el comando 'strings'](https://www.educba.com/linux-string-command/)
