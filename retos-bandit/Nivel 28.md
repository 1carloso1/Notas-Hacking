## Objetivo
There is a git repository at `ssh://bandit28-git@localhost/home/bandit28-git/repo`. The password for the user `bandit28-git` is the same as for the user `bandit28`.

Clone the repository and find the password for the next level.

## Datos de acceso al nivel
-   Username: bandit28

-   Password: AVanL161y9rsbcJIsFHuw35rjaOM19nR

-   Host: bandit.labs.overthewire.org

-   Port: 2220

## Solución
```bash()
bandit28@bandit:~$ mktemp -d
/tmp/tmp.0mEssc7Dz1
bandit28@bandit:~$ cd /tmp/tmp.0mEssc7Dz1
bandit28@bandit:/tmp/tmp.0mEssc7Dz1$ git clone ssh://bandit28-git@localhost/home/bandit28-git/repo
Cloning into 'repo'...
The authenticity of host 'localhost (127.0.0.1)' can't be established.
ED25519 key fingerprint is SHA256:C2ihUBV7ihnV1wUXRb4RrEcLfXC5CXlhmAAM/urerLY.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Could not create directory '/home/bandit28/.ssh' (Permission denied).
Failed to add the host to the list of known hosts (/home/bandit28/.ssh/known_hosts).

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

!!! You are trying to log into this SSH server on port 22, which is not intended.

bandit28-git@localhost: Permission denied (publickey).
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
bandit28@bandit:/tmp/tmp.0mEssc7Dz1$ git clone ssh://bandit28-git@localhost:2220/home/bandit28-git/repo
Cloning into 'repo'...
The authenticity of host '[localhost]:2220 ([127.0.0.1]:2220)' can't be established.
ED25519 key fingerprint is SHA256:C2ihUBV7ihnV1wUXRb4RrEcLfXC5CXlhmAAM/urerLY.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Could not create directory '/home/bandit28/.ssh' (Permission denied).
Failed to add the host to the list of known hosts (/home/bandit28/.ssh/known_hosts).
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

bandit28-git@localhosts password: 
remote: Enumerating objects: 9, done.
remote: Counting objects: 100% (9/9), done.
remote: Compressing objects: 100% (6/6), done.
remote: Total 9 (delta 2), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (9/9), done.
Resolving deltas: 100% (2/2), done.
bandit28@bandit:/tmp/tmp.0mEssc7Dz1$ ls
repo
bandit28@bandit:/tmp/tmp.0mEssc7Dz1$ cd repo/
bandit28@bandit:/tmp/tmp.0mEssc7Dz1/repo$ ls
README.md
bandit28@bandit:/tmp/tmp.0mEssc7Dz1/repo$ cat README.md
# Bandit Notes
Some notes for level29 of bandit.

## credentials

- username: bandit29
- password: xxxxxxxxxx

bandit28@bandit:/tmp/tmp.0mEssc7Dz1/repo$ git log
commit 104db85a904e9691ff22aafe1a96124c88f75afa (HEAD -> master, origin/master, origin/HEAD)
Author: Morla Porla <morla@overthewire.org>
Date:   Tue Feb 21 22:03:10 2023 +0000

    fix info leak

commit 6c3c5e485cc531e5d52c321587ce1103833ab7c3
Author: Morla Porla <morla@overthewire.org>
Date:   Tue Feb 21 22:03:10 2023 +0000

    add missing data

commit cd3b97ef95879ec34df0d6c82f2a96d552f0e56c
Author: Ben Dover <noone@overthewire.org>
Date:   Tue Feb 21 22:03:10 2023 +0000

    initial commit of README.md
bandit28@bandit:/tmp/tmp.0mEssc7Dz1/repo$ git diff 104db85a904e9691ff22aafe1a96124c88f75afa 6c3c5e485cc531e5d52c321587ce1103833ab7c3
diff --git a/README.md b/README.md
index 5c6457b..b302105 100644
--- a/README.md
+++ b/README.md
@@ -4,5 +4,5 @@ Some notes for level29 of bandit.
 ## credentials
 
 - username: bandit29
-- password: xxxxxxxxxx
+- password: tQKvmcwNYcFS6vmPHIUSI3ShmsrQZK8S
```

## Notas adicionales
Para poder hacer este nivel vimos que en el README.md no encontramos nada util, aunque nos daba indicios de que la contraseña debia estar ahi. Por lo que con git log vimos los diferentes commits que se han hecho, y ya viendolos, con git diff comparamos el commit actual con el anterior que decia 'add missing data' que es lo que nos interesa.
- <b>git log</b>: muestra los logs de cuando se ejecuta un `commit`
- <b>git diff</b>: os indica los cambios entre `commits`

## Referencias 
-   [https://git-scm.com/doc](https://git-scm.com/doc)