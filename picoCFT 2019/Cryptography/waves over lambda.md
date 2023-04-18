## Descripción
We made a lot of substitutions to encrypt this. Can you decrypt it? Connect with nc jupiter.challenges.picoctf.org 39894.

## Pistas
- Flag is not in the usual flag format

## Solución 
- Para resolver el reto, se nos da el siguiente texto encriptado:

```
kqnluors dcuc ps vqhu yxol - yucjhcnkv_ps_k_qwcu_xobego_olyxklrvhc
-------------------------------------------------------------------------------
ecrzccn hs rdcuc zos, os p dowc oxucogv sopg sqbczdcuc, rdc eqng qy rdc sco. ecspgcs dqxgpnl qhu dcours rqlcrdcu rduqhld xqnl fcupqgs qy scfouorpqn, pr dog rdc cyyckr qy botpnl hs rqxcuonr qy cokd qrdcu's vounsong cwcn kqnwpkrpqns. rdc xozvcurdc ecsr qy qxg ycxxqzsdog, eckohsc qy dps bonv vcous ong bonv wpurhcs, rdc qnxv khsdpqn qn gckt, ong zos xvpnl qn rdc qnxv uhl. rdc okkqhnronr dog euqhldr qhr oxucogv o eqa qy gqbpnqcs, ong zos rqvpnl oukdprckrhuoxxv zprd rdc eqncs. bouxqz sor kuqss-xcllcg upldr oyr, xconpnl olopnsr rdc bpiicn-bosr. dc dog shntcn kdccts, o vcxxqz kqbfxcapqn, o sruopldr eokt, on oskcrpk osfckr, ong, zprd dps oubs guqffcg, rdc foxbs qy dongs qhrzougs, ucscbexcg on pgqx. rdc gpuckrqu, sorpsypcg rdc onkdqu dog lqqg dqxg, bogc dps zov oyr ong sor gqzn obqnlsr hs. zc cakdonlcg o ycz zqugs xoipxv. oyrcuzougs rdcuc zos spxcnkc qn eqoug rdc vokdr. yqu sqbc ucosqn qu qrdcu zc gpg nqr eclpn rdor lobc qy gqbpnqcs. zc ycxr bcgprorpwc, ong ypr yqu nqrdpnl ehr fxokpg sroupnl. rdc gov zos cngpnl pn o scucnprv qy srpxx ong cajhpsprc eupxxponkc. rdc zorcu sdqnc fokpypkoxxv; rdc stv, zprdqhr o sfckt, zos o ecnpln pbbcnsprv qy hnsropncg xpldr; rdc wcuv bpsr qn rdc cssca bousd zos xptc o lohiv ong uogponr yoeupk, dhnl yuqb rdc zqqgcg upscs pnxong, ong guofpnl rdc xqz sdqucs pn gpofdonqhs yqxgs. qnxv rdc lxqqb rq rdc zcsr, euqqgpnl qwcu rdc hffcu ucokdcs, eckobc bquc sqbeuc cwcuv bpnhrc, os py onlcucg ev rdc offuqokd qy rdc shn.
```

- La descripcion nos dice que el texto esta encriptado en `substitution cipher`, por lo que lo decodificaremos con [quipqiup](https://www.quipqiup.com/), lo que nos da resumidamente esto:

```
congrats here is your flag - frequency_is_c_over_lambda_agflcgtyue
```

- Y como nos indica la flag, no tiene formato, por lo que la bandera es:

```bash()
picoCTF{frequency_is_c_over_lambda_agflcgtyue}
```

## Notas adicionales
- En criptografía, el `cifrado por sustitución` es un método de cifrado por el que unidades de texto plano son sustituidas con texto cifrado siguiendo un sistema regular; las "unidades" pueden ser una sola letra, pares de letras, tríos de letras, mezclas de lo anterior, entre otros.

## Referencias 
- [Cifrado por sustitución (Substitution cipher)](https://es.wikipedia.org/wiki/Cifrado_por_sustituci%C3%B3n)