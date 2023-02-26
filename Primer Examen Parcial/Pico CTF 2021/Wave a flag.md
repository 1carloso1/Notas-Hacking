## Descripción
Can you invoke help flags for a tool or binary? [This program](https://mercury.picoctf.net/static/f95b1ee9f29d631d99073e34703a2826/warm) has extraordinarily helpful information...

## Solución
```bash()                                                               
┌──(kali㉿kali)-[~/Downloads]
└─$ ls    
warm
┌──(kali㉿kali)-[~/Downloads]
└─$ chmod +x warm      
┌──(kali㉿kali)-[~/Downloads]
└─$ ./warm
Hello user! Pass me a -h to learn what I can do!
┌──(kali㉿kali)-[~/Downloads]
└─$ ./warm -h
Oh, help? I actually dont do much, but I do have this flag here: picoCTF{b1scu1ts_4nd_gr4vy_f0668f62}
```

## Notas adicionales
Siguiendo las pistas que me da el nivel, es muy facil.

## Referencias 