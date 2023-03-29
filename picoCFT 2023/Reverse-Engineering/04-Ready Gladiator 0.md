## Descripción:
Can you make a CoreWars warrior that always loses, no ties?Your opponent is the Imp. The source is available [here](https://artifacts.picoctf.net/c/311/imp.red). If you wanted to pit the Imp against himself, you could download the Imp and connect to the CoreWars server like this:`nc saturn.picoctf.net 54631 < imp.red`

**Hints:**
1. CoreWars is a well-established game with a lot of docs and strategy
2. Experiment with input to the CoreWars handler or create a self-defeating bot

## Solución:

```bash
┌──(kali㉿kali)-[~/picoCTF-2023/Reverse-Engineering/Ready_Gladiator0]
└─$ ls                                   
imp.red
                                                                                                                                                             
┌──(kali㉿kali)-[~/picoCTF-2023/Reverse-Engineering/Ready_Gladiator0]
└─$ cat imp.red                          
;redcode
;name Imp Ex
;assert 1
mov 0, 1
end
                                                                                                                                                             
┌──(kali㉿kali)-[~/picoCTF-2023/Reverse-Engineering/Ready_Gladiator0]
└─$ nc saturn.picoctf.net 54631 < imp.red
;redcode
;name Imp Ex
;assert 1
mov 0, 1
end
Submit your warrior: (enter 'end' when done)

Warrior1:
;redcode
;name Imp Ex
;assert 1
mov 0, 1
end

Rounds: 100
Warrior 1 wins: 0
Warrior 2 wins: 0
Ties: 100
Try again. Your warrior (warrior 1) must lose all rounds, no ties.
                                                                                                                                                             
┌──(kali㉿kali)-[~/picoCTF-2023/Reverse-Engineering/Ready_Gladiator0]
└─$ nano imp.red                         
                                                                                                                                                             
┌──(kali㉿kali)-[~/picoCTF-2023/Reverse-Engineering/Ready_Gladiator0]
└─$ nc saturn.picoctf.net 54631 < imp.red
;redcode
;name Imp Ex
;assert 1
mov 0, 0
end
Submit your warrior: (enter 'end' when done)

Warrior1:
;redcode
;name Imp Ex
;assert 1
mov 0, 0
end

Rounds: 100
Warrior 1 wins: 0
Warrior 2 wins: 100
Ties: 0
You did it!
picoCTF{h3r0_t0_z3r0_4m1r1gh7_e476d4cf}
                                                                                                                                                             
┌──(kali㉿kali)-[~/picoCTF-2023/Reverse-Engineering/Ready_Gladiator0]
└─$ 
```

### Flag: picoCTF{h3r0_t0_z3r0_4m1r1gh7_e476d4cf}

## Notas adicionales:
| Comando | Descripción |
| --- | --- |

## Referencias: