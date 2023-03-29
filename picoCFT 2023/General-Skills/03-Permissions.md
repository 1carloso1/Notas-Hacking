## Descripción:
Can you read files in the root file?The system admin has provisioned an account for you on the main server:`ssh -p 55112 picoplayer@saturn.picoctf.net`Password: `Sd9KYTm5kr`Can you login and read the root file?

**Hints:**
1. What permissions do you have?

## Solución:
1. Nos conectamos al servidor (host) por ssh:

```bash
┌──(kali㉿kali)-[~]
└─$ ssh -p 55112 picoplayer@saturn.picoctf.net  
The authenticity of host '[saturn.picoctf.net]:55112 ([13.59.203.175]:55112)' can't be established.
ED25519 key fingerprint is SHA256:Km7la74G7/fztU37KiXuMDlWhxowKKAxA3TjvWy1Y0o.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[saturn.picoctf.net]:55112' (ED25519) to the list of known hosts.
picoplayer@saturn.picoctf.net's password: 
Welcome to Ubuntu 20.04.5 LTS (GNU/Linux 5.15.0-1031-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

This system has been minimized by removing packages and content that are
not required on a system that users do not log into.

To restore this content, you can run the 'unminimize' command.

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

picoplayer@challenge:~$
```

2. Vemos que en la raíz tenemos una carpeta llamada `challenge` la cual contiene una archivo llamado  `metadata.json` el cual tiene la bandera: 

```bash
picoplayer@challenge:~$ ls
picoplayer@challenge:~$ cd /
picoplayer@challenge:/$ ls
bin  boot  challenge  dev  etc  home  lib  lib32  lib64  libx32  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
picoplayer@challenge:/$ cd challenge/
picoplayer@challenge:/challenge$ ls
metadata.json
picoplayer@challenge:/challenge$ cat metadata.json 
{"flag": "picoCTF{uS1ng_v1m_3dit0r_89e9cf1a}", "username": "picoplayer", "password": "Sd9KYTm5kr"}picoplayer@challenge:/challenge$ 
picoplayer@challenge:/challenge$ 
```

### Flag: picoCTF{uS1ng_v1m_3dit0r_89e9cf1a}

## Notas adicionales:

## Referencias: