## Descripción
Can you figure out what is in the `eax` register? Put your answer in the picoCTF flag format: `picoCTF{n}` where `n` is the contents of the `eax` register in the decimal number base. If the answer was `0x11` your flag would be `picoCTF{17}`.Download the assembly dump [here](https://artifacts.picoctf.net/c/530/disassembler-dump0_c.txt).

## Pistas
- Not everything in this disassembly listing is optimal.

## Solución
- Para resolver el reto, tenemos que entender como funciona el codigo ensamblador dado:

```
<+0>:     endbr64 
<+4>:     push   rbp
<+5>:     mov    rbp,rsp
<+8>:     mov    DWORD PTR [rbp-0x14],edi
<+11>:    mov    QWORD PTR [rbp-0x20],rsi
<+15>:    mov    DWORD PTR [rbp-0xc],0x9fe1a
<+22>:    mov    DWORD PTR [rbp-0x8],0x4
<+29>:    mov    eax,DWORD PTR [rbp-0xc]
<+32>:    imul   eax,DWORD PTR [rbp-0x8]
<+36>:    add    eax,0x1f5
<+41>:    mov    DWORD PTR [rbp-0x4],eax
<+44>:    mov    eax,DWORD PTR [rbp-0x4]
<+47>:    pop    rbp
<+48>:    ret

```

- En este reto, tenemos que analizar primero a que variables se les asigna un valor:

```
<+15>:    mov    DWORD PTR [rbp-0xc],0x9fe1a
<+22>:    mov    DWORD PTR [rbp-0x8],0x4
```

- Despues a `eax` se le asaigna el valor de `rbp-0xc` que es 0x9fe1a.
- Despues con la instruccion `imul   eax,DWORD PTR [rbp-0x8]`, se guarda en la variable `eax` el resultado de la multiplicación entre `eax` y `rbp-0x8` que nos da como resultado 0x27f868.
- Despues con la instruccion `add    eax,0x1f5` , se le suma a `eax` el valor de 0x1f5, lo que nos da como resultado `0x27fa5d`, que transformado a decimal seria:

```bash()
picoCTF{2619997}
```

## Notas adicionales
- Solo es cuestión de detectar la variable.

## Referencias 
- Sin referencias  