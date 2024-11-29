import codecs

cadenaBinaria = input("Ingrese la cadena binaria: ")
listaBin =[] 
cadenaBin = ""

#Con split se guardaran en la lista la cadena de numeros binarios
listaBin = cadenaBinaria.split()

#Con el for recorreremos cada posicion de la lista para obtener la letra de cada posicion
for i in listaBin:
    #Aqui el numero binario pasara a ser hexadecimal
    hexstr = f'{int(i, 2):X}'
    #Aqui con la posicion en hexadecimal obtendremos el valor ASCII
    binary_str = codecs.decode(hexstr, "hex")
    #Aqui se le quitan los '' a los simbolos y se suman a la cadena de  texto
    cadenaBin = cadenaBin + str(binary_str,'utf-8')

#Se muestra la traduccion de la cadena binarias
print("word: "+cadenaBin+"\n")

cadenaDecimal = input("Ingrese la cadena octal: ")
cadenaOct = ""
listaOct =[] 

#Con split se guardaran en la lista la cadena de numeros decimales
listaOct = cadenaDecimal.split()

#Con el for recorreremos cada posicion de la lista para obtener la letra de cada posicion
for j in listaOct:
    #Aqui el numero octal a numero decimal
    j = int(j,8)
    #Aqui el numero decimal a valor ASCII
    letra = chr(int(j))
    #Aqui  se suman a la cadena de  texto
    cadenaOct = cadenaOct + letra
   

#Se muestra la traduccion de la cadena octal
print("word: "+cadenaOct+"\n")

cadenaHex = input("Ingrese la cadena hexadecimal: ")
#Aqui se convierte la cadena hexadecimal a ASCII directamente
cadena_ascii = bytes.fromhex(cadenaHex).decode('utf-8')
#Se muestra la traduccion de la cadena hexadecimal
print("word: "+cadena_ascii)