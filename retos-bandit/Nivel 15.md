## Objetivo
The password for the next level can be retrieved by submitting the password of the current level to **port 30001 on localhost** using SSL encryption.

## Datos de acceso al nivel
-   Username: bandit15

-   Password: jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt

-   Host: bandit.labs.overthewire.org

-   Port: 2220

## Solución
```bash()
bandit15@bandit:~$ openssl s_client -connect localhost:30001
CONNECTED(00000003)
Can't use SSL_get_servername
depth=0 CN = localhost
verify error:num=18:self-signed certificate
verify return:1
depth=0 CN = localhost
verify error:num=10:certificate has expired
notAfter=Feb 21 06:20:29 2023 GMT
verify return:1
depth=0 CN = localhost
notAfter=Feb 21 06:20:29 2023 GMT
verify return:1
---
Certificate chain
 0 s:CN = localhost
   i:CN = localhost
   a:PKEY: rsaEncryption, 2048 (bit); sigalg: RSA-SHA1
   v:NotBefore: Feb 21 06:19:29 2023 GMT; NotAfter: Feb 21 06:20:29 2023 GMT
---
Server certificate
-----BEGIN CERTIFICATE-----
MIIDCzCCAfOgAwIBAgIEA7qUdzANBgkqhkiG9w0BAQUFADAUMRIwEAYDVQQDDAls
b2NhbGhvc3QwHhcNMjMwMjIxMDYxOTI5WhcNMjMwMjIxMDYyMDI5WjAUMRIwEAYD
VQQDDAlsb2NhbGhvc3QwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDL
vM0gZzAHdXTeD5t4ruUJo/kRs4UAodA9XcqDhNtW464W0c55RqKLp921syy3Lvjr
8Q9WkqvCFX+efShMd8XnzbT/dyRrD+cZQnSiPJ3bwDdpwqfkl9h3mb609Kb5HI6R
JgogEyuRLJI+HKtr/wXHwo1vBZ0+yaPMX6sdkd6Hu5Ra0L5Q5+E5+3F/8QgvCeVE
hDRIOrh2a7jxykb8G6+xVC6jIZY0YfrZz6LrESyQau256pqyaQPqQoUWTlitxIql
Ym2Baw7vYDxmFZrvj0FkumC6NokX6K2G9bZ0DaKR/DspPdAC4oT81SawJvsBibdN
51VI6dxBn412ZS8bS155AgMBAAGjZTBjMBQGA1UdEQQNMAuCCWxvY2FsaG9zdDBL
BglghkgBhvhCAQ0EPhY8QXV0b21hdGljYWxseSBnZW5lcmF0ZWQgYnkgTmNhdC4g
U2VlIGh0dHBzOi8vbm1hcC5vcmcvbmNhdC8uMA0GCSqGSIb3DQEBBQUAA4IBAQA9
skxWNwZbedjaVTa5yMPUZQ4Nf5/LAAMtS5Q7mzGH5tdQsTGR0Z4n4eA4hzrmzHBF
MVRL5mR9n+sM5pIrKDa6f4zIc5ObxDyN19ie+3SFASCPz9tihK8Js2V8qsR6LHV1
pfD8DSG0hZPtUuK3Mfi+nWqQUFiiTGj30mb9vlS1sSWv5PGznou1gQ3ZfrDs7B4K
ZKZrllPIVV1CrlDw2Bv8Dc432LQuZAmKAjBd6FG0OAboU/WJMTwAfVjlKMtvC8tg
DZ3djSTprq6PrXlI0utw/MsMIh69b61BRXUuDvRxhU11SNmSI8aegjVL8KuK+Euh
sSLPTocV29SY1YXOwEQi
-----END CERTIFICATE-----
subject=CN = localhost
issuer=CN = localhost
---
No client certificate CA names sent
Peer signing digest: SHA256
Peer signature type: RSA-PSS
Server Temp Key: X25519, 253 bits
---
SSL handshake has read 1339 bytes and written 373 bytes
Verification error: certificate has expired
---
New, TLSv1.3, Cipher is TLS_AES_256_GCM_SHA384
Server public key is 2048 bit
Secure Renegotiation IS NOT supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
Early data was not sent
Verify return code: 10 (certificate has expired)
---
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: E66B4B3AED2A27596F1A267C227E2FA4682A0C83216673C2E5350954EE04B077
    Session-ID-ctx: 
    Resumption PSK: ED8992B1DC10F5DFD774F3C189D5CF76A3B0ABB3D14E57CD53325C75A9644BBF7D60AD2A80DEF0DE72C1557C7909817B
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - ee ae 09 e4 56 06 6c 9e-c9 80 86 77 50 83 15 59   ....V.l....wP..Y
    0010 - 36 5a 62 06 b7 d2 64 dc-4a bf 54 ad 3a a3 19 af   6Zb...d.J.T.:...
    0020 - a5 7e e8 81 d5 2b 14 e8-d1 b8 ab 83 b1 89 5b 9a   .~...+........[.
    0030 - f4 b5 e1 b2 47 1b 7f bb-11 f7 a8 68 78 2e c6 7f   ....G......hx...
    0040 - 0f a4 ac a2 7d 5e 56 34-1c 4b 58 6f 1a d7 fe 00   ....}^V4.KXo....
    0050 - 04 e9 21 92 79 43 fe 44-7c 0a ce ad 44 5f 76 34   ..!.yC.D|...D_v4
    0060 - 2e 1f e3 55 2f 1d f6 f9-19 dc 42 d2 f4 cc 19 f9   ...U/.....B.....
    0070 - 0e f7 84 ab 99 27 7f 10-1f 1b e2 03 08 b0 0d c1   .....'..........
    0080 - 59 d4 b9 33 fa 4c 9e cd-00 95 18 79 4e 4e 59 60   Y..3.L.....yNNY`
    0090 - 6a 3a 07 3f 2a e4 58 d6-cb c0 0c 0a 10 1d b8 32   j:.?*.X........2
    00a0 - bb 4c bd f6 af ff 8d 85-8f 69 ea be 7e f2 0a b2   .L.......i..~...
    00b0 - 8e 87 87 95 b1 e4 c6 57-15 8f ad 14 7f f8 03 db   .......W........
    00c0 - fc 3e 10 b3 90 f4 4c 3c-b9 f3 8e 58 ef 1e 5c 66   .>....L<...X..\f

    Start Time: 1677007384
    Timeout   : 7200 (sec)
    Verify return code: 10 (certificate has expired)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: 316E7B9D1FE9AE1BC2D12E96A716AE67687D6230915DE43F777184820EBA4BBE
    Session-ID-ctx: 
    Resumption PSK: B014F84CDFE8C02F0DB3A18F3ED5D6E73EDAB383E15FCCF4D45FC63B4FBB73E1E1D63078E46AA25281C9BA56B633AD33
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - ee ae 09 e4 56 06 6c 9e-c9 80 86 77 50 83 15 59   ....V.l....wP..Y
    0010 - 4e 9b 56 5e 80 14 15 60-e1 de f6 0b e6 81 49 cb   N.V^...`......I.
    0020 - f6 c6 90 de 3f 45 79 3c-36 14 3a 78 02 01 32 3b   ....?Ey<6.:x..2;
    0030 - f5 87 1a 3b c9 74 af cf-ca 95 e4 69 5b 9a 3b c8   ...;.t.....i[.;.
    0040 - 80 80 c3 2d f7 29 e9 da-1d 9e ce 59 41 45 3a 11   ...-.).....YAE:.
    0050 - d9 60 3f 90 d4 a2 c8 1e-5c 85 a4 22 ac 2e 3b f2   .`?.....\.."..;.
    0060 - ff 17 22 09 61 d5 cd a0-65 cf a5 5a 61 85 40 be   ..".a...e..Za.@.
    0070 - 07 5c 60 71 d5 09 22 a8-ad 46 a4 c6 b0 3f f3 1c   .\`q.."..F...?..
    0080 - 2f 9c 73 fe 42 e4 09 9c-02 ce 13 99 16 c7 a9 3a   /.s.B..........:
    0090 - 9c bb f3 8d 6d 85 e7 18-dc 9a b8 c7 52 8e 2a 0f   ....m.......R.*.
    00a0 - f5 8d 63 17 6c d1 2e fa-20 6b 8a 43 a5 25 68 c0   ..c.l... k.C.%h.
    00b0 - 38 08 da 31 db bd 31 d3-3a 94 ff 13 83 f1 57 ba   8..1..1.:.....W.
    00c0 - 80 23 ab f6 9e 9e b0 e9-0e fe be 9b fa 47 d1 b6   .#...........G..

    Start Time: 1677007384
    Timeout   : 7200 (sec)
    Verify return code: 10 (certificate has expired)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt
Correct!
JQttfApK4SeyHwDlI9SXGR50qclOAil1

closed

```

## Notas adicionales
El comando <b>openssl s_client</b> implementa un cliente SSL/TLS genérico que se conecta a un host remoto mediante SSL/TLS. Es una herramienta de diagnóstico muy útil para servidores SSL.
Le tuve que dar la contraseña del nivel actual para recibir la contraseña del nivel 16.

## Referencias 
[Forma de resolver del maestro Carlos](https://ingsoftware.reduaz.mx/moodle/pluginfile.php/68464/mod_resource/content/2/06-retos-bandit-p3.pdf)
[Información sobre comando SSL](https://www.openssl.org/docs/man1.0.2/man1/openssl-s_client.html)