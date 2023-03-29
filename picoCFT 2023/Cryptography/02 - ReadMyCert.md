## Descripción:
How about we take you on an adventure on exploring certificate signing requests Take a look at this CSR file here.


**Hints:**
1. Download the certificate signing request and try to read it.

## Solución:
- Para obtener la solucion de este reto, se descargo el archivo `readmycert.csr`. Al leerlo nos da lo siguiente:

```bash
-----BEGIN CERTIFICATE REQUEST-----
MIICpzCCAY8CAQAwPDEmMCQGA1UEAwwdcGljb0NURntyZWFkX215Y2VydF9jZGE4
Y2IyNn0xEjAQBgNVBCkMCWN0ZlBsYXllcjCCASIwDQYJKoZIhvcNAQEBBQADggEP
ADCCAQoCggEBAKREZd5ePwEHGldid+0ZckMNH1jZPoVtIiPLZGzSELAuHgAvmP4a
bvB1KQ3hhgpuElom+8MXwstx5HlUrNzRoLSDa28KHiSg+XddpwtnQwxI5K0tappd
BLXOwHGcHSA4oFdIPVzxZh9XbF9Rogd0aYo7gfAvtzJtgFK6W7UhP5wNZnkfnpDw
24SMUJ4wOe1UX5wu3ugpPkGYMF+RyL0NgOndilLtJLapq4IRkkkBLHD2PJ1hGmis
yKSNfiWStJnrB7DWL1sUo0VhdndXXICH6P1Ve3MfEHfbxXJBx+4MWimqLGlZv33a
+yC//XeIZk/xXr2XzNvE3xmzMqEh+CO3lwECAwEAAaAmMCQGCSqGSIb3DQEJDjEX
MBUwEwYDVR0lBAwwCgYIKwYBBQUHAwIwDQYJKoZIhvcNAQELBQADggEBADmCw2EZ
ED4Ggik4IvwDaPncO7zZ6NSbLdVfRAoqtHMCKMlwxyCHOws82PiEeOAYjtN2Olma
J6LSi5bJBcNkiZhE9Kf+8fiNphCq0WPNRxJ20cPLIEOD2bZLuNAkgfqq3OmXVzkP
Fb8zP3eHUBo7Rey3zO070dXPzyxvg68iyI8cGZbPartt3GFXsE4zywRiPQP8Abtf
LTTpxcOcuZVktW6BZQ9pG5xlTGaE5opmI0vkIs3wFLeiItF5BlQ+VJnYzwHmdCST
iRfeo+VV6YajaLYVyItUnIwf7HUUq7CJK7bZCX3wl9LYwwwq16KEkPN0kNmydnyj
t0SpVnQ18utRsf0=
-----END CERTIFICATE REQUEST-----

```

- Para obtener la flag, hay que utilizar un decodificador de CSR, por lo que se utilizara la pagina [Decodificador CSR](https://es.rakko.tools/tools/42/). Al decodificar el texto, nos dara la flag. 
### Flag: picoCTF{read_mycert_cda8cb26}

## Notas adicionales:

| Abreviación | Descripción |
| --- | --- |
| CSR | Solicitud de firma de certificado |

## Referencias: