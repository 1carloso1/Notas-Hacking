## Descripción
This program has constructed the flag using hex ascii values. Identify the flag text by disassembling the program.You can download the file from [here](https://artifacts.picoctf.net/c/506/asciiftw).

## Pistas
- The combined range of hex-ascii for English alphabets and numerical digits is from 30 to 7A.
- Online hex-ascii converters can be helpful.

## Solución
- Para resolver este reto, debemos desensamblar el codigo, debido a que el archivo que nos dan es un ejecutable. Yo utilice el programa `ghidra`.
- Ya teniendo el codigo desensamblado, podemos empezar a analizar el codigo ensamblador, un recordatorio muy importante es  que la bandera empieza con el valor hexadecimal 70 ('p'). 
- Encontramos en la funcion main lo siguiente:}

```
        00101184 c6 45 d0 70     MOV        byte ptr [RBP + local_38],0x70
        00101188 c6 45 d1 69     MOV        byte ptr [RBP + local_37],0x69
        0010118c c6 45 d2 63     MOV        byte ptr [RBP + local_36],0x63
        00101190 c6 45 d3 6f     MOV        byte ptr [RBP + local_35],0x6f
        00101194 c6 45 d4 43     MOV        byte ptr [RBP + local_34],0x43
        00101198 c6 45 d5 54     MOV        byte ptr [RBP + local_33],0x54
        0010119c c6 45 d6 46     MOV        byte ptr [RBP + local_32],0x46
        001011a0 c6 45 d7 7b     MOV        byte ptr [RBP + local_31],0x7b
        001011a4 c6 45 d8 41     MOV        byte ptr [RBP + local_30],0x41
        001011a8 c6 45 d9 53     MOV        byte ptr [RBP + local_2f],0x53
        001011ac c6 45 da 43     MOV        byte ptr [RBP + local_2e],0x43
        001011b0 c6 45 db 49     MOV        byte ptr [RBP + local_2d],0x49
        001011b4 c6 45 dc 49     MOV        byte ptr [RBP + local_2c],0x49
        001011b8 c6 45 dd 5f     MOV        byte ptr [RBP + local_2b],0x5f
        001011bc c6 45 de 49     MOV        byte ptr [RBP + local_2a],0x49
        001011c0 c6 45 df 53     MOV        byte ptr [RBP + local_29],0x53
        001011c4 c6 45 e0 5f     MOV        byte ptr [RBP + local_28],0x5f
        001011c8 c6 45 e1 45     MOV        byte ptr [RBP + local_27],0x45
        001011cc c6 45 e2 41     MOV        byte ptr [RBP + local_26],0x41
        001011d0 c6 45 e3 53     MOV        byte ptr [RBP + local_25],0x53
        001011d4 c6 45 e4 59     MOV        byte ptr [RBP + local_24],0x59
        001011d8 c6 45 e5 5f     MOV        byte ptr [RBP + local_23],0x5f
        001011dc c6 45 e6 33     MOV        byte ptr [RBP + local_22],0x33
        001011e0 c6 45 e7 43     MOV        byte ptr [RBP + local_21],0x43
        001011e4 c6 45 e8 46     MOV        byte ptr [RBP + local_20],0x46
        001011e8 c6 45 e9 34     MOV        byte ptr [RBP + local_1f],0x34
        001011ec c6 45 ea 42     MOV        byte ptr [RBP + local_1e],0x42
        001011f0 c6 45 eb 46     MOV        byte ptr [RBP + local_1d],0x46
        001011f4 c6 45 ec 41     MOV        byte ptr [RBP + local_1c],0x41
        001011f8 c6 45 ed 44     MOV        byte ptr [RBP + local_1b],0x44
        001011fc c6 45 ee 7d     MOV        byte ptr [RBP + local_1a],0x7d
```

- Si solo tomamos los valores hexadecimales, tenemos la cadena

```
70 69 63 6F 43 54 46 7B 41 53 43 49 49 5F 49 53 5F 45 41 53 59 5F 33 43 46 34 42 46 41 44 7D
```

- Utilizaremos [rapidtables](https://www.rapidtables.com/convert/number/ascii-hex-bin-dec-converter.html) para transformar de HEX a ASCII y obtenemos la flag:
```bash()
picoCTF{ASCII_IS_EASY_3CF4BFAD}
```

## Notas adicionales
- Hay que analizar el codigo ensamblador, no descompilado

## Referencias 
- Sin referencias