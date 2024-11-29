# Responder(Windows)

- Encontramos el puerto 80 abierto con el servicio windows
- Al ingresar en el navegador con la ip de la maquina objetivo, marca un error, por lo que se procede a forzar el sitio

![Untitled](images/Untitled%2022.png)

- Para forzar el sitio, tenemos que agregar el ip y el sitio al documento donde se almacenan los host

![Untitled](Untitled%201%202.png)

- Al realizar eso, recargamos la pagina y ahora podremos acceder a ella./

![Untitled](Untitled%202%202.png)

- Al estar analizando la pagina, podemos ver que hay una posible vulnerabilidad en el sitio relacionado a la url, por lo que podemos tratar de encontrar informacion vulnerable

![Untitled](Untitled%203%202.png)

- como podemos ver en la siguiente imagen, esta simple linea nos muestra algunas vulnerabilidades relacionadas con la url

![Untitled](Untitled%204%202.png)

![Untitled](Untitled%205%202.png)

- Podemos proceder a utilizar el comando **responder**, este responde a consultas NetBIOS específicas basadas en la solicitud del servidor de archivos.Para esto necesitamos saber que tunel esta disponible e utilizar su ip

![Untitled](Untitled%206%202.png)

![Untitled](Untitled%207%202.png)

- Podemos añadir a la url: [//”ip”/testShare](notion://10.10.14.52/testShare) para poder recibir el usuario y la contraseña encriptada
    - Se puede observar que se nos da el usuario y la contraseña encriptada

![Untitled](Untitled%208%202.png)

![Untitled](Untitled%209%202.png)

- Se procede a guardar la contraseña en un archivo .txt para proceder a desencriptar con el siguiente comando

![Untitled](Untitled%2010%202.png)

- Con el usuario y contraseña procedemos a utilizar el siguiente comando para adueñarnos de la maquina

![Untitled](Untitled%2011%202.png)

- Estando en la consola de windows, procedemos a buscar la flag

![Untitled](Untitled%2012%202.png)

# Flag

ea81b7afddd03efaa0945333ed147fac