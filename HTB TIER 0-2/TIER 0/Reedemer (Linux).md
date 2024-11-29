# Reedemer (Linux)

## Solución

- Con nmap se encontro el puerto 6379 abierto con el servicio redis corriendo en el
- Entramos al servicio con el comando redis-cli, ‘-h’ especifica el host, en este caso la ip

![Captura de pantalla 2023-02-10 134722.png](Captura_de_pantalla_2023-02-10_134722.png)

- Con el comando ‘info’ dentro de redis-cli nos muestra la informacion del servidor

![Captura de pantalla 2023-02-10 134904.png](Captura_de_pantalla_2023-02-10_134904.png)

- Con ‘keys *’ podemos ver todas las llaves que tiene la base de datos, y con get podemos obtener la deseada

![Captura de pantalla 2023-02-10 140120.png](Captura_de_pantalla_2023-02-10_140120.png)

## Flag

03e1d2b376c37ab3f5319922053953eb