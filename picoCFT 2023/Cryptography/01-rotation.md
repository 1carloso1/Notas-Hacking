## Descripción:
You will find the flag after decrypting this fileDownload the encrypted flag [here](https://artifacts.picoctf.net/c/448/encrypted.txt).

**Hints:**
1. Sometimes rotation is right

## Solución:
1. En este reto nos dan una mensaje encriptado: 

```bash
┌──(kali㉿kali)-[~/picoCTF-2023/Cryptography/rotation]
└─$ ls         
encrypted.txt
                                                                                                                                                             
┌──(kali㉿kali)-[~/picoCTF-2023/Cryptography/rotation]
└─$ cat encrypted.txt                                                                   
xqkwKBN{z0bib1wv_l3kzgxb3l_jln2n252}
                                                                                                                                                             
┌──(kali㉿kali)-[~/picoCTF-2023/Cryptography/rotation]
└─$
```

2. Con ayuda de la herramienta [CyberChef ](https://gchq.github.io/CyberChef/) identificamos que el mensaje esta encriptado usando ROT18 por lo tanto al aplicar el algoritmo obtenemos la bandera.

### Flag: picoCTF{r0tat1on_d3crypt3d_bdf2f252}

## Notas adicionales:

## Referencias:
- https://gchq.github.io/CyberChef/