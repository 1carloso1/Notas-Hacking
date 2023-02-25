cadenaHex = input("Ingrese la cadena hexadecimal: ")
cadena_ascii = bytes.fromhex(cadenaHex).decode('utf-8')
print(cadena_ascii)
