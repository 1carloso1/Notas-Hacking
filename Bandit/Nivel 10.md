## Objetivo
The password for the next level is stored in the file **data.txt**, which contains base64 encoded data

## Datos de acceso al nivel
-   Username: bandit10

-   Password: G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s

-   Host: bandit.labs.overthewire.org

-   Port: 2220

## Solución
```bash()
bandit10@bandit:~$ ls
data.txt
bandit10@bandit:~$ cat data.txt | base64 -d
The password is 6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM
bandit10@bandit:~$ 

```

## Notas adicionales
<b>Base64</b>: codificar o decodificar ARCHIVO, o entrada estándar, a salida estándar.
<b>-d, --decode</b>:  decodifica los datos


## Referencias 
[Documentación base64](https://www.gnu.org/software/coreutils/base64)
