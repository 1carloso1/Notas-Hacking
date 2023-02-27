## Descripción
Unzip this archive and find the flag.

## Solución
```bash()
┌──(kali㉿kali)-[~/Downloads/big-zip-files]
└─$ grep -r picoCTF 
folder_pmbymkjcya/folder_cawigcwvgv/folder_ltdayfmktr/folder_fnpfclfyee/whzxrpivpqld.txt:information on the record will last a billion years. Genes and brains and books encode picoCTF{gr3p_15_m4g1c_ef8790dc}

```

## Notas adicionales
`grep -r` --recursive. Indaga en todas las carpetas que estan dentro de la ubicación, buscando el parametro dado.

## Referencias 
[GNU grep home page](https://www.gnu.org/software/grep/)