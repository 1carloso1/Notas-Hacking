## Objetivo
There is a git repository at `ssh://bandit29-git@localhost/home/bandit29-git/repo`. The password for the user `bandit29-git` is the same as for the user `bandit29`.

Clone the repository and find the password for the next level.

## Datos de acceso al nivel
-   Username: bandit29

-   Password: tQKvmcwNYcFS6vmPHIUSI3ShmsrQZK8S

-   Host: bandit.labs.overthewire.org

-   Port: 2220

## Solución
```bash()
bandit29@bandit:~$ mktemp -d
/tmp/tmp.xfE1tv2Qrc
bandit29@bandit:~$ cd /tmp/tmp.xfE1tv2Qrc
bandit29@bandit:/tmp/tmp.xfE1tv2Qrc$ git clone ssh://bandit29-git@localhost:2220/home/bandit29-git/repo
Cloning into 'repo'...
The authenticity of host '[localhost]:2220 ([127.0.0.1]:2220)' can't be established.
ED25519 key fingerprint is SHA256:C2ihUBV7ihnV1wUXRb4RrEcLfXC5CXlhmAAM/urerLY.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Could not create directory '/home/bandit29/.ssh' (Permission denied).
Failed to add the host to the list of known hosts (/home/bandit29/.ssh/known_hosts).
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

bandit29-git@localhost's password: 
remote: Enumerating objects: 16, done.
remote: Counting objects: 100% (16/16), done.
remote: Compressing objects: 100% (11/11), done.
remote: Total 16 (delta 2), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (16/16), done.
Resolving deltas: 100% (2/2), done.
bandit29@bandit:/tmp/tmp.xfE1tv2Qrc$ cd repo/
bandit29@bandit:/tmp/tmp.xfE1tv2Qrc/repo$ ls
README.md
bandit29@bandit:/tmp/tmp.xfE1tv2Qrc/repo$ cat README.md
# Bandit Notes
Some notes for bandit30 of bandit.

## credentials

- username: bandit30
- password: <no passwords in production!>

bandit29@bandit:/tmp/tmp.xfE1tv2Qrc/repo$ git log
commit 0afe3501277395fbfa017480925edee3df6e8bb5 (HEAD -> master, origin/master, origin/HEAD)
Author: Ben Dover <noone@overthewire.org>
Date:   Tue Feb 21 22:03:11 2023 +0000

    fix username

commit c2606dfc0aef7179bf1ccd6cffa9ed19151facb4
Author: Ben Dover <noone@overthewire.org>
Date:   Tue Feb 21 22:03:11 2023 +0000

    initial commit of README.md
bandit29@bandit:/tmp/tmp.xfE1tv2Qrc/repo$ git diff 0afe3501277395fbfa017480925edee3df6e8bb5 c2606dfc0aef7179bf1ccd6cffa9ed19151facb4
diff --git a/README.md b/README.md
index 1af21d3..2da2f39 100644
--- a/README.md
+++ b/README.md
@@ -3,6 +3,6 @@ Some notes for bandit30 of bandit.
 
 ## credentials
 
-- username: bandit30
+- username: bandit29
 - password: <no passwords in production!>
 
bandit29@bandit:/tmp/tmp.xfE1tv2Qrc/repo$ git branch
* master
bandit29@bandit:/tmp/tmp.xfE1tv2Qrc/repo$ git branch -a
* master
  remotes/origin/HEAD -> origin/master
  remotes/origin/dev
  remotes/origin/master
  remotes/origin/sploits-dev
bandit29@bandit:/tmp/tmp.xfE1tv2Qrc/repo$ git checkout remotes/origin/dev
Note: switching to 'remotes/origin/dev'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at fbbce0e add data needed for development
bandit29@bandit:/tmp/tmp.xfE1tv2Qrc/repo$ git branch
* (HEAD detached at origin/dev)
  master
bandit29@bandit:/tmp/tmp.xfE1tv2Qrc/repo$ git log
commit fbbce0ec6c80acb0fdc00ebb4b5228dd868fd799 (HEAD, origin/dev)
Author: Morla Porla <morla@overthewire.org>
Date:   Tue Feb 21 22:03:11 2023 +0000

    add data needed for development

commit 925c929e0527f14c189b3d617d2bcc60f019f567
Author: Ben Dover <noone@overthewire.org>
Date:   Tue Feb 21 22:03:11 2023 +0000

    add gif2ascii

commit 0afe3501277395fbfa017480925edee3df6e8bb5 (origin/master, origin/HEAD, master)
Author: Ben Dover <noone@overthewire.org>
Date:   Tue Feb 21 22:03:11 2023 +0000

    fix username

commit c2606dfc0aef7179bf1ccd6cffa9ed19151facb4
Author: Ben Dover <noone@overthewire.org>
Date:   Tue Feb 21 22:03:11 2023 +0000

    initial commit of README.md
bandit29@bandit:/tmp/tmp.xfE1tv2Qrc/repo$ git show fbbce0ec6c80acb0fdc00ebb4b5228dd868fd799
commit fbbce0ec6c80acb0fdc00ebb4b5228dd868fd799 (HEAD, origin/dev)
Author: Morla Porla <morla@overthewire.org>
Date:   Tue Feb 21 22:03:11 2023 +0000

    add data needed for development

diff --git a/README.md b/README.md
index 1af21d3..a4b1cf1 100644
--- a/README.md
+++ b/README.md
@@ -4,5 +4,5 @@ Some notes for bandit30 of bandit.
 ## credentials
 
 - username: bandit30
-- password: <no passwords in production!>
+- password: xbhV3HpNGlTIdnjUrdAlPzc2L6y9EOnS

```

## Notas adicionales
Al entrar al repositorio encontramos el archivo `README.md` que no tenia nada importante, e igual que con el nivel anterior, intente ver los commit anteriores para ver si encontraba algo, pero no habia commits. Por lo que con el comando `git branch` vi la rama en la que me encontraba para luego utilizar `git branch -a` para ver las demas ramas del repositorio. Encontre interesante la rama `remotes/origin/dev`, por lo que con el comando `git checkout`, estando dentro de la rama, vi los commits anteriores, donde encontre el nombre de uno interesante 'add data needed for development', por lo que entre ahi y pude encontrar la flag.

## Referencias 
-   [https://git-scm.com/doc](https://git-scm.com/doc)