
## Descripción
We have recovered a binary and a text file. Can you reverse the flag.

## Pistas
- objdump and Gihdra are some tools that could assist with this

## Solución
- Para resolver este reto, se nos da un archivo ejecutable y una flag cifrada, ademas, en las pistas nos dicen que usemos `objdump` y `Gihdra `.
- Al analizar el ejecutable con `objdump`, nos da lo siguiente:

```bash()
─$ objdump -D rev -M intel | grep '<main>:' -A20
0000000000001185 <main>:
    1185:       55                      push   rbp
    1186:       48 89 e5                mov    rbp,rsp
    1189:       48 83 ec 50             sub    rsp,0x50
    118d:       48 8d 35 74 0e 00 00    lea    rsi,[rip+0xe74]        # 2008 <_IO_stdin_used+0x8>
    1194:       48 8d 3d 6f 0e 00 00    lea    rdi,[rip+0xe6f]        # 200a <_IO_stdin_used+0xa>
    119b:       e8 d0 fe ff ff          call   1070 <fopen@plt>
    11a0:       48 89 45 e8             mov    QWORD PTR [rbp-0x18],rax
    11a4:       48 8d 35 68 0e 00 00    lea    rsi,[rip+0xe68]        # 2013 <_IO_stdin_used+0x13>
    11ab:       48 8d 3d 63 0e 00 00    lea    rdi,[rip+0xe63]        # 2015 <_IO_stdin_used+0x15>
    11b2:       e8 b9 fe ff ff          call   1070 <fopen@plt>
    11b7:       48 89 45 e0             mov    QWORD PTR [rbp-0x20],rax
    11bb:       48 83 7d e8 00          cmp    QWORD PTR [rbp-0x18],0x0
    11c0:       75 0c                   jne    11ce <main+0x49>
    11c2:       48 8d 3d 57 0e 00 00    lea    rdi,[rip+0xe57]        # 2020 <_IO_stdin_used+0x20>
    11c9:       e8 62 fe ff ff          call   1030 <puts@plt>
    11ce:       48 83 7d e0 00          cmp    QWORD PTR [rbp-0x20],0x0
    11d3:       75 0c                   jne    11e1 <main+0x5c>
    11d5:       48 8d 3d 7e 0e 00 00    lea    rdi,[rip+0xe7e]        # 205a <_IO_stdin_used+0x5a>
    11dc:       e8 4f fe ff ff          call   1030 <puts@plt>
    11e1:       48 8b 55 e8             mov    rdx,QWORD PTR [rbp-0x18]
```

- Con esta infromacion no podemos hacer mucho, asi que abriremos el archivo con `Gihdra ` para ver el main descompilado, lo cual es:

```bash()
{
  size_t sVar1;
  char flag [23];
  char local_41;
  int local_2c;
  FILE *flagrev;
  FILE *local_20;
  uint j;
  int i;
  char rev;
  
  local_20 = fopen("flag.txt","r");
  flagrev = fopen("rev_this","a");
  if (local_20 == (FILE *)0x0) {
    puts("No flag found, please make sure this is run on the server");
  }
  if (flagrev == (FILE *)0x0) {
    puts("please run this on the server");
  }
  sVar1 = fread(flag,0x18,1,local_20);
  local_2c = (int)sVar1;
  if ((int)sVar1 < 1) {
                    /* WARNING: Subroutine does not return */
    exit(0);
  }
  for (i = 0; i < 8; i = i + 1) {
    rev = flag[i];
    fputc((int)rev,flagrev);
  }
  for (j = 8; (int)j < 0x17; j = j + 1) {
    if ((j & 1) == 0) {
      rev = flag[(int)j] + '\x05';
    }
    else {
      rev = flag[(int)j] + -2;
    }
    fputc((int)rev,flagrev);
  }
  rev = local_41;
  fputc((int)local_41,flagrev);
  fclose(flagrev);
  fclose(local_20);
  return;
}

```

- Pero solo nos interesa la parte donde se codifica la bandera:

```bash()
for (i = 0; i < 8; i = i + 1) {
    rev = flag[i];
    fputc((int)rev,flagrev);
  }
  for (j = 8; (int)j < 0x17; j = j + 1) {
    if ((j & 1) == 0) {
      rev = flag[(int)j] + '\x05';
    }
    else {
      rev = flag[(int)j] + -2;
    }
```

- Con la bandera codificada, podemos crear un script para desencriptar la bandera. Dicho programa es:

```python()
cifrado = "picoCTF{w1{1wq8/7376j.:} "
flag = ""

for i in range(8,len(cifrado)-1):
    if i & 1 == 0:
      flag += chr(ord(cifrado[i]) -5)
    else:
        flag += chr(ord(cifrado[i]) + 2)
print(flag)
```

- El cual nos da la bandera:

```bash()
picoCTF{r3v3rs312528e05}
```

## Notas adicionales
- El código recorre cada caracter en la cadena `cifrado`, comenzando en el índice 8 y hasta el penúltimo caracter. Si el índice `i` es par (verificado utilizando la expresión `i & 1 == 0`), entonces el caracter en la posición `i` se cifra restando 5 a su código ASCII utilizando la función `chr(ord(cifrado[i]) - 5)`. Si el índice `i` es impar, entonces el caracter en la posición `i` se cifra sumando 2 a su código ASCII utilizando la función `chr(ord(cifrado[i]) + 2)`.
- Los caracteres cifrados se concatenan a la cadena `flag` utilizando el operador `+=`. Después de que se ha recorrido toda la cadena `cifrado`, la cadena `flag` contiene el resultado del cifrado.

## Referencias 
- [Canal de hackadvisermx](https://www.youtube.com/@hackadvisermxyt)