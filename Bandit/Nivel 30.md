## Objetivo
There is a git repository at ssh://bandit30-git@localhost/home/bandit30-git/repo. The password for the user bandit30-git is the same as for the user bandit30.

## Datos de acceso al nivel
-   Username: bandit30

-   Password: xbhV3HpNGlTIdnjUrdAlPzc2L6y9EOnS

-   Host: bandit.labs.overthewire.org

-   Port: 2220

## Solución
```bash()
bandit30@bandit:/tmp/tmp.X0b44vxUoy$ cd repo/

bandit30@bandit:/tmp/tmp.X0b44vxUoy/repo$ ls
README.md
bandit30@bandit:/tmp/tmp.X0b44vxUoy/repo$ cat README.md 
just an epmty file... muahaha

bandit30@bandit:/tmp/tmp.X0b44vxUoy/repo$ git log
commit cf552c166d78421e64ddf52f850e680075d216e1 (HEAD -> master, origin/master, origin/HEAD)
Author: Ben Dover <noone@overthewire.org>
Date:   Tue Feb 21 22:03:13 2023 +0000
    initial commit of README.md
    
bandit30@bandit:/tmp/tmp.X0b44vxUoy/repo$ git branch
* master
bandit30@bandit:/tmp/tmp.X0b44vxUoy/repo$ git branch -a
* master
  remotes/origin/HEAD -> origin/master
  remotes/origin/master
  
bandit30@bandit:/tmp/tmp.X0b44vxUoy/repo$ git show-ref
cf552c166d78421e64ddf52f850e680075d216e1 refs/heads/master
cf552c166d78421e64ddf52f850e680075d216e1 refs/remotes/origin/HEAD
cf552c166d78421e64ddf52f850e680075d216e1 refs/remotes/origin/master
831aac2e2341f009e40e46392a4f5dd318483019 refs/tags/secret
bandit30@bandit:/tmp/tmp.X0b44vxUoy/repo$ git show 831aac2e2341f009e40e46392a4f5dd318483019
OoffzGDlzhAlerFJ2cAiz1D41JW1Mhmt

```

## Notas adicionales
Como se puede ver en la solución, al no encontrar nada en archvio `README.md`, procedí a ver los commits. Como no se habia hecho ningun commit anteriormente,  verifique las ramas del repositorio, de las cuales solo existe la rama `origin/master. Por lo que solo pude recorrer a utilizar el comando git show-ref. Este comando lo que hace es ver las referencias de las ramas ocucultas. Dichas ramas se ocultan con el comando git stash, obteniendo como resultado ls rama ocula y su referencia.
`

## Referencias 
-   [https://git-scm.com/doc](https://git-scm.com/doc)