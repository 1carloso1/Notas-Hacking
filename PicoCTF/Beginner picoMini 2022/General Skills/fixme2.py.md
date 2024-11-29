## Descripción
Fix the syntax error in the Python script to print the flag.

## Solución
```bash()
┌──(kali㉿kali)-[~/Downloads]
└─$ python3 fixme2.py 
  File "/home/kali/Downloads/fixme2.py", line 22
    if flag = "":
       ^^^^^^^^^
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?                        
┌──(kali㉿kali)-[~/Downloads]
└─$ emacs fixme2.py                         
┌──(kali㉿kali)-[~/Downloads]
└─$ python3 fixme2.py
That is correct! Heres your flag: picoCTF{3qu4l1ty_n0t_4551gnm3nt_4863e11b}
```

## Notas adicionales
Como se muestra en la solución, el error esta en que en un condicional if esta mal la sintaxis, ya que tiene '=' en lugar de '"= ='

Original:
```python()
if flag = "":
  print('String XOR encountered a problem, quitting.')
```
Corregido:
```python()
if flag == "":
  print('String XOR encountered a problem, quitting.')
```

## Referencias 