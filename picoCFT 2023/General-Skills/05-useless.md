## Descripción:
There's an interesting script in the user's home directoryThe work computer is running SSH. We've been given a script which performs some basic calculations, explore the script and find a flag.

```
Hostname: saturn.picoctf.net
Port:     56481
Username: picoplayer
Password: password
```

**Hints:**

## Solución:
1. nos conectamos por ssh al host:

```bash
┌──(kali㉿kali)-[~]
└─$ ssh -p 56481 picoplayer@saturn.picoctf.net
The authenticity of host '[saturn.picoctf.net]:56481 ([13.59.203.175]:56481)' can't be established.
ED25519 key fingerprint is SHA256:ves7M6DhshpiJSsScBWo3n34oOFTUXvLZqPyqLWeTHk.
This host key is known by the following other names/addresses:
    ~/.ssh/known_hosts:10: [hashed name]
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[saturn.picoctf.net]:56481' (ED25519) to the list of known hosts.
picoplayer@saturn.picoctf.net's password: 
Welcome to Ubuntu 20.04.6 LTS (GNU/Linux 5.15.0-1031-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

picoplayer@challenge:~$ 
```

2. Vemos que tenemos un script de bash el cual al ejecutarlo recibe tres parámetros los cuales son tres números, el script realiza la suma de los tres números y nos muestrea el mensaje `Read the manual` el cual nos indica que leamos el manual del script, al leer dicho manual encontramos la flag:    

```bash
picoplayer@challenge:~$ ls
useless
picoplayer@challenge:~$ ls -l
total 4
-rwxr-xr-x 1 root root 517 Mar 16 01:30 useless
picoplayer@challenge:~$ ./useless 
Read the code first
picoplayer@challenge:~$ cat useless 
#!/bin/bash
# Basic mathematical operations via command-line arguments

if [ $# != 3 ]
then
  echo "Read the code first"
else
        if [[ "$1" == "add" ]]
        then 
          sum=$(( $2 + $3 ))
          echo "The Sum is: $sum"  

        elif [[ "$1" == "sub" ]]
        then 
          sub=$(( $2 - $3 ))
          echo "The Substract is: $sub" 

        elif [[ "$1" == "div" ]]
        then 
          div=$(( $2 / $3 ))
          echo "The quotient is: $div" 

        elif [[ "$1" == "mul" ]]
        then
          mul=$(( $2 * $3 ))
          echo "The product is: $mul" 

        else
          echo "Read the manual"
         
        fi
fi
picoplayer@challenge:~$ ./useless 10 20 5
Read the manual
picoplayer@challenge:~$ ls
useless
picoplayer@challenge:~$ man useless 

useless
     useless, — This is a simple calculator script

SYNOPSIS
     useless, [add sub mul div] number1 number2

DESCRIPTION
     Use the useless, macro to make simple calulations like addition,subtraction, multiplication and division.

Examples
     ./useless add 1 2
       This will add 1 and 2 and return 3

     ./useless mul 2 3
       This will return 6 as a product of 2 and 3

     ./useless div 6 3
       This will return 2 as a quotient of 6 and 3

     ./useless sub 6 5
       This will return 1 as a remainder of substraction of 5 from 6

Authors
     This script was designed and developed by Cylab Africa

     picoCTF{us3l3ss_ch4ll3ng3_3xpl0it3d_4373}

picoplayer@challenge:~$
```

### Flag: picoCTF{us3l3ss_ch4ll3ng3_3xpl0it3d_4373}

## Notas adicionales:

## Referencias:
