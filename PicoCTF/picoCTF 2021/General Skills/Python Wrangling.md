## Descripción
Python scripts are invoked kind of like programs in the Terminal... Can you run this Python script using this password to get the flag?

## Solución
```bash()                       
┌──(kali㉿kali)-[~/Downloads]
└─$ ls
ende.py  flag.txt.en  pw.txt                         
┌──(kali㉿kali)-[~/Downloads]
└─$ cat pw.txt 
ac9bd0ffac9bd0ffac9bd0ffac9bd0ff                         
┌──(kali㉿kali)-[~/Downloads]
└─$ python ende.py -d flag.txt.en
Please enter the password:ac9bd0ffac9bd0ffac9bd0ffac9bd0ff
picoCTF{4p0110_1n_7h3_h0us3_ac9bd0ff}
```

## Notas adicionales
Para saber como funcionaba el script de python, lo lei con el comando <b>nano</b>, por lo que para que funcionara tenia que utilizar -d (descomprime) + el archivo dado.
## Referencias 