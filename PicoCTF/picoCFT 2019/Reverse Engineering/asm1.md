## Descripción
What does asm1(0x8be) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. [Source](https://jupiter.challenges.picoctf.org/static/66c927e32f3d7be7a62d13a7c2250943/test.S)

## Pistas
- assembly [conditions](https://www.tutorialspoint.com/assembly_programming/assembly_conditions.htm)

## Solución
- 1.  En este reto se nos da un código en ensamblador:

```bash()
asm1:
        <+0>:   push   ebp
        <+1>:   mov    ebp,esp
        <+3>:   cmp    DWORD PTR [ebp+0x8],0x71c
        <+10>:  jg     0x512 <asm1+37>
        <+12>:  cmp    DWORD PTR [ebp+0x8],0x6cf
        <+19>:  jne    0x50a <asm1+29>
        <+21>:  mov    eax,DWORD PTR [ebp+0x8]
        <+24>:  add    eax,0x3
        <+27>:  jmp    0x529 <asm1+60>
        <+29>:  mov    eax,DWORD PTR [ebp+0x8]
        <+32>:  sub    eax,0x3
        <+35>:  jmp    0x529 <asm1+60>
        <+37>:  cmp    DWORD PTR [ebp+0x8],0x8be
        <+44>:  jne    0x523 <asm1+54>
        <+46>:  mov    eax,DWORD PTR [ebp+0x8]
        <+49>:  sub    eax,0x3
        <+52>:  jmp    0x529 <asm1+60>
        <+54>:  mov    eax,DWORD PTR [ebp+0x8]
        <+57>:  add    eax,0x3
        <+60>:  pop    ebp
        <+61>:  ret    

```

- 2.  Con ayuda de Python realizamos las comparaciones indicadas y obtenemos la flag:

```bash()
>>> 0x8be > 0x71c
True
>>> 0x8be != 0x8be
False
>>> hex(0x8be - 0x3)
'0x8bb'
```

La flag que regresa es:

```
0x8bb
```

## Notas adicionales
### **¿Qué es el Lenguaje Ensamblador?**

El **lenguaje ensamblador** es un lenguaje de nivel bajo, que está cerca de ser comprendido al mismo tiempo por el programador o desarrollador de software y las computadoras.  Estas últimas emplean lenguaje binario para llevar a cabo cada proceso, mientras que los programadores utilizan lenguajes de programación de niveles alto o intermedio.  El primer lenguaje ensamblador fue desarrollado por **Kathleen Booth** alrededor de los años 50 y cambió el mundo de la programación para siempre; desde ese momento se hizo más sencillo crear programas.

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