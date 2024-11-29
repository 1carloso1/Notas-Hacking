## Objetivo
After all this git stuff its time for another escape. Good luck!

## Datos de acceso al nivel
-   Username: bandit32

-   Password: rmCBvG56y58BXzv98yZGdO7ATVL5dW8y

-   Host: bandit.labs.overthewire.org

-   Port: 2220

## Solución
```bash()
WELCOME TO THE UPPERCASE SHELL
>> $0
$ pwd
/home/bandit32
$ ls
uppershell
$ whoami           
bandit33
$ cat /etc/bandit_pass/bandit33
odHo63fHiFqcWWJG9rLiLDtPm45KzUKy
$ 

```

## Notas adicionales
- Como dice el nombre de la shell, todo lo que se escribe en la linea de comandos lo transforma en mayusculas.
- Para poder ingresar a la shell es necesario ingresar `$0`. Esto es debido gracias a el parámetro posicional. `Los parámetros posicionales son nombrados numéricamente a partir de 1 hasta N, donde N es el último argumento enviado al script. También existe el parámetro posicional 0, cuyo valor es el nombre del script invocado( o en defecto, la manera en que se invocó).`.
- estando en la shell, vemos que usuario somos, como somos el usuario `Bandit33`, buscamos la contraseña en los archivos del usuario.


## Referencias 
- -   [https://hablemoslinux.wordpress.com/2012/07/02/los-parametros-posicionales-en-un-shell-script/](https://hablemoslinux.wordpress.com/2012/07/02/los-parametros-posicionales-en-un-shell-script/)