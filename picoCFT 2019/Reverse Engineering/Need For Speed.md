
## Descripción
The name of the game is speed. Are you quick enough to solve this problem and keep it above 50 mph? need-for-speed.

## Pistas
- What is the final key?

## Solución
- Usaremos `gdb` para ejecutar el programa y modificar la ejecucion dle programa de tal manera que podemamos alterar el valor de las variables o mandar llamar una funcion. Haremos un analisis mas dinamico.
- Para ejecutar el archivo, tenemos que darle permisos al problema.
- Ya ejecutado, utilizaremos el comando `(gdb) set disassembly-flavor intel` para ver la salida en formato intel.
- Procederemos a desensamblar la funcion 'main', con el comando disassemble main`. Se nos mostrara

```bash()
  0x000000000000091a <+0>:     push   rbp
   0x000000000000091b <+1>:     mov    rbp,rsp
   0x000000000000091e <+4>:     sub    rsp,0x10
   0x0000000000000922 <+8>:     mov    DWORD PTR [rbp-0x4],edi
   0x0000000000000925 <+11>:    mov    QWORD PTR [rbp-0x10],rsi
   0x0000000000000929 <+15>:    mov    eax,0x0
   0x000000000000092e <+20>:    call   0x8d8 <header>
   0x0000000000000933 <+25>:    mov    eax,0x0
   0x0000000000000938 <+30>:    call   0x82f <set_timer>
   0x000000000000093d <+35>:    mov    eax,0x0
   0x0000000000000942 <+40>:    call   0x87d <get_key>
   0x0000000000000947 <+45>:    mov    eax,0x0
   0x000000000000094c <+50>:    call   0x8ac <print_flag>
   0x0000000000000951 <+55>:    mov    eax,0x0
   0x0000000000000956 <+60>:    leave
   0x0000000000000957 <+61>:    ret

```

- Lo siguiente es establecer un punto de interrupcion en algun lugar para alterar su funcionamiento con `(gdb) break main`

```bash()
Breakpoint 1 at 0x91e
```

- Vamos a correr de nuevo el programa con `(gdb) run` y lo volveremos a desensamblar, para ver que ya se nos muestra la interrupcion

```bash()
Dump of assembler code for function main:
   0x000055555540091a <+0>:     push   rbp
   0x000055555540091b <+1>:     mov    rbp,rsp
=> 0x000055555540091e <+4>:     sub    rsp,0x10
   0x0000555555400922 <+8>:     mov    DWORD PTR [rbp-0x4],edi
   0x0000555555400925 <+11>:    mov    QWORD PTR [rbp-0x10],rsi
   0x0000555555400929 <+15>:    mov    eax,0x0
   0x000055555540092e <+20>:    call   0x5555554008d8 <header>
   0x0000555555400933 <+25>:    mov    eax,0x0
   0x0000555555400938 <+30>:    call   0x55555540082f <set_timer>
   0x000055555540093d <+35>:    mov    eax,0x0
   0x0000555555400942 <+40>:    call   0x55555540087d <get_key>
   0x0000555555400947 <+45>:    mov    eax,0x0
   0x000055555540094c <+50>:    call   0x5555554008ac <print_flag>
   0x0000555555400951 <+55>:    mov    eax,0x0
   0x0000555555400956 <+60>:    leave
   0x0000555555400957 <+61>:    ret
End of assembler dump.
```

- Que tal si directamente mandamos llamar <get_key> y <print_flag> para obtener la bandera

```bash()
(gdb) call (int) get_key()
Creating key...
Finished
$1 = 9
(gdb) call (int) print_flag()
Printing flag:
PICOCTF{Good job keeping bus #190ca38b speeding along!}
```

- La bandera es:

```bash()
PICOCTF{Good job keeping bus #190ca38b speeding along!}

```

## Notas adicionales
- GDB es un depurador a nivel de fuente, capaz de romper programas en cualquier línea específica, mostrar valores variables y determinar dónde ocurrieron los errores. Actualmente, gdb es compatible con C, C++, D, Objective-C, Fortran, Java, OpenCL C, Pascal, ensamblado, Modula-2, Go y Ada. Imprescindible para cualquier programador serio.

## Referencias 
- [Canal de hackadvisermx](https://www.youtube.com/@hackadvisermxyt)
