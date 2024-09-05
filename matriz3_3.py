#Inicio de la matriz
matriz = []

#Solicitar al usuario que llene la matriz
print("Por favor, ingrese el numero de la matriz: ")
for i in range(3):
    fila = []
    for j in range(3):
        elemento = int(input(f"Ingrese el numero en la posicion ({i+1}, {j+1}): "))
        fila.append(elemento)
    matriz.append(fila)

#Calcular la suma de los elementos de la matriz 
suma_total = 0
for fila in matriz:
    suma_total += sum(fila)

#Aqui se mostrara la matriz y la suma total
print("\nLa matriz ingresada es:")
for fila in matriz:
    print(fila)

print(f"\nLa suma de todos los elementos de la matriz es: {suma_total}")
