# Sequel(Linux)

- Se encontro que el puerto 3306 estaba abierto corriendo un servicio de mySQL
- Por lo que se procedio a ingresar por comando al servicio, donde ‘-h’ es el host, osea el ip de la maquina objetivo y ‘-u’ es el usuario (Se agrega root por que no solicita contraseña)

![Captura de pantalla 2023-02-10 144034.png](Captura_de_pantalla_2023-02-10_144034.png)

- Para ver las bases de datos del servidor, utilizamos el siguiente comando:
    
    ![Captura de pantalla 2023-02-10 144811.png](Captura_de_pantalla_2023-02-10_144811.png)
    
- En este caso nos interesa la llamada ‘hbt’, por lo que con el comando ‘use’ entramos en la base de datos

![Captura de pantalla 2023-02-10 145110.png](Captura_de_pantalla_2023-02-10_145110.png)

![Captura de pantalla 2023-02-10 145313.png](Captura_de_pantalla_2023-02-10_145313.png)

- Ya estando en la base de datos procedemos a ver las tablas que contiene para ver donde podria estar la flag
- Con la siguiente linea, se puede mostrar todo el contenido de cada tabla, para asi encontrar la flag
    
    ![Captura de pantalla 2023-02-10 145512.png](Captura_de_pantalla_2023-02-10_145512.png)
    

# Flag

7b4bec00d1a39e3dd4e021ec3d915da8