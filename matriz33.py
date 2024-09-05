# Inicializar la matriz 3x3
matriz = []

# Solicitar al usuario que llene la matriz
print("Por favor, ingrese los elementos de la matriz 3x3:")
for i in range(3):
    fila = []
    for j in range(3):
        elemento = int(input(f"Ingrese el elemento en la posición ({i+1},{j+1}): "))
        fila.append(elemento)
    matriz.append(fila)

# Mostrar la matriz ingresada
print("\nLa matriz ingresada es:")
for fila in matriz:
    print(fila)

# Mostrar los elementos de la diagonal principal
print("\nLos elementos de la diagonal principal son:")
for i in range(3):
    print(matriz[i][i])
