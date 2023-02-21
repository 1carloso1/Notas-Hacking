## Objetivo
The password for the next level can be retrieved by submitting the password of the current level to **port 30000 on localhost**.

## Datos de acceso al nivel
-   Username: bandit14

-   Password: fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq

-   Host: bandit.labs.overthewire.org

-   Port: 2220

## Solución
```bash()
bandit14@bandit:~$ nc -v localhost 30000
Connection to localhost (127.0.0.1) 30000 port [tcp/*] succeeded!
fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq
Correct!
jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt
```

## Notas adicionales
Me pongo en conexion con el puerto dado en el localhost, donde le muestro la contraseña del nivel actual para que me mande la contraseña del siguiente
## Referencias 
