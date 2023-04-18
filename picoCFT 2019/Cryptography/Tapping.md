## Descripción
Theres tapping coming in from the wires. What's it saying nc jupiter.challenges.picoctf.org 48247.

## Pistas
- What kind of encoding uses dashes and dots?
- The flag is in the format PICOCTF{}

## Solución
- Al ver el mensaje `.--. .. -.-. --- -.-. - ..-. { -- ----- .-. ... ...-- -.-. ----- -.. ...-- .---- ... ..-. ..- -. .---- ..--- -.... .---- ....- ...-- ---.. .---- ---.. .---- }` nos podemos dar cuenta que estaq en codigo morse.
- Por lo que usando un decodificador [Morse Code Translator](https://www.dcode.fr/morse-code) solo para lo que esta dentro de las llaves ` -- ----- .-. ... ...-- -.-. ----- -.. ...-- .---- ... ..-. ..- -. .---- ..--- -.... .---- ....- ...-- ---.. .---- ---.. .---- ` nos da la siguiente traducción: `M0RS3C0D31SFUN1261438181`. Por lo que la flag es: 

```bash()
picoCTF{M0RS3C0D31SFUN1261438181}
```

## Notas adicionales
- El código morse, también conocido como alfabeto morse o clave morse es un sistema de representación de letras y números mediante señales emitidas de forma intermitente.

## Referencias 
- [Codigo Morse](https://es.wikipedia.org/wiki/C%C3%B3digo_morse)