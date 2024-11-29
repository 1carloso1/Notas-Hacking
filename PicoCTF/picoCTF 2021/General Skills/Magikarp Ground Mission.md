## Descripción
Do you know how to move between directories and read files in the shell? Start the container, `ssh` to it, and then `ls` once connected to begin. Login via `ssh` as `ctf-player` with the password, `a13b7f9d`

Additional details will be available after launching your challenge instance.

## Solución
```bash()
┌──(kali㉿kali)-[~]
└─$ ssh ctf-player@venus.picoctf.net -p 60334
ctf-player@venus.picoctf.nets password: 
Welcome to Ubuntu 18.04.5 LTS (GNU/Linux 5.4.0-1041-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage
This system has been minimized by removing packages and content that are
not required on a system that users do not log into.

To restore this content, you can run the 'unminimize' command.
Last login: Sun Feb 26 00:03:45 2023 from 127.0.0.1
ctf-player@pico-chall$ ls
1of3.flag.txt  instructions-to-2of3.txt
ctf-player@pico-chall$ cat instructions-to-2of3.txt 
Next, go to the root of all things, more succinctly `/`
ctf-player@pico-chall$ pwd
/home/ctf-player/drop-in
ctf-player@pico-chall$ cat 1of3.flag.txt 
picoCTF{xxsh_
ctf-player@pico-chall$ cd ..
ctf-player@pico-chall$ ls
3of3.flag.txt  drop-in
ctf-player@pico-chall$ cat 3of3.flag.txt 
71be5264}
ctf-player@pico-chall$ pwd
/home/ctf-player
ctf-player@pico-chall$ cd /
ctf-player@pico-chall$ ls
2of3.flag.txt  boot  etc   instructions-to-3of3.txt  lib64  mnt  proc  run   srv  tmp  var
bin            dev   home  lib                       media  opt  root  sbin  sys  usr
ctf-player@pico-chall$ cat 2of3.flag.txt 
0ut_0f_\/\/4t3r_
ctf-player@pico-chall$ Connection to venus.picoctf.net closed by remote host.
Connection to venus.picoctf.net closed.

picoCTF{xxsh_0ut_0f_\/\/4t3r_71be5264}
```

## Notas adicionales
My facil de realizar.

## Referencias 