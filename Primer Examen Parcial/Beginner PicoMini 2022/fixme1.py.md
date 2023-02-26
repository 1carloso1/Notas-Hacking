## Descripción
Fix the syntax error in this Python script to print the flag.

## Solución
```bash()
┌──(kali㉿kali)-[~/Downloads]
└─$ python3 fixme1.py 
  File "/home/kali/Downloads/fixme1.py", line 20
    print('That is correct! Here\'s your flag: ' + flag)
IndentationError: unexpected indent

──(kali㉿kali)-[~/Downloads]
└─$ emacs fixme1.py 

┌──(kali㉿kali)-[~/Downloads]
└─$ python3 fixme1.py
That is correct! Heres your flag: picoCTF{1nd3nt1ty_cr1515_6a476c8f}

```

## Notas adicionales
Solo estaba mal identada la ultima linea que imprimia la flag, por eso no la muestra en el codigo original 

Original:
```python()
flag = str_xor(flag_enc, 'enkidu')
	print('That is correct! Here\'s your flag: ' + flag)
```
Corregido:
```python()
flag = str_xor(flag_enc, 'enkidu')
print('That is correct! Here\'s your flag: ' + flag)
```


## Referencias