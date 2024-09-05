# Crear un vector vacio 
numero = []

# Pedir al usuario que ingrese 5 numero
for i in range(5):
    num = float(input(f"Ingrese el numero {i + 1}: "))
    numero.append(num)

# Calcular la suma de los elementos 
suma = sum(numero)

# Calcular el elemento
elemento = suma / len(numero)

# Mostrar el resltado 
print(f"La suma de los numeros ingresados es: {suma}")
print(f"El elemento de los numeros ingresados es: {elemento}")
