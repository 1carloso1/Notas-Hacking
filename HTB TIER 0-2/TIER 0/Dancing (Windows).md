# Dancing (Windows)

## Solución

- Con nmap se encontro lo siguiente:

![../../../images/Captura de pantalla 2023-02-10 130458.png](Captura_de_pantalla_2023-02-10_130458.png)

por lo que vemos que esta el puerto 445, por lo que podemos operar con smb

- Con -L podemos ver listados los recursos compartidos para encontrar la flag

![Captura de pantalla 2023-02-10 130755.png](Captura_de_pantalla_2023-02-10_130755.png)

- El recurso compartido Workshares no pide contraseña, por lo cual entraremos ahi con -N + la ruta. Estando dentro de la consola windows, procedemos a buscar la bandera y descargarla

![Captura de pantalla 2023-02-10 131629.png](Captura_de_pantalla_2023-02-10_131629.png)

- Verificamos que se haya descargado y la leemos en caso de que este

![Captura de pantalla 2023-02-10 131748.png](Captura_de_pantalla_2023-02-10_131748.png)

## Flag

5f61c10dffbc77a704d76016a22f1664