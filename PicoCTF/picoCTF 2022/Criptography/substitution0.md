## Descripción
A message has come in but it seems to be all scrambled. Luckily it seems to have the key at the beginning. Can you crack this substitution cipher?Download the message [here](https://artifacts.picoctf.net/c/152/message.txt).

## Pistas
- Try a frequency attack. An online tool might help.

## Solución
- Para resolver este reto, tenemos que analizar la descripción, ya que nos indica que esto es un `substitution cipher`.
- El reto nos da el siguiente texto:

```
DECKFMYIQJRWTZPXGNABUSOLVH 

Ifnfuxpz Wfyndzk dnpaf, oqbi d yndsf dzk abdbfwv dqn, dzk enpuyib tf bif effbwf
mnpt d ywdaa cdaf qz oiqci qb oda fzcwpafk. Qb oda d efdubqmuw acdndedfua, dzk, db
bidb bqtf, uzrzpoz bp zdbundwqaba—pm cpunaf d ynfdb xnqhf qz d acqfzbqmqc xpqzb
pm sqfo. Bifnf ofnf bop npuzk ewdcr axpba zfdn pzf flbnftqbv pm bif edcr, dzk d
wpzy pzf zfdn bif pbifn. Bif acdwfa ofnf flcffkqzywv idnk dzk ywpaav, oqbi dww bif
dxxfdndzcf pm eunzqaifk ypwk. Bif ofqyib pm bif qzafcb oda sfnv nftdnrdewf, dzk,
bdrqzy dww biqzya qzbp cpzaqkfndbqpz, Q cpuwk idnkwv ewdtf Juxqbfn mpn iqa pxqzqpz
nfaxfcbqzy qb.
Bif mwdy qa: xqcpCBM{5UE5717U710Z_3S0WU710Z_59533D2F}  
```

- Pra decodificarlo, utilice la herramienta [dcode](https://www.dcode.fr/monoalphabetic-substitution) que nos da la siguiente traducción:

```
ABCDEFGHIJKLMNOPQRSTUVWXYZ 

HERE UPON LEGRAND AROSE, WITH A GRAVE AND STATELY AIR, AND BROUGHT ME THE BEETLE FROM A GLASS CASE IN WHICH IT WAS ENCLOSED. IT WAS A BEAUTIFUL SCARABAEUS, AND, AT THAT TIME, UNKNOWN TO NATURALISTS--OF COURSE A GREAT PRIZE IN A SCIENTIFIC POINT OF VIEW. THERE WERE TWO ROUND BLACK SPOTS NEAR ONE EXTREMITY OF THE BACK, AND A LONG ONE NEAR THE OTHER. THE SCALES WERE EXCEEDINGLY HARD AND GLOSSY, WITH ALL THE APPEARANCE OF BURNISHED GOLD. THE WEIGHT OF THE INSECT WAS VERY REMARKABLE, AND, TAKING ALL THINGS INTO CONSIDERATION, I COULD HARDLY BLAME JUPITER FOR HIS OPINION RESPECTING IT. 
THE FLAG IS: PICOCTF{5UB5717U710N_3V0LU710N_59533A2E}
```

- Esto es gracias a el ataque de frecuencia que hace el algoritmo de la pagina, obtiene Alfabeto de descifrado recíproco `STCABEQZHJDXFRWOIKVMUYLPGN` a partir del dado `DECKFMYIQJRWTZPXGNABUSOLVH`.

```bash()
picoctf{5ub5717u710n_3v0lu710n_59533a2e}
```

## Notas adicionales
- Sin notas adicionales

## Referencias
- Sin referencias