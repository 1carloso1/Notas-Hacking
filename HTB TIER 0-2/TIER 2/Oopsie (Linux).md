# Oopsie (Linux)

# Solución

- Se encontro el puerto 80 abierto con el servicio http corriendo.
- Se introdujo en el navegador la ip de la maquina objetivo
    
    ![Untitled](../../images/Untitled%2014.png)
    
- Como no se encontro ninguna funcionalidad en la pagina, se procedio a ver el codigo de la pagina con “CTRL+U”, donde se encontro un enlace oculto

![Untitled](../../images/Untitled%201%201.png)

- Se procedio a ingresar a ese enlace, donde nos encontramos con lo siguiente:
- Como no pudimos hacer nada con sql inyection, ingresamos como invitados

![Untitled](../../images/Untitled%202%201.png)

- Como podemos ver, no podemos acceder a algunas funcionalidades por falta de permisos

![Untitled](../../images/Untitled%203%201.png)

- Encontramos una vulnerabilidad en el apartado “Account”, ya que nos muestra la info de el usuario logueado, y como se ve en la url, el invitado tiene el id=2

![Untitled](../../images/Untitled%204%201.png)

- Por lo que si cambiamos el id, nos muestra la información del administrador

![Untitled](../../images/Untitled%205%201.png)

- Por lo que si inspeccionamos la pagina, y nos vamos a “storage”, podemos ver nuestra informacion como usuarios.

![Untitled](../../images/Untitled%206%201.png)

- Por lo que podemos elevar nuestros permisos con la informacion previamente encontrada

![Untitled](../../images/Untitled%207%201.png)

- como se puede apreciar, ya podemos subir archivos, ya que somos administradores ahora, por lo que podemos aprovechar esto como una vulnerabilidad. Podemos hacer un PHP reverse shell subiendo un archivo que nos permita hacer esta funcionalidad.

![Untitled](../../images/Untitled%208%201.png)

- Existe un archivo en kali llamado “php-reverse-shell.php”, por lo que podemos editarlo (poner nuestra ip y el puerto que queremos) para hacerlo funcional y poderlo subir a la pagina.

![Untitled](../../images/Untitled%209%201.png)

- Antes de subirlo a la plataforma necesitamos saber a donde se van los archivos subidos, para poder ejecutar nuestro reverse shell, por lo que con gobuster encontramos dicha pagina.

![Untitled](../../images/Untitled%2010%201.png)

- Sabiendo a donde se va a enviar, procedemos a crear un listener en el puerto que definimos en el archivo.

![Untitled](../../images/Untitled%2011%201.png)

- Ya teniendo todo listo, procedemos a subir el archivo

![Untitled](../../images/Untitled%2012%201.png)

- Ya subido el archivo, estamos listos para ejectuarlo, esto sera desde el path en la url encontrada + el nombre del archivo subido. Lo que nos dara como resultado la conexión con el listener

![Untitled](../../images/Untitled%2013%201.png)

- Ahora necesitamos mejorar nuetra shell, ya que en este momento no podemos hacer mucho, por lo que se escribio el siguiente comando para mejorarla: **“python3 -c 'import pty; pty.spawn("/bin/bash")’”**

![Untitled](../../images/Untitled%2014%201.png)

- Como ahora tenemos privilegios, necesitamos saber que usuarios existen para poder empezar a buscar informacion, ingresando a las contraseñas. COmo se puede observar, encontramos a un usuario llamado “Robert”

![Untitled](../../images/Untitled%2015.png)

- Por lo que accederemos a el e intentaremos encontrar algo interesante. Como se puede ver, encontramos la flag de usuario, pero aun necesitamos informacion para acceder al administrador

![Untitled](../../images/Untitled%2016.png)

- Como se puede ver, encontramos la información de usuario de robert

![Untitled](../../images/Untitled%2017.png)

- Teniendo la informacion de robert, entraremos a la shell como su usuario

![Untitled](../../images/Untitled%2018.png)

- Lo que podemos hacer ahora es intentar escalar privilegios, por que veremos que permisos con como root tiene este usuario, y como se puede ver no tiene acceso a ninguno. por lo que procederemos a ver que permisos tiene. Bugtracker suena muy interesante

![Untitled](../../images/Untitled%2019.png)

- Encontramos la ruta de bugtracker, y vemos que tenemos permisos de Read-write, a aveces estos binarios se pueden ejecutar para que nos den permisos de root. Ya que como se puede ver en los permisos, se ejecutaria como root

![Untitled](../../images/Untitled%2020.png)

- Se introdujo /bin/bash para ver que nos daba, y como se puede ver, esta ejecutando el comando cat, y aprece que todos estos estan ubicados en reports, y luego esta eliminando los archivos con el id ingresado

![Untitled](../../images/Untitled%2021.png)

- Asi quen podemos escribir un archivo en root/reports que generen un bin/bash y podriamos hacer que se ejecute como root para nosotros

[https://www.notion.so](https://www.notion.so)

- Ahora le damos al archivo el bit de ejecutable para que pueda ser ejecutado

![Untitled](../../images/Untitled%2022%201.png)

- y ahora que tiene el bit ejecutable lo podemos agregar a la ruta, por lo que configuramos el directorio actual en la ruta. Por lo que ahora /tmp estara configurada en la ruta

![Untitled](../../images/Untitled%2023.png)

- Ahora si ejecutamos bugtracker y si ejecutamos cualquier idm nos va a dar el root shell

![Untitled](../../images/Untitled%2024.png)

- Por lo que procederemos a encontrar la flag del root

![Untitled](../../images/Untitled%2025.png)

# Flag

user: f2c74ee8db7983851ab2a96a44eb7981

root: af13b0bee69f8a877c3faf667f7beacf