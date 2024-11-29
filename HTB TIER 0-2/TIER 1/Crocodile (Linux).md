# Crocodile (Linux)

- Se encontro el puerto 21 abierto con el servicio ftp y el servicio 80 abierto con el servicio http
- Se ingresa al servicio ftp por medio de la consola
    
    ![Captura de pantalla 2023-02-10 150908.png](../../images/Captura_de_pantalla_2023-02-10_150908.png)
    
- Comandar ls para ver los documentos y extraer los de interes.
    
    ![Captura de pantalla 2023-02-10 151114.png](../../images/Captura_de_pantalla_2023-02-10_151114.png)
    
- Verificamos el contenido de los archivos

![Captura de pantalla 2023-02-10 151229.png](../../images/Captura_de_pantalla_2023-02-10_151229.png)

- Entramos al sitio http de la ip de la maquina atacante.
    
    ![Captura de pantalla 2023-02-10 150107.png](../../images/Captura_de_pantalla_2023-02-10_150107.png)
    
- Para poder encontrar una pista de la flag, se intenta encontrar alguna vulnereabilidad del sitio, no se encontro una a la vista, por lo que con gobuster intentare encontrar una url
- Con el siguiente comando de gobuster encontre una url que me llamo la antencion, por lo que entre en ella
    
    ![Captura de pantalla 2023-02-10 152256.png](../../images/Captura_de_pantalla_2023-02-10_152256.png)
    
- En esta interface puedo probar los usuarios y contraseñas que encontre previamente

![Captura de pantalla 2023-02-10 152505.png](../../images/Captura_de_pantalla_2023-02-10_152505.png)

- Con el usuario:’admin’ y la contraseña ‘rKXM59ESxesUFHAd’ pude ingresar y encontrar la bandera

![Untitled](../../images/Untitled%2013.png)

# Flag

c7110277ac44d78b6a9fff2232434d16