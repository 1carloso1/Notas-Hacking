## Descripción:
Can you make sense of this file?Download the file [here](https://artifacts.picoctf.net/c/294/enc_flag).

**Hints:**
1.Multiple decoding is always good.

## Solución:

```bash
┌──(kali㉿kali)-[~/picoCTF-2023/generalSkills/repetitions]
└─$ ls
enc_flag
                                                                                                                                                             
┌──(kali㉿kali)-[~/picoCTF-2023/generalSkills/repetitions]
└─$ cat enc_flag             
VmpGU1EyRXlUWGxTYmxKVVYwZFNWbGxyV21GV1JteDBUbFpPYWxKdFVsaFpWVlUxWVZaS1ZWWnVh
RmRXZWtab1dWWmtSMk5yTlZWWApiVVpUVm10d1VWZFdVa2RpYlZaWFZtNVdVZ3BpU0VKeldWUkNk
MlZXVlhoWGJYQk9VbFJXU0ZkcVRuTldaM0JZVWpGS2VWWkdaSGRXCk1sWnpWV3hhVm1KRk5XOVVW
VkpEVGxaYVdFMVhSbFZhTTBKWVZGVm9RMDFHV1hoWGJFNW9DbUpXUmpOVVZsWlhWakpHZEdWRlZs
aGkKYlRrelZERldUMkpzUWxWTlJYTkxDZz09Cg==
                                                                                                                                                             
┌──(kali㉿kali)-[~/picoCTF-2023/generalSkills/repetitions]
└─$ cat enc_flag | base64 -d 
VjFSQ2EyTXlSblJUV0dSVllrWmFWRmx0TlZOalJtUlhZVVU1YVZKVVZuaFdWekZoWVZkR2NrNVVX
bUZTVmtwUVdWUkdibVZXVm5WUgpiSEJzWVRCd2VWVXhXbXBOUlRWSFdqTnNWZ3BYUjFKeVZGZHdW
MlZzVWxaVmJFNW9UVVJDTlZaWE1XRlVaM0JYVFVoQ01GWXhXbE5oCmJWRjNUVlZXVjJGdGVFVlhi
bTkzVDFWT2JsQlVNRXNLCg==
                                                                                                                                                             
┌──(kali㉿kali)-[~/picoCTF-2023/generalSkills/repetitions]
└─$ cat enc_flag | base64 -d | base64 -d
V1RCa2MyRnRTWGRVYkZaVFltNVNjRmRXYUU5aVJUVnhWVzFhYVdGck5UWmFSVkpQWVRGbmVWVnVR
bHBsYTBweVUxWmpNRTVHWjNsVgpXR1JyVFdwV2VsUlZVbE5oTURCNVZXMWFUZ3BXTUhCMFYxWlNh
bVF3TVVWV2FteEVXbm93T1VOblBUMEsK
                                                                                                                                                             
┌──(kali㉿kali)-[~/picoCTF-2023/generalSkills/repetitions]
└─$ cat enc_flag | base64 -d | base64 -d | base64 -d
WTBkc2FtSXdUbFZTYm5ScFdWaE9iRTVxVW1aaWFrNTZaRVJPYTFneVVuQlpla0pyU1ZjME5GZ3lV
WGRrTWpWelRVUlNhMDB5VW1aTgpWMHB0V1ZSamQwMUVWamxEWnowOUNnPT0K
                                                                                                                                                             
┌──(kali㉿kali)-[~/picoCTF-2023/generalSkills/repetitions]
└─$ cat enc_flag | base64 -d | base64 -d | base64 -d | base64 -d
Y0dsamIwTlVSbnRpWVhObE5qUmZiak56ZEROa1gyUnBZekJrSVc0NFgyUXdkMjVzTURSa00yUmZN
V0ptWVRjd01EVjlDZz09Cg==
                                                                                                                                                             
┌──(kali㉿kali)-[~/picoCTF-2023/generalSkills/repetitions]
└─$ cat enc_flag | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d
cGljb0NURntiYXNlNjRfbjNzdDNkX2RpYzBkIW44X2Qwd25sMDRkM2RfMWJmYTcwMDV9Cg==
                                                                                                                                                             
┌──(kali㉿kali)-[~/picoCTF-2023/generalSkills/repetitions]
└─$ cat enc_flag | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d
picoCTF{base64_n3st3d_dic0d!n8_d0wnl04d3d_1bfa7005}
                                                                                                                                                             
┌──(kali㉿kali)-[~/picoCTF-2023/generalSkills/repetitions]
└─$
```

### Flag: picoCTF{base64_n3st3d_dic0d!n8_d0wnl04d3d_1bfa7005}

## Notas adicionales:
| Comando | Descripción |
| --- | --- |
| base64 | El **comando base64** permite **codificar y descodificar cadenas de caracteres desde línea de comandos GNU/Linux**, en este caso desde BASH. |

## Referencias:
- https://es.wikipedia.org/wiki/Base64