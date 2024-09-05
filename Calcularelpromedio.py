# Crear un vector vacio 
numeros = []

# Pedir al usuario que ingrese 10 numeros
for i in range(10):
    num = float(input(f"Ingrese el numero {i + 1}: "))
    numeros.append(num) 

# Calcular la suma de los elementos
suma = sum(numeros)

#Calcular el primedio
promedio = suma / len(numeros)

#Mostrar el resultado
print(f"La suma de los numeros ingresados es: {suma}")
print(f"El promedio de los numeros ingresados es: {promedio}")
