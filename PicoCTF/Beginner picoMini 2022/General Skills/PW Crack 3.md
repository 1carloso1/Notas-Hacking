## Descripción
Can you crack the password to get the flag? Download the password checker here and you'll need the encrypted flag and the hash in the same directory too. There are 7 potential passwords with 1 being correct. You can find these by examining the password checker script.

## Solución
```bash()
┌──(kali㉿kali)-[~/Downloads]
└─$ emacs level3.py                                                    
┌──(kali㉿kali)-[~/Downloads]
└─$ echo '["8799", "d3ab", "1ea2", "acaf", "2295", "a9de", "6f3d"]' > psswds.txt                                                             
┌──(kali㉿kali)-[~/Downloads]
└─$ cat psswds.txt 
["8799", "d3ab", "1ea2", "acaf", "2295", "a9de", "6f3d"]                                                           
┌──(kali㉿kali)-[~/Downloads]
└─$ python3 level3.py
Please enter correct password for flag: 8799
That password is incorrect                                                            
┌──(kali㉿kali)-[~/Downloads]
└─$ python3 level3.py
Please enter correct password for flag: d3ab
That password is incorrect                                                             
┌──(kali㉿kali)-[~/Downloads]
└─$ python3 level3.py    
Please enter correct password for flag: 1ea2
Welcome back... your flag, user:
picoCTF{m45h_fl1ng1ng_6f98a49f}
```

## Notas adicionales
Para obtener la flag, tuve que entrar al codigo del porgrama level3.py para encontrar una lista con las contraseñas, por lo que tome esas contraseñas y las guarde en un archivo de texto, para asi probar una por una para llar la correcta, ene ste caso fue la contraseña del indice 2 de la lista.

## Referencias 
