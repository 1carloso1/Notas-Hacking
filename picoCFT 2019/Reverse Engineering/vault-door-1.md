## Descripción
This vault uses some complicated arrays! I hope you can make sense of it, special agent. The source code for this vault is here: [VaultDoor1.java](https://jupiter.challenges.picoctf.org/static/87e103a8db01087de9ccf5a7a022ddf8/VaultDoor1.java)

## Solución
- Para solucionar este problema, tenemos que ver el script del codigo en java. Si eres una persona muy observadora veras que la contraseña se encuentra en el metodo checkPassword().
- Este metodo booleano devuelve `True` si se cumplen las condicionales que tiene este. Dichas condicionales incluyen que la contraseña debe medir 32 caracteres, y que cada posicion de la cadena tenga un valor especifico. Por lo que nos aprovecharemos de toda esta información que nos da este metodo para poder crear un programa corto que nos de la flag.
	- Para eso crearemos una variable llamada `canario`, que mide 32 caracteres y <b>debe de ser un valor diferente a cualquier valor de la cadena original</b> para que funcione este metodo.
	- Tambien crearemos una variable `String` que ira guardando los valores de la contraseña original
	- Crearemos un for que recorra 32 posiciones. Tambien aprovecharemos las funciones `charAt()` del metodo original. Compararemos en cada posicion que el valor de `canario` en esa posicion no sea igual que el valor de la contraeña original, y si se cumple esa condición, se guardara el valor original a la cadena vacia. Como siempre se cumplira esa condición, se iran guardando los valores hasta asi formar la contraseña que necesitamos.
	- Al tener la contraseña, solo la imprimimos con el formato de la FLAG para solo copiar y pegarla


```java()
class VaultDoor1 {

    public static void main(String args[]) {

        VaultDoor1 vaultDoor = new VaultDoor1();

        System.out.println(vaultDoor.mostrarContraseña());

    }

        public String mostrarContraseña(){

            String canario = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";

            String contraseña = "";

            for (int n = 0; n<=32; n++){

                if (n == 0){

                    if ( canario.charAt(0)  != 'd'){

                        contraseña += 'd';

                    }

                }

                else if (n == 1){

                    if ( canario.charAt(1)  != '3'){

                        contraseña += '3';

                    }

                }

                else if (n == 2){

                    if ( canario.charAt(2)  != '5'){

                        contraseña += '5';

                    }

                }

                else if (n == 3){

                    if ( canario.charAt(3)  != 'c'){

                        contraseña += 'c';

                    }

                }

                else if (n == 4){

                    if ( canario.charAt(4)  != 'r'){

                        contraseña += 'r';

                    }

                }

                else if (n == 5){

                    if ( canario.charAt(5)  != '4'){

                        contraseña += '4';

                    }

                }

                else if (n == 6){

                    if ( canario.charAt(6)  != 'm'){

                        contraseña += 'm';

                    }

                }

                else if (n == 7){

                    if ( canario.charAt(7)  != 'b'){

                        contraseña += 'b';

                    }

                }

                else if (n == 8){

                    if ( canario.charAt(8)  != 'l'){

                        contraseña += 'l';

                    }

                }

                else if (n == 9){

                    if ( canario.charAt(9)  != '3'){

                        contraseña += '3';

                    }

                }

                else if (n == 10){

                    if ( canario.charAt(10) != '_'){

                        contraseña += '_';

                    }

                }

                else if (n == 11){

                    if ( canario.charAt(11) != 't'){

                        contraseña += 't';

                    }

                }

                else if (n == 12){

                    if ( canario.charAt(12) != 'H'){

                        contraseña += 'H';

                    }

                }

                else if (n == 13){

                    if ( canario.charAt(13) != '3'){

                        contraseña += '3';

                    }

                }

                else if (n == 14){

                    if ( canario.charAt(14) != '_'){

                        contraseña += '_';

                    }

                }

                else if (n == 15){

                    if ( canario.charAt(15) != 'c'){

                        contraseña += 'c';

                    }  

                }

                else if (n == 16){

                    if ( canario.charAt(16) != 'H'){

                        contraseña += 'H';

                    }

                }

                else if (n == 17){

                    if ( canario.charAt(17) != '4'){

                        contraseña += '4';

                    }  

                }

                else if (n == 18){

                    if ( canario.charAt(18) != 'r'){

                        contraseña += 'r';

                    }

                }

                else if (n == 19){

                    if ( canario.charAt(19) != '4'){

                        contraseña += '4';

                    }  

                }

                else if (n ==20){

                    if ( canario.charAt(20) != 'c'){

                        contraseña += 'c';

                    }

                }

                else if (n == 21){

                    if ( canario.charAt(21) != 'T'){

                        contraseña += 'T';

                    }

                }

                else if (n == 22){

                    if ( canario.charAt(22) != '3'){

                        contraseña += '3';

                    }

                }

                else if (n == 23){

                    if ( canario.charAt(23) != 'r'){

                        contraseña += 'r';

                    }

                }

                else if (n == 24){

                    if ( canario.charAt(24) != '5'){

                        contraseña += '5';

                    }

                }

                else if (n == 25){

                    if ( canario.charAt(25) != '_'){

                        contraseña += '_';

                    }

                }

                else if (n == 26){

                    if ( canario.charAt(26) != 'f'){

                        contraseña += 'f';

                    }

                }

                else if (n == 27){

                    if ( canario.charAt(27) != '6'){

                        contraseña += '6';

                    }

                }

                else if (n == 28){

                    if ( canario.charAt(28) != 'd'){

                        contraseña += 'd';

                    }

                }

                else if (n == 29){

                    if ( canario.charAt(29) != 'a'){

                        contraseña += 'a';

                    }

                }

                else if (n == 30){

                    if ( canario.charAt(30) != 'f'){

                        contraseña += 'f';

                    }

                }

                else if (n == 31){

                    if ( canario.charAt(31) != '4'){

                        contraseña += '4';

                    }

                }

            }

            return "picoCTF{"+contraseña+"}";      

    }

}
```

```bash()
picoCTF{d35cr4mbl3_tH3_cH4r4cT3r5_f6daf4}
```

## Notas adicionales
- Esta fue mi manera de encontrar la solución, probablemente no sea la mejor ni la mas facil de hacer, pero cumple su función.
- - Solo se debe analizar el codigo y enfocarnos en los metodos que analizan la flag.

## Referencias 
- Sin referencias.