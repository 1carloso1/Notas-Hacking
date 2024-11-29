## Objetivo
To gain access to the next level, you should use the setuid binary in the homedirectory. Execute it without arguments to find out how to use it. The password for this level can be found in the usual place (/etc/bandit_pass), after you have used the setuid binary.

## Datos de acceso al nivel
-   Username: bandit19

-   Password: awhqfNnAbc1naukrpqDYcF95h7HoMTrC

-   Host: bandit.labs.overthewire.org

-   Port: 2220

## Solución
```bash()
bandit19@bandit:~$ ls
bandit20-do
bandit19@bandit:~$ ./bandit20-do 
Run a command as another user.
  Example: ./bandit20-do id
bandit19@bandit:~$ ./bandit20-do cat /etc/bandit_pass/bandit20
VxCazJaVykI6W36BkBU0mJTCM8rR95XT

```

## Notas adicionales
El binario dado en este nivel nos funciono de tal manera que al ejecutarlo simulamos ser el nivel 20, y poder acceder a su información.

## Referencias 
