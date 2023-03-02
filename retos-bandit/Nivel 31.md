## Objetivo
There is a git repository at ssh://bandit31-git@localhost/home/bandit31-git/repo. The password for the user bandit31-git is the same as for the user bandit31.

## Datos de acceso al nivel
-   Username: bandit31

-   Password: OoffzGDlzhAlerFJ2cAiz1D41JW1Mhmt

-   Host: bandit.labs.overthewire.org

-   Port: 2220

## Solución
```bash()
bandit31@bandit:/tmp/tmp.Xu97xjd6x1/repo$ ls
README.md

bandit31@bandit:/tmp/tmp.Xu97xjd6x1/repo$ cat README.md 
This time your task is to push a file to the remote repository.

Details:
    File name: key.txt
    Content: 'May I come in?'
    Branch: master

bandit31@bandit:/tmp/tmp.Xu97xjd6x1/repo$ git branch
* master

bandit31@bandit:/tmp/tmp.Xu97xjd6x1/repo$ echo 'May I come in?' > key.txt
bandit31@bandit:/tmp/tmp.Xu97xjd6x1/repo$ ls
key.txt  README.md
bandit31@bandit:/tmp/tmp.Xu97xjd6x1/repo$ cat key.txt 
May I come in?

bandit31@bandit:/tmp/tmp.Xu97xjd6x1/repo$ git add key.txt
The following paths are ignored by one of your .gitignore files:
key.txt
hint: Use -f if you really want to add them.
hint: Turn this message off by running
hint: "git config advice.addIgnoredFile false"
bandit31@bandit:/tmp/tmp.Xu97xjd6x1/repo$ git add -f key.txt
bandit31@bandit:/tmp/tmp.Xu97xjd6x1/repo$ git commit -m "update key.txt file"
[master fedf826] update key.txt file
 1 file changed, 1 insertion(+)
 create mode 100644 key.txt
bandit31@bandit:/tmp/tmp.Xu97xjd6x1/repo$ git push
The authenticity of host '[localhost]:2220 ([127.0.0.1]:2220)' can't be established.
ED25519 key fingerprint is SHA256:C2ihUBV7ihnV1wUXRb4RrEcLfXC5CXlhmAAM/urerLY.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Could not create directory '/home/bandit31/.ssh' (Permission denied).
Failed to add the host to the list of known hosts (/home/bandit31/.ssh/known_hosts).
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

bandit31-git@localhost's password: 
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 2 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 330 bytes | 330.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
remote: ### Attempting to validate files... ####
remote: 
remote: .oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.
remote: 
remote: Well done! Here is the password for the next level:
remote: rmCBvG56y58BXzv98yZGdO7ATVL5dW8y 
remote: 
remote: .oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.
remote: 
To ssh://localhost:2220/home/bandit31-git/repo
 ! [remote rejected] master -> master (pre-receive hook declined)
error: failed to push some refs to 'ssh://localhost:2220/home/bandit31-git/repo'

```

## Notas adicionales
Para poder completar este nivel, vemos que al leer el `README.md` nos dice que ahora es turno de hacer un push de un archivo  `key.txt` con el contenido May I come in? en la rama master. 

Como se puede observar en la solución, no tenemos problema en añadir el archivo, pero al hacer el commit nos sale

`The following paths are ignored by one of your .gitignore files: key.txt`
`hint: Use -f if you really want to add them.` 

Por lo que procedemos a reescribir el codigo. Esto es causa de que debemos forzarlo con la opción `-f`, debido que en `.gitignore` se están ignorando los archivos TXT.
Al hacer el push, nos muestra la contraseña hacia el siguiente nivel.

## Referencias 
 - [https://git-scm.com/doc](https://git-scm.com/doc)