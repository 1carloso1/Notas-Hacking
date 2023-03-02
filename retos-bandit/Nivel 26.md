## Objetivo
Good job getting a shell! Now hurry and grab the password for bandit27!

## Datos de acceso al nivel
-   Username: bandit26

-   Password: c7GvcKlw9mC7aUQaPx7nwFstuAIBw1o1

-   Host: bandit.labs.overthewire.org

-   Port: 2220
## Solución
```bash()
 _                     _ _ _   ___   __
  _                     _ _ _   ___   __
 | |                   | (_) | |__ \ / /
 | |__   __ _ _ __   __| |_| |_   ) / /_
 | '_ \ / _` | '_ \ / _` | | __| / / '_ \
 | |_) | (_| | | | | (_| | | |_ / /| (_) |
 |_.__/ \__,_|_| |_|\__,_|_|\__|____\___/
~                                                                                                                                                     
~                                                                                                                                                     
~                                                                                                                                                                                                                                                                                                        
~                                                                                                                                                     
~                                                                                                                                                     
~                                                                                                                                                     
~                                                                                                                                                     
~                                                                                                                                                     
~   
:set shell=/bin/bash
:shell                                                                                                                    
bandit26@bandit:~$ ls
bandit27-do  text.txt
bandit26@bandit:~$ ./bandit27-do cat /etc/bandit_pass/bandit27
YnQpBuifNMas1hcUFk70ZmqkhUU2EuaS

```

## Notas adicionales
Para realizar este nivel, nos aprovecharemos de 'more', puse la ventana de un tamaño tan chico que me dio la opcion de more, estando ahi, pude entrar al editor VIM y pude visualizar completamente la ventana, pero como no mostraba la contraseña, utilice /bin/bash para poder "activar" la terminal para poder usarla y asi utilizar el binario que nos permite acceder a los archivos del nivel 27.

## Referencias 
- [Forma de resolver del maestro Carlos](https://ingsoftware.reduaz.mx/moodle/pluginfile.php/68464/mod_resource/content/2/06-retos-bandit-p3.pdf)
