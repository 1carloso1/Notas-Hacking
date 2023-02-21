## Objetivo
The password for the next level is stored in the file **data.txt**, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions

## Datos de acceso al nivel
-   Username: bandit11

-   Password: 6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM

-   Host: bandit.labs.overthewire.org

-   Port: 2220

## Solución
```bash()
bandit11@bandit:~$ ls
data.txt
bandit11@bandit:~$ cat data.txt 
Gur cnffjbeq vf WIAOOSFzMjXXBC0KoSKBbJ8puQm5lIEi
bandit11@bandit:~$ cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
The password is JVNBBFSmZwKKOP0XbFXOoW8chDz5yVRv

```

## Notas adicionales
La flag fue ocultada, las palabras fueron rotadas 13 veces, es decir, la letra original fue cambiada por la letra que esta 13 lugares despues (rot13)
<b>tr</b>: se utiliza para traducir/transformar datos de una forma a otra
## Referencias 
[Referencia de medium](https://david-varghese.medium.com/overthewire-bandit-level-11-level-12-df6e59deda05)
