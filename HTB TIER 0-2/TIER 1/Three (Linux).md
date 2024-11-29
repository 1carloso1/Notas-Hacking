# Three (Linux)

- Se encontro el puerto 80 con el servicio http
- Se ingreso la ip al navegador para ver el sitio

![Untitled](Untitled%2026.png)

- Se encontro que en el apartado de Contacto, habia un dominio, por que se procedio a agregarlo al script donde se encuentran los host para poder acceder a el de manera forzada.

![Untitled](Untitled%201%203.png)

![Untitled](Untitled%202%203.png)

- No se encontro nada, por lo que procedi a buscar subdominios (no se encontro el subdominio con mi pc, por lo que supongo que fue un error de instalacion de seclists)

[https://www.notion.so](https://www.notion.so)

![Untitled](Untitled%203%203.png)

- El subdominio encontrado tambien fue agregado al script de hosts

![Untitled](Untitled%204%203.png)

- El dominio nos da lo siguiente, por lo que podemos suponer que esta corriendo un servicio

![Untitled](Untitled%205%203.png)

- Con awscli podemos obtener mas informacion ndel subdominio, lo que nos da la informacion necesarua para atacar, ya que encontramos que la pagina esta hecha con php

![Untitled](Untitled%206%203.png)

- Procedemos a crear un archivo php para poder crear un webshell

![Untitled](Untitled%207%203.png)

- el archivo php creado lo podemos agregar al sitio con awscli para poder acceder a el desde el url de la pagina

![Untitled](Untitled%208%203.png)

- Con este simple comando dentro de la url podemos comprobar su funcionalidad

![Untitled](Untitled%209%203.png)

- Procedemos a crear una shell reversa en, por lo que necesitamos la ip de algun tun, en este caso tun0, para oder crear la shell reversa

![Untitled](Untitled%2010%203.png)

![Untitled](Untitled%2011%203.png)

- Despues generada la shell reversa, la guardamos en un archivo

![Untitled](Untitled%2012%203.png)

- Lo siguiente es crear una estancia para escuchar en un puerto la reverse shell

![Untitled](Untitled%2013%202.png)

- Lo siguiente es crear un servicio web para poder lanzar nuestro rever shell

![Untitled](Untitled%2014%202.png)

- Teniendo el servico web activo, procedemos a escribir en la web shell, el ip de tun0 (el mismo que de el reverse shell creado), el puerto del servicio web, y el archivo de reverse shell, lo que hace el bash es que toma el contenido de este comando, y lo manda a la estancia que va a escuchar

![Untitled](Untitled%2015%201.png)

- Si se siguio el procedimiento, podremos ver que se conecto con la estancia para escuchar hecha anteriormente

![Untitled](Untitled%2016%201.png)

- Procedemos a encontrar la flag

![Untitled](Untitled%2017%201.png)

# Flag

a980d99281a28d638ac68b9bf9453c2b