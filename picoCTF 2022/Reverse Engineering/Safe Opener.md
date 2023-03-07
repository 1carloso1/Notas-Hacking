## Descripción
Can you open this safe?I forgot the key to my safe but this [program](https://artifacts.picoctf.net/c/463/SafeOpener.java) is supposed to help me with retrieving the lost key. Can you help me unlock my safe?Put the password you recover into the picoCTF flag format like:`picoCTF{password}`

## Solución
- Para poder realizar este reto es necesario checar a detalle el codigo fuente, ya que sabiendo de que manera esta codificada la flag, podemos aplicar la ingenieria reversa para poder obtener la solución.
- La pista mas importante es la siguiente:

```java()
encodedkey = encoder.encodeToString(key.getBytes());
```

- Se codifica el parametro recibido `key` en base 64 para comparar con la contraseña original, lo que nos dice que la contraseña original esta codifica en 64 bits, por lo que se procedera a decodificar en 64 bits la original.

```bash()
encodedkey = "cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz" == picoCTF{pl3as3_l3t_m3_1nt0_th3_saf3}
```

## Notas adicionales
- Se decodifico la contraseña en base 64 en [base64decode.org](https://www.base64decode.org/)

## Referencias 