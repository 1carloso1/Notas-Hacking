## Descripción
What does asm2(0xb,0x2e) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. Source

## Pistas
- assembly conditions

## Solución
En este desafío, tenemos el código fuente de un fragmento de código ensamblador. El nombre del archivo es test.S y debajo puede ver el fragmento de código:

```bash()
asm2:
	<+0>:	push   ebp
	<+1>:	mov    ebp,esp
	<+3>:	sub    esp,0x10
	<+6>:	mov    eax,DWORD PTR [ebp+0xc]
	<+9>:	mov    DWORD PTR [ebp-0x4],eax
	<+12>:	mov    eax,DWORD PTR [ebp+0x8]
	<+15>:	mov    DWORD PTR [ebp-0x8],eax
	<+18>:	jmp    0x509 <asm2+28>
	<+20>:	add    DWORD PTR [ebp-0x4],0x1
	<+24>:	sub    DWORD PTR [ebp-0x8],0xffffff80
	<+28>:	cmp    DWORD PTR [ebp-0x8],0x63f3
	<+35>:	jle    0x501 <asm2+20>
	<+37>:	mov    eax,DWORD PTR [ebp-0x4]
	<+40>:	leave  
	<+41>:	ret
```

- Repasemos cada instrucción de este bloque de código de una en una:
1.  Primero, estamos asignando al registro **eax** el valor en **ebp+0xc**  que es **0x2e** , según la pila.
2.  Luego, movemos el valor en el registro **eax** a **ebp-0x4** , que en nuestro caso es **local1** , haciéndolo igual a **0x2e** .
3.  Luego, movemos el contenido **ebp+0x8** a **eax** , haciéndolo igual a **0xb** .
4.  En la línea +15 movemos el contenido del registro **eax** a **ebp-0x8** , que es la variable **local2** , haciéndolo igual a **0xb** .
5.  Finalmente, saltamos a **asm2+28** .
- Como saben, la instrucción anterior nos hizo saltar a asm2+28, que es una comparación, seguido de un salto si es menor o igual a. En este caso, tenemos una comparación entre  **ebp-0x8** (que sabemos que es local2 y es igual a  **0xb** ) y  **0x63f3** . Sabemos que  **0xb**  es menor que  **0x63f3**  , así que damos el salto a  **asm2+20** .
- En la línea +20 tenemos una instrucción de suma, estamos sumando 1 a  **ebp-0x4** , convirtiéndolo en 0x2f.
- En la línea +24 tenemos una subinstrucción, estamos restando 0xffffff80 a ebp-0x8. Esta es una arquitectura 0x86 por lo que tenemos que truncar el resultado.
- Después de ejecutar el código obtenemos la bandera:
- 
```bash()
0xf6
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