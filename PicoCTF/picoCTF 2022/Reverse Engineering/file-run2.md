## Descripción
Another program, but this time, it seems to want some input. What happens if you try to run it on the command line with input "Hello!"?Download the program [here](https://artifacts.picoctf.net/c/351/run).

## Solución
- Para obtener la flag solo se necesita ejecutar el programa dado agregandole la cadena `Hello!`. Pero para eso es necesario darle permisos con el comando `chmod +x`.
```bash()
└─$ ./run Hello!  
The flag is: picoCTF{U51N6_Y0Ur_F1r57_F113_9bc52b6b}  
```

## Notas adicionales
- Un nivel muy facil, no se necesitan notas adicionales.

## Referencias 