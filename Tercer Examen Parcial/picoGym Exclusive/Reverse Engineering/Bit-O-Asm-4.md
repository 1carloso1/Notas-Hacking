## Descripción
Can you figure out what is in the `eax` register? Put your answer in the picoCTF flag format: `picoCTF{n}` where `n` is the contents of the `eax` register in the decimal number base. If the answer was `0x11` your flag would be `picoCTF{17}`.Download the assembly dump [here](https://artifacts.picoctf.net/c/511/disassembler-dump0_d.txt).

## Pistas
- Don't tell anyone I told you this, but you can solve this problem without understanding the compare/jump relationship.
- Of course, if you're really good, you'll only need one attempt to solve this problem.

## Solución
- En este reto, tenemos que analizar primero a que variables se les asigna un valor:

```
<+15>:    mov    DWORD PTR [rbp-0x4],0x9fe1a
```

- Despues se compara si 0x9fe1a es menor igual a 0x2710, lo que es falso, por lo que no se cumple la condicion para saltar a <main+37>
- Le restamos 0x65 a 0x9fe1a, despues se saltara a <main+41>, donde le asiganeremos el resultado a la variable `eax` que es 0x9fdb5, en decimal seria:

```bash()
picoCTF{654773}
```

## Notas adicionales
- el registro edi generalmente se utiliza para almacenar el primer argumento de una función.
- rsi suele utilizarse para almacenar el segundo argumento de una función.

## Referencias 
- Sin referencias  
