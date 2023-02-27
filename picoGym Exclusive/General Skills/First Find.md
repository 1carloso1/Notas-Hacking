## Descripción
Unzip this archive and find the file named 'uber-secret.txt'

## Solución
```bash()
┌──(kali㉿kali)-[~/Downloads/files]
└─$ grep -r picoCTF          
14789.txt.utf-8:brassa un picotin d'orge_. Comme depuis une demi-heure environ c'était
adequate_books/more_books/.secret/deeper_secrets/deepest_secrets/uber-secret.txt:picoCTF{f1nd_15_f457_ab443fd1}
```

## Notas adicionales
`grep -r` --recursive. Indaga en todas las carpetas que estan dentro de la ubicación, buscando el parametro dado.

## Referencias 
[GNU grep home page](https://www.gnu.org/software/grep/)