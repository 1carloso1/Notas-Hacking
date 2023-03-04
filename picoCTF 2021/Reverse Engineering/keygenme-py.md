## Descripción
[keygenme-trial.py](https://mercury.picoctf.net/static/9055e7d35f5f4646338a1734aea0dda5/keygenme-trial.py)

## Solución
- Para poder obtener la flag de este problema no se necesita ejecutar el codigo dado, ya que no nos interesa su funcionalidad. Lo que nos interesa son algunas variables. Estas variables muestran de forma muy obvia que son fragmentos de la Flag. Pero hace falta una parte, esta parte la obtendremos a traves de la variable `username_trial` y con ayuda de algunas funciones de `hashlib`.
- Casi al final del codigo podemos ver que el valor de la variable que nos falta esta codificado a traves de la variable  `username_trial`, y nos da la posicion de las letras codificadas. Por lo que estas posiciones nos serviran para pode realizar un form que de forma reversa obtenga el valor codificado.
- Al obtener el valor, lo sumamos con las demas partes de la Flag para poder obtener la Flag 
- completa.

```python()
import hashlib

key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_static2_trial = "}"
username_trial = b"FRASER"
potential_dynamic_key = ""

# positions in username_trial
positions = [4,5,3,6,2,7,1,8]

for p in positions:
    potential_dynamic_key += hashlib.sha256(username_trial).hexdigest()[p]

key = key_part_static1_trial + potential_dynamic_key + key_part_static2_trial

print(key)
```

```bash()
picoCTF{1n_7h3_|<3y_of_ac73dc29}
```
## Notas adicionales
- No se necesito el codigo original, solo revisar la información y sustraer las varibales importantes para poder generar la Flag.

## Referencias 
[Código Original](https://github.com/xnomas/PicoCTF-2021-Writeups/tree/main/keygenme-py)