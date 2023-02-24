## Objetivo
The password for the next level is stored in a file **readme** in the homedirectory. Unfortunately, someone has modified **.bashrc** to log you out when you log in with SSH.

## Datos de acceso al nivel
-   Username: bandit18

-   Password: hga5tuuCLF6fFzUpnagiMN8ssu9LFrdg

-   Host: bandit.labs.overthewire.org

-   Port: 2220

## Solución
```bash()
┌──(kali㉿kali)-[~]
└─$ ssh bandit18@bandit.labs.overthewire.org -p 2220 /bin/bash
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

bandit18@bandit.labs.overthewire.org's password: 
ls
readme
cat readme
awhqfNnAbc1naukrpqDYcF95h7HoMTrC
```

## Notas adicionales
En este nivel, la shell esta modoficada, por lo que tendre que utilizarla desde /bin/bash. Es la razón por la cual este nivel se ve diferente

## Referencias 
