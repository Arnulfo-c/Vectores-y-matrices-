# Inicializamos el vector 
numeros = []

# Solicitamos al usuario que ingrese 6 numeros 
for i in range(6):
    numero = float(input(f"Ingrese el numero {i + 1}: "))
    numeros.append(numero)

# Invertimos el orden del vector 
numeros_invertimos = numeros[::-1]

# Imprimimos el vector original y el invertido
print(f"vector original: {numeros}")
print(f"vector invertido: {numeros_invertimos}")