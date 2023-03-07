## Descripción
Can you get the flag? Download this binary. Here's the test drive instructions:

    $ chmod +x gdbme
    $ gdb gdbme
    (gdb) layout asm
    (gdb) break *(main+99)
    (gdb) run
    (gdb) jump *(main+104)


## Solución

```bash()
picoCTF{d3bugg3r_dr1v3_197c378a}
```

## Notas adicionales

## Referencias 