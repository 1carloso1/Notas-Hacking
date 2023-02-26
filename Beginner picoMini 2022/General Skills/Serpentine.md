## Descripción
Find the flag in the Python script!

## Solución
```bash()
┌──(kali㉿kali)-[~/Downloads]
└─$ python3 serpentine.py
    Y
  .-^-.
 /     \      .- ~ ~ -.
()     ()    /   _ _   `.                     _ _ _
 \_   _/    /  /     \   \                . ~  _ _  ~ .
   | |     /  /       \   \             .' .~       ~-. `.
   | |    /  /         )   )           /  /             `.`.
   \ \_ _/  /         /   /           /  /                `'
    \_ _ _.'         /   /           (  (
                    /   /             \  \
                   /   /               \  \
                  /   /                 )  )
                 (   (                 /  /
                  `.  `.             .'  /
                    `.   ~ - - - - ~   .'
                       ~ . _ _ _ _ . ~

Welcome to the serpentine encourager!


a) Print encouragement
b) Print flag
c) Quit

What would you like to do? (a/b/c) b
picoCTF{7h3_r04d_l355_7r4v3l3d_8e47d128}
a) Print encouragement
b) Print flag
c) Quit

What would you like to do? (a/b/c) c
```

## Notas adicionales
La funcion dela opción b) solo imprimia un mensaje, mas no la funcion que imprimia la flag, por lo que elimine ese mensaje y lo reemplace por la función que si daba la flag

Original:
```python()
  elif choice == 'b':
      print('\nOops! I must have misplaced the print_flag function! Check my source code!\n\n')
```

Corregido:
```python()
 elif choice == 'b':
      print(flag_enc)
```


## Referencias 