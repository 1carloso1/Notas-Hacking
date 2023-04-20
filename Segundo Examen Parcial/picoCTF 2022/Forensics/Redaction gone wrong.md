## Descripción
Now you DON’T see me. This report has some critical data in it, some of which have been redacted correctly, while some were not. Can you find an important key that was not redacted properly?

## Pistas
- How can you be sure of the redaction?

## Solución
- Para resolver este reto, se nos muestra un PDF con letras censuradas, por lo que no se pueden ver. Despues de analizar el contenido, nos podemos dar cuenta que podemos seleccionar el todo el texto (incluido el censurado), por lo que si lo ponemos en un editor de codigo podemos ver que el texto es:

```shell()
Financial Report for ABC Labs, Kigali, Rwanda for the year 2021.
Breakdown - Just painted over in MS word.
Cost Benefit Analysis
Credit Debit
This is not the flag, keep looking
Expenses from the
picoCTF{C4n_Y0u_S33_m3_fully}
Redacted document.
```

- Entonces la flag es:

```bash()
picoCTF{C4n_Y0u_S33_m3_fully}
```

## Notas adicionales
- Primero intente buscar los metadatos del documento, pero la solución fue mucho mas facil que eso.

## Referencias
- Sin referencias.