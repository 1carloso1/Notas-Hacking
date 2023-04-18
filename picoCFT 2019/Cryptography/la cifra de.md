## Descripción
I found this cipher in an old book. Can you figure out what it says? Connect with nc jupiter.challenges.picoctf.org 5726.

## Pistas
- There are tools that make this easy.
- Perhaps looking at history will help

## Solución
- Para resolver este reto, se nos da el siguinete texto:

```
Encrypted message:
Ne iy nytkwpsznyg nth it mtsztcy vjzprj zfzjy rkhpibj nrkitt ltc tnnygy ysee itd tte cxjltk

Ifrosr tnj noawde uk siyyzre, yse Bnretèwp Cousex mls hjpn xjtnbjytki xatd eisjd

Iz bls lfwskqj azycihzeej yz Brftsk ip Volpnèxj ls oy hay tcimnyarqj dkxnrogpd os 1553 my Mnzvgs Mazytszf Merqlsu ny hox moup Wa inqrg ipl. Ynr. Gotgat Gltzndtg Gplrfdo 

Ltc tnj tmvqpmkseaznzn uk ehox nivmpr g ylbrj ts ltcmki my yqtdosr tnj wocjc hgqq ol fy oxitngwj arusahje fuw ln guaaxjytrd catizm tzxbkw zf vqlckx hizm ceyupcz yz tnj fpvjc hgqqpohzCZK{m311a50_0x_a1rn3x3_h1ah3x6kp60egf}

Ehk ktryy herq-ooizxetypd jjdcxnatoty ol f aordllvmlbkytc inahkw socjgex, bls sfoe gwzuti 1467 my Rjzn Hfetoxea Gqmexyt.

Tnj Gimjyèrk Htpnjc iy ysexjqoxj dosjeisjd cgqwej yse Gqmexyt Doxn ox Fwbkwei Inahkw.

Tn 1508, Ptsatsps Zwttnjxiax tnbjytki ehk xz-cgqwej ylbaql rkhea (g rltxni ol xsilypd gqahggpty) ysaz bzuri wazjc bk f nroytcgq nosuznkse ol yse Bnretèwp Cousex.

Gplrfdo’y xpcuso butvlky lpvjlrki tn 1555 gx l cuseitzltoty ol yse lncsz. Yse rthex mllbjd ol yse gqahggpty fce tth snnqtki cemzwaxqj, bay ehk fwpnfmezx lnj yse osoed qptzjcs gwp mocpd hd xegsd ol f xnkrznoh vee usrgxp, wnnnh ify bk itfljcety hizm paim noxwpsvtydkse.
```

- Por lo que el mensaje da a entender que es un cifrado Vigenere, por lo que utilizaremos el decodificador [cryptii.](https://cryptii.com/pipes/vigenere-cipher) donde la palabra clave sera `flag` ya que sabemos que es una palabra que aparecera si o si. la flag que nos da el descifrado es:

```bash()
picoCTF{b311a50_0r_v1gn3r3_c1ph3r6fe60eaa}
```

## Notas adicionales
- El cifrado Vigenère es un **cifrado basado en diferentes series de caracteres o letras del cifrado César formando estos caracteres una tabla, llamada tabla de Vigenère, que se usa como clave**. El cifrado de Vigenère es un cifrado polialfabético y de sustitución. El cifrado Vigenère se ha reinventado muchas veces.

## Referencias 
- [El cifrado de Vigenère](https://www.ugr.es/~anillos/textos/pdf/2011/EXPO-1.Criptografia/02a11.htm#:~:text=El%20cifrado%20Vigen%C3%A8re%20es%20un,se%20ha%20reinventado%20muchas%20veces.)