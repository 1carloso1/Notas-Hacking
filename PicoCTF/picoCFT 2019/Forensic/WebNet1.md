## Descripción
We found this packet capture and key. Recover the flag.

## Pistas
- Try using a tool like Wireshark.
- How can you decrypt the TLS stream?

## Solución
- Para resolver este reto, se nos da un archivo `capture-pcap` que abriremos con wireshark y un archivo `picopico.key` que nos ayudara despues con el reto.
- El primer paso para resolver este reto es seguir el flujo de TCP, y nos muestra que los datos están encriptados (excepto algunas partes durante el protocolo de enlace, como el certificado)
- Si inspeccionamos ese handshake de manos, más precisamente, observando el paquete Server Hello, vemos que se seleccionó un conjunto de cifrado que se basa en RSA y AES.
- Wireshark puede descifrar los datos cifrados con este conjunto de cifrado cuando proporcionamos la clave RSA privada del servidor. Esto se debe a que, en este ejemplo, Wireshark necesita descifrar el secreto premaestro enviado por el cliente al servidor. Este secreto maestro previo se cifra con la clave RSA pública del servidor. Por lo que aqui es donde el archivo `picopico.key` nos caera de perlas.
- Para poder agregar esta clave, iremos a `edit/preferences`, despues seleccionaremos el protocolo `TLS` y editaremos la `RSA Keys list` agregandole el arhcivo que contiene la clave. 
- Cuando cierre los cuadros de diálogo y la pantalla principal recupere el foco, los datos TLS se descifrarán.
- Cuando seleccionamos TCP, todavía tenemos datos encriptados, pero cuando seleccionamos TLS, ahora podemos ver los datos descifrados:

```bash()
GET /starter-template.css HTTP/1.1
Host: ec2-18-223-184-200.us-east-2.compute.amazonaws.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: text/css,*/*;q=0.1
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Referer: https://ec2-18-223-184-200.us-east-2.compute.amazonaws.com/second.html
Pragma: no-cache
Cache-Control: no-cache

HTTP/1.1 200 OK
Date: Fri, 23 Aug 2019 16:27:04 GMT
Server: Apache/2.4.29 (Ubuntu)
Last-Modified: Mon, 12 Aug 2019 16:47:05 GMT
ETag: "62-58fee462bf227-gzip"
Accept-Ranges: bytes
Vary: Accept-Encoding
Content-Encoding: gzip
Pico-Flag: picoCTF{this.is.not.your.flag.anymore}
Content-Length: 100
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/css

..........K.O.T..RP(HLI..K.-./.R0-J......+.I,*I-.-I.-.I,IEVj.`.T.`..Q..P.ZQ......g.......2.. ...b...GET /vulture.jpg HTTP/1.1
Host: ec2-18-223-184-200.us-east-2.compute.amazonaws.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: image/webp,*/*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Referer: https://ec2-18-223-184-200.us-east-2.compute.amazonaws.com/second.html
Pragma: no-cache
Cache-Control: no-cache

HTTP/1.1 200 OK
Date: Fri, 23 Aug 2019 16:27:04 GMT
Server: Apache/2.4.29 (Ubuntu)
Last-Modified: Fri, 23 Aug 2019 16:26:33 GMT
ETag: "112fb-590cb44f2cbe6"
Accept-Ranges: bytes
Content-Length: 70395
Pico-Flag: picoCTF{this.is.not.your.flag.anymore}
Keep-Alive: timeout=5, max=99
Connection: Keep-Alive
Content-Type: image/jpeg

......JFIF..............Exif..MM.*.................J...........R.(...........;.........Z................................picoCTF{honey.roasted.peanuts}......ICC_PROFILE.......lcms....mntrRGB XYZ .........).9acspAPPL...................................-lcms...............................................
```

- Donde podemos ver que hay dos flags `picoCTF{this.is.not.your.flag.anymore}` y `picoCTF{honey.roasted.peanuts}`, y probando las dos la correcta es:

```bash()
picoCTF{honey.roasted.peanuts}
```

## Notas adicionales
- Este reto es idéntico a WebNet0
- Pude resolver este reto viendo un tutorial general de como desencriptar el TLS stream

## Referencias 
- [Tutorial para desencriptar TLS stream](https://blog.didierstevens.com/2020/12/14/decrypting-tls-streams-with-wireshark-part-1/)