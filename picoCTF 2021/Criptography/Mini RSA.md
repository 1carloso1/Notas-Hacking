## Descripción
What happens if you have a small exponent? There is a twist though, we padded the plaintext so that (M ** e) is just barely larger than N. Let's decrypt this: [ciphertext](https://mercury.picoctf.net/static/a24cf907007a19dbf30310acad0df9e5/ciphertext)

## Pistas
- RSA [tutorial](https://en.wikipedia.org/wiki/RSA_(cryptosystem))
- How could having too small of an `e` affect the security of this key?
- Make sure you don't lose precision, the numbers are pretty big (besides the `e` value)
- You shouldn't have to make _too_ many guesses
- `pico` is in the flag, but not at the beginning

## Solución
- En RSA, el cifrado se realiza elevando un mensaje original `m` a la potencia del exponente de cifrado `e` y luego tomando el residuo del resultado dividido por el módulo `n`. En otras palabras, el mensaje cifrado `c` se calcula como: `c = (m^e) mod n`.
- Para descifrar un mensaje cifrado, normalmente se necesita conocer el exponente de descifrado `d`, que es un número que se calcula a partir del exponente de cifrado `e` y otros parámetros del sistema de cifrado. Sin embargo, si el exponente de cifrado es pequeño, es posible encontrar la raíz `e`-ésima del mensaje cifrado `c` y obtener el mensaje original `m`.
- Podemos despejar `m` al reescribir la formula `c = (m^e) mod n` a `m^e = tn + c` para poder despejar `m`: `m = iroot(tn+c, e)`.
- Con esto, cree un programa en python que resolviera este problema.

```python()
from gmpy2 import iroot
from Crypto.Util.number import long_to_bytes

n = 1615765684321463054078226051959887884233678317734892901740763321135213636796075462401950274602405095138589898087428337758445013281488966866073355710771864671726991918706558071231266976427184673800225254531695928541272546385146495736420261815693810544589811104967829354461491178200126099661909654163542661541699404839644035177445092988952614918424317082380174383819025585076206641993479326576180793544321194357018916215113009742654408597083724508169216182008449693917227497813165444372201517541788989925461711067825681947947471001390843774746442699739386923285801022685451221261010798837646928092277556198145662924691803032880040492762442561497760689933601781401617086600593482127465655390841361154025890679757514060456103104199255917164678161972735858939464790960448345988941481499050248673128656508055285037090026439683847266536283160142071643015434813473463469733112182328678706702116054036618277506997666534567846763938692335069955755244438415377933440029498378955355877502743215305768814857864433151287
e = 3
c = 1220012318588871886132524757898884422174534558055593713309088304910273991073554732659977133980685370899257850121970812405700793710546674062154237544840177616746805668666317481140872605653768484867292138139949076102907399831998827567645230986345455915692863094364797526497302082734955903755050638155202890599808145893251774383242888588567652079502880522005531571120463301333725071534050137246298274874319432561063978068140428652193294702808687000503934999928337234367205234422580586283326017530708854836817980318398277272759022724136418545105867685463283579824831916699431331460258806680372323026200534791012439563034432826050072742892112790177234284090476467119938191076883854821999876464545771711445501514467804193760659882386680300508589975451301720477703627085437101600726487172968870448635983769708507451946168500510817590720157574816563284526466526806699820426206566718022595284382939272542309819250701217431454132436646725890151031992160610219312035760562959174778547776304922277751548955049884940378

for t in range(10000):
    m, is_true_root  = iroot(i*n + c,e)
    if is_true_root:
        print(f"t: {i}")
        print(long_to_bytes(m))
        break
```

- La salida que nos da es :

```bash()
t: 3533
b'                                                                                                        picoCTF{e_sh0u1d_b3_lArg3r_0b39bbb1}'
```

## Notas adicionales
- En resumen, este código intenta encontrar el mensaje original cifrado con RSA mediante un ataque de texto claro elegido, utilizando el exponente de cifrado pequeño `e` y la función `gmpy2.iroot`.
- En la línea `m, is_true_root = iroot(t*n + c, e)`, la variable `m` se asigna al resultado de la raíz `e`-ésima de `t*n + c`, mientras que la variable `is_true_root` se asigna al segundo elemento de la tupla que devuelve la función `iroot`.
- En resumen, la línea `m, is_true_root = iroot(t*n + c,e)` calcula la raíz `e`-ésima de un número construido a partir de `t`, `n` y `c`, y asigna el resultado a la variable `m`, mientras que la variable `is_true_root` se utiliza para indicar si el resultado es una raíz entera exacta.

## Referencias
- Sin referencias.