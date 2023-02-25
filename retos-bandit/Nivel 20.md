## Objetivo
There is a setuid binary in the homedirectory that does the following: it makes a connection to localhost on the port you specify as a commandline argument. It then reads a line of text from the connection and compares it to the password in the previous level (bandit20). If the password is correct, it will transmit the password for the next level (bandit21).

## Datos de acceso al nivel
-   Username: bandit20

-   Password: VxCazJaVykI6W36BkBU0mJTCM8rR95XT

-   Host: bandit.labs.overthewire.org

-   Port: 2220

## Solución
```bash()
bandit20@bandit:~$ ls
suconnect
bandit20@bandit:~$ ./suconnect 
Usage: ./suconnect <portnumber>
This program will connect to the given port on localhost using TCP. If it receives the correct password from the other side, the next password is transmitted back.
bandit20@bandit:~$ nc -lnvp 6666 <<< VxCazJaVykI6W36BkBU0mJTCM8rR95XT &
[5] 3129871
bandit20@bandit:~$ Listening on 0.0.0.0 6666

bandit20@bandit:~$ ./suconnect 6666
Connection received on 127.0.0.1 50528
Read: VxCazJaVykI6W36BkBU0mJTCM8rR95XT
Password matches, sending next password
NvEJF7oVjkddltPSrdKEFOllh9V1IBcq
```

## Notas adicionales
Suconnect es el binario que se utilizo para producir una reverse shell que pudimos interceptar con netcat.
En Netcat, el símbolo "&" se utiliza para ejecutar comandos en segundo plano. Cuando se utiliza "&" al final de un comando en la línea de comandos de Netcat, el comando se ejecuta en segundo plano, lo que significa que Netcat continuará ejecutándose y aceptando entradas de usuario mientras el comando se ejecuta en segundo plano. Un ejemplo de esto es cuando inciamos el listener, pudimos ejecutar en segundo plano el binario dado para obtener la contraseña siguiente

## Referencias 
[](https://linuxize.com/post/how-to-run-linux-commands-in-background/)