## Descripción
Can you solve this?What two positive numbers can make this possible: `n1 > n1 + n2 OR n2 > n1 + n2`Enter them here `nc saturn.picoctf.net 49265`. [Source](https://artifacts.picoctf.net/c/456/flag.c)

## Pistas
- Integer overflow
- Not necessarily a math problem

## Solución
- Se nos da el siguinete codigo:

```
#include <stdio.h>
#include <stdlib.h>

static int addIntOvf(int result, int a, int b) {
    result = a + b;
    if(a > 0 && b > 0 && result < 0)
        return -1;
    if(a < 0 && b < 0 && result > 0)
        return -1;
    return 0;
}

int main() {
    int num1, num2, sum;
    FILE *flag;
    char c;

    printf("n1 > n1 + n2 OR n2 > n1 + n2 \n");
    fflush(stdout);
    printf("What two positive numbers can make this possible: \n");
    fflush(stdout);
    
    if (scanf("%d", &num1) && scanf("%d", &num2)) {
        printf("You entered %d and %d\n", num1, num2);
        fflush(stdout);
        sum = num1 + num2;
        if (addIntOvf(sum, num1, num2) == 0) {
            printf("No overflow\n");
            fflush(stdout);
            exit(0);
        } else if (addIntOvf(sum, num1, num2) == -1) {
            printf("You have an integer overflow\n");
            fflush(stdout);
        }

        if (num1 > 0 || num2 > 0) {
            flag = fopen("flag.txt","r");
            if(flag == NULL){
                printf("flag not found: please run this on the server\n");
                fflush(stdout);
                exit(0);
            }
            char buf[60];
            fgets(buf, 59, flag);
            printf("YOUR FLAG IS: %s\n", buf);
            fflush(stdout);
            exit(0);
        }
    }
    return 0;
}
```

- El programa solicita dos números enteros y los suma, si la suma es menor que cualquiera de los valores de entrada, se elimina la bandera. Este es un simple desbordamiento de enteros.
	- Los valores de entrada y la suma se manejan como enteros con signo.
	- El valor entero máximo con signo es 2.147.483.647.
-  Seleccione dos números que desborden el rango positivo máximo de un entero con signo cuando se suman, el primero muy cerca (o igual) del máximo, el segundo lo suficiente como para desbordarse, de modo que la suma sea menor que el primer número.

```
$ echo -e "2147483647\n1" | nc saturn.picoctf.net 57395
n1 > n1 + n2 OR n2 > n1 + n2 
What two positive numbers can make this possible: 
You entered 2147483647 and 1
You have an integer overflow
YOUR FLAG IS: picoCTF{Tw0_Sum_Integer_Bu773R_0v3rfl0w_ccd078bd}
```

## Notas adicionales
- En la programación informática, se produce un desbordamiento de enteros cuando una operación aritmética intenta crear un valor numérico que está fuera del rango que se puede representar con un número determinado de dígitos

## Referencias 
- Sin referencias