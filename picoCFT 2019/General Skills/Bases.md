## Descripción
What does this `bDNhcm5fdGgzX3IwcDM1` mean? I think it has something to do with bases.

## Solución
```bash()
┌──(kali㉿kali)-[~]
└─$ echo 'bDNhcm5fdGgzX3IwcDM1' as > msj.txt 
┌──(kali㉿kali)-[~]
└─$ base64 -d msj.txt             
l3arn_th3_r0p35 base64: invalid input

picoCTF{l3arn_th3_r0p35}
```

## Notas adicionales
<b>Base64</b>: codificar o decodificar ARCHIVO, o entrada estándar, a salida estándar.
<b>-d, --decode</b>:  decodifica los datos

## Referencias 
[Documentación base64](https://www.gnu.org/software/coreutils/base64)
