## Descripción
This vault uses for-loops and byte arrays. The source code for this vault is here: [VaultDoor3.java](https://jupiter.challenges.picoctf.org/static/a4018cec1446761cb2e8cce05db925fa/VaultDoor3.java)

## Solución
- Como podemos ver en el codigo, al ejecutar el programa se nos pide la contraseña, esta contraseña sera validada  por el metodo `checkPassword()`, este metodo debe recibir una cadena de 32 digitos, si no regresara false. Al ver el final de este metodo, podemos ver una cadena que pudiera ser la flag: `jU5t_a_sna_3lpm12g94c_u_4_m7ra41`. Pero si vemos los ciclos for de este metodo, es que se reordenan los digitos, para asi guardar la cadena re organizada en la variable `s`.
- Sabiendo esto, podemos manipular el codigo para que el metodo `checkPassword()` regrese la variable `c`, y poder imprimir la contraseña organizada. EL codigo modificado es el siguiente:

```java()
import java.util.*;

class VaultDoor3 {
    
    public static void main(String args[]) {

        VaultDoor3 vaultDoor = new VaultDoor3();
        String S = vaultDoor.checkPassword("jU5t_a_sna_3lpm12g94c_u_4_m7ra41");
        System.out.println(S);
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter vault password: ");
        String userInput = scanner.next();
	String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
                                                        /*
                                                        * 8, 31
                                                        */
	/*if (vaultDoor.checkPassword(input)) {
	    System.out.println("Access granted.");
	} else {
	    System.out.println("Access denied!");
        }*/
    }

    // Our security monitoring team has noticed some intrusions on some of the
    // less secure doors. Dr. Evil has asked me specifically to build a stronger
    // vault door to protect his Doomsday plans. I just *know* this door will
    // keep all of those nosy agents out of our business. Mwa ha!
    //
    // -Minion #2671
    public String checkPassword(String password) {
        /*if (password.length() != 32) {
            return false;
        } */
        char[] buffer = new char[32];
        int i;
        for (i=0; i<8; i++) {
            buffer[i] = password.charAt(i);
        }
        for (; i<16; i++) {
            buffer[i] = password.charAt(23-i);
        }
        for (; i<32; i+=2) {
            buffer[i] = password.charAt(46-i);
        }
        for (i=31; i>=17; i-=2) {
            buffer[i] = password.charAt(i);
        }
        String s = new String(buffer);
        return s;
        //*return s.equals("jU5t_a_sna_3lpm12g94c_u_4_m7ra41");
    }
}
```

- La flag es:

```bash()
picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_c79a21}
```

## Notas adicionales
- Esta fue mi manera de encontrar la solución, probablemente no sea la mejor ni la mas facil de hacer, pero cumple su función.
- Solo se debe analizar el codigo y enfocarnos en los metodos que analizan la flag.

## Referencias 
- Sin referencias.