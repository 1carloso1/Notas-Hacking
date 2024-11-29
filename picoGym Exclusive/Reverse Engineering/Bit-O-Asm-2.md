## Descripción
Can you figure out what is in the `eax` register? Put your answer in the picoCTF flag format: `picoCTF{n}` where `n` is the contents of the `eax` register in the decimal number base. If the answer was `0x11` your flag would be `picoCTF{17}`.Download the assembly dump [here](https://artifacts.picoctf.net/c/510/disassembler-dump0_b.txt).

## Pistas
- `PTR`'s or 'pointers', reference a location in memory where values can be stored.

## Solución
- Para resolver el reto, tenemos que entender como funciona el codigo ensamblador dado:

```
<+0>:     endbr64 
<+4>:     push   rbp
<+5>:     mov    rbp,rsp
<+8>:     mov    DWORD PTR [rbp-0x14],edi
<+11>:    mov    QWORD PTR [rbp-0x20],rsi
<+15>:    mov    DWORD PTR [rbp-0x4],0x9fe1a
<+22>:    mov    eax,DWORD PTR [rbp-0x4]
<+25>:    pop    rbp
<+26>:    ret
```

- <+0>: endbr64 Esta instrucción es específica de la arquitectura x86-64 y se utiliza para indicar el inicio de una función. Proporciona una señal para el procesador de que la función comienza en esta ubicación de memoria.

- <+4>: push rbp Esta instrucción realiza un "push" del valor del registro de base de pila (rbp) en la pila. Esto generalmente se hace al comienzo de una función para guardar el valor del registro rbp.

- <+5>: mov rbp,rsp Esta instrucción copia el valor del registro de pila (rsp) en el registro de base de pila (rbp). Esto establece el registro de base de pila para que apunte al inicio del marco de pila actual.

- <+8>: mov DWORD PTR [rbp-0x14],edi Esta instrucción mueve el valor del registro edi a la ubicación de memoria apuntada por rbp-0x14. En lenguaje ensamblador x86-64, el registro edi generalmente se utiliza para almacenar el primer argumento de una función.

- <+11>: mov QWORD PTR [rbp-0x20],rsi Esta instrucción mueve el valor del registro rsi a la ubicación de memoria apuntada por rbp-0x20. En x86-64, rsi suele utilizarse para almacenar el segundo argumento de una función.

- <+15>: mov DWORD PTR [rbp-0x4],0x9fe1a Esta instrucción mueve el valor inmediato 0x9fe1a (hexadecimal) a la ubicación de memoria apuntada por rbp-0x4.

- <+22>: mov eax,DWORD PTR [rbp-0x4] Esta instrucción mueve el valor almacenado en la ubicación de memoria apuntada por rbp-0x4 al registro eax. eax es un registro general utilizado para almacenar valores temporales o retornar valores de una función.

- <+25>: pop rbp Esta instrucción realiza un "pop" del valor actual de la pila y lo coloca en el registro rbp. Esto revierte la operación realizada en la instrucción "push rbp" y restaura el valor original del registro rbp.

- <+26>: ret Esta instrucción indica el final de la función y devuelve el control al llamador. La instrucción "ret" generalmente va seguida de una ubicación de memoria o registro que contiene la dirección de retorno.

- Como podemos ver, se nos dice que se mueve a la variable `eax` el valor de laubicación de memoria apuntada por rbp-0x4. el cual seria `0x9fe1a`, que en deciamal es:

```bash()
picoCTF{654874}
```

## Notas adicionales
- Solo es cuestión de detectar la variable.

## Referencias 
- Sin referencias  