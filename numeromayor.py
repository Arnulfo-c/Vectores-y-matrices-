# Creamos un vetor vacio
numeros = []

# Solicitamos al usuario que ingrese 7 numeros 
for i in range(7):
    numero = float(input(f"Ingrese el numero {i + 1}: "))
    numeros.append(numero)

# Encontramos el numero mayor 
numero_mayor = max(numeros)

# Imprimimos el resultado 
print(f"El numero mayor ingresado es: {numero_mayor}")
