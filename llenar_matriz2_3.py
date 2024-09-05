# Inicializar la matriz 2x3
matriz = []

# Solicitar al usuario que llene la matriz
print("Por favor, ingrese los elementos de la matriz 2x3:")
for i in range(2):
    fila = []
    for j in range(3):
        elemento = int(input(f"Ingrese el elemento en la posición ({i+1},{j+1}): "))
        fila.append(elemento)
    matriz.append(fila)

# Mostrar la matriz ingresada
print("\nLa matriz ingresada es:")
for fila in matriz:
    print(fila)

# Calcular la transpuesta de la matriz
transpuesta = [[matriz[j][i] for j in range(2)] for i in range(3)]

# Mostrar la matriz transpuesta
print("\nLa matriz transpuesta es:")
for fila in transpuesta:
    print(fila)
