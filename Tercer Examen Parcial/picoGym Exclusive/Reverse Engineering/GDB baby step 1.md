## Descripción
Can you figure out what is in the `eax` register at the end of the `main` function? Put your answer in the picoCTF flag format: `picoCTF{n}` where `n` is the contents of the `eax` register in the decimal number base. If the answer was `0x11` your flag would be `picoCTF{17}`.Disassemble [this](https://artifacts.picoctf.net/c/512/debugger0_a).

## Pistas
- gdb is a very good debugger to use for this problem and many others!
- `main` is actually a recognized symbol that can be used with gdb commands.

## Solución
- Para desensamblar el codigo, debemos darle permisos de ejecucion al programa `gdbdebugger_a` y luego ejecurlo con el comando `gdb debugger0_a`, que nos dira `(No debugging symbols found in debugger0_a)`, por lo que utilizaremos el comando `(gdb) layout asm` que nos mostrara:

![[debugger_A_asm.png]]

- Ya desensamblado, solo es cuestion de buscar la variable `eax`, que solo aparece una vez en el codigo, recibiendo el valor hexadecimal 0x86342, que en decimal seria 549698

```bash()
picoCTF{549698}
```

## Notas adicionales
- Solo es cuestión de detectar la variable.

## Referencias 
- Sin referencias  