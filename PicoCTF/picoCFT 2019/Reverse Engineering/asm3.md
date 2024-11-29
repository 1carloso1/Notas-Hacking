## Descripción
What does asm3(0xba6c5a02,0xd101e3dd,0xbb86a173) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. Source

## Pistas
-more(?) registers

## Solución
- En este reto se nos da un código en ensamblador:

```bash()
asm3:
        <+0>:   push   ebp
        <+1>:   mov    ebp,esp
        <+3>:   xor    eax,eax
        <+5>:   mov    ah,BYTE PTR [ebp+0xb]
        <+8>:   shl    ax,0x10
        <+12>:  sub    al,BYTE PTR [ebp+0xd]
        <+15>:  add    ah,BYTE PTR [ebp+0xc]
        <+18>:  xor    ax,WORD PTR [ebp+0x12]
        <+22>:  nop
        <+23>:  pop    ebp
        <+24>:  ret   
```

- 2.  Editamos el código para poder emularlo en [Assembly x86 Emulator](https://carlosrafaelgn.com.br/Asm86/)y lo ejecutamos paso por paso con la ventana registros abierta. La flag que obtendremos sera: 

```bash()
0x669b
```

## Notas adicionales
**¿Qué es el Lenguaje Ensamblador?** El **lenguaje ensamblador** es un lenguaje de nivel bajo, que está cerca de ser comprendido al mismo tiempo por el programador o desarrollador de software y las computadoras.  Estas últimas emplean lenguaje binario para llevar a cabo cada proceso, mientras que los programadores utilizan lenguajes de programación de niveles alto o intermedio.  El primer lenguaje ensamblador fue desarrollado por **Kathleen Booth** alrededor de los años 50 y cambió el mundo de la programación para siempre; desde ese momento se hizo más sencillo crear programas.

**Estas son algunas instrucciones usadas en lenguaje ensamblador:**

-   **add.** Instruye al procesador para que sume dos operandos y almacene el resultado.
-   **mov.** Es una instrucción común en varios lenguajes ensambladores, sirve para mover datos o registros de un sitio a otro.
-   **mul.** Da instrucciones al procesador de realizar la multiplicación de dos operandos, cumpliendo previamente con ciertas condiciones.
-   **and.** Es la instrucción necesaria para utilizar el operador lógico ‘y’ en lenguaje ensamblador.
-   **cmp.** Esta instrucción **resta el operando fuente al operando destino pero sin que éste almacene el resultado de la operación**, solo se afecta el estado de las banderas.
-   **jg:** Salta si es más grande o salta si no es menor o igual.

## Referencias 
-   [https://www.cs.virginia.edu/~evans/cs216/guides/x86.html](https://www.cs.virginia.edu/~evans/cs216/guides/x86.html)
-   [https://moisesrbb.tripod.com/unidad5.htm#u518](https://moisesrbb.tripod.com/unidad5.htm#u518) 