## Descripción
A musician left us a [message](https://jupiter.challenges.picoctf.org/static/d5570d48262dbba2a31f2a940409ad9d/message.txt). What's it mean?

## Pistas
- (None)

## Solución
- Pra resolver este reto, se nos da la flag, pero en lugar de caracteres nos da coordenadas:

```bash()
picoCTF{(35.028309, 135.753082)(46.469391, 30.740883)(39.758949, -84.191605)(41.015137, 28.979530)(24.466667, 54.366669)(3.140853, 101.693207)_(9.005401, 38.763611)(-3.989038, -79.203560)(52.377956, 4.897070)(41.085651, -73.858467)(57.790001, -152.407227)(31.205753, 29.924526)}
```

- Si buscamos las coordenadas podremos encontrar ubicaciones reales, por lo que podriamos obtener la flag de la primera letra de la ubicación

| Coordenadas | Ubicación | Letra |
| --- | --- | --- |
| (35.028309, 135.753082) | Kyoto, Japan | **K** |
| (46.469391, 30.740883) | Odessa, Ukraine | **O** |
| (39.758949, -84.191605) | Dayton, United States | **D** |
| (41.015137, 28.979530) | Istanbul, Turkey | **I** |
| (24.466667, 54.366669) | Abu Dhabi, UAE | **A** |
| (3.140853, 101.693207) | Kuala Lumpur, Malaysia | **K** |
| (9.005401, 38.763611) | Addis Ababa, Ethiopia | **A** |
| (-3.989038, -79.203560) | Loja, Ecuador | **L** |
| (52.377956, 4.897070) | Amsterdam, Netherlands | **A** |
| (41.085651, -73.858467) | Sleepy Hollow, USA | **S** |
| (57.790001, -152.407227) | Kodiak, United States | **K** |
| (31.205753, 29.924526) | Alexandria, Egypt | **A** |

- Las letras forman el nombre de dos ubicaciones, por lo que las podriamos separar como se hace habitalmente con una flag: `KODIAK_ALASKA`. Entonces la flag seria:

```bash()
picoCTF{KODIAK_ALASKA}
```

## Notas adicionales
- Las ubicaciones las encontre gracias a google maps.

## Referencias 
