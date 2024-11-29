## Descripción
This vault uses ASCII encoding for the password. The source code for this vault is here: [VaultDoor4.java](https://jupiter.challenges.picoctf.org/static/834acd392e0964a41f05790655a994b9/VaultDoor4.java)

## Solución
- La pista que se nos da en el programa es que trasnformo la flag en diferentes bases.
- Si analizamos el codigo, podemos ver que la flag se guarda en la siguiente variable

```
byte[] myBytes = {  
    106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,  
    0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,  
    0142, 0131, 0164, 063 , 0163, 0137, 0146, 064 ,  
    'a' , '8' , 'c' , 'd' , '8' , 'f' , '7' , 'e' ,  
};
```

- Podemos ver que cada renglon esta transformado en una base diferente, solo tenemos que averiguar a que base se transformo y regresarlo a ASCII.
	- 1, decimal a ASCII = jU5t_4_b
	- 2, hexadecimal a ASCII = UnCh_0f_
	- 3, octal a ASCII = bYt3s_f4
	- 4, ASCII = a8cd8f7e
- Si juntamos las cadenas, obtenemos la flag: 

```bash()
jU5t_4_bUnCh_0f_bYt3s_f4a8cd8f7e
```

## Notas adicionales
- Esta fue mi manera de encontrar la solución, probablemente no sea la mejor ni la mas facil de hacer, pero cumple su función.
- Solo se debe analizar el codigo y enfocarnos en los metodos que analizan la flag.

## Referencias 
- Sin referencias.