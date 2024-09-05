# Función para multiplicar dos matrices de 2x2
def multiplicar_matrices(matriz1, matriz2):
    resultado = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]
    return resultado

# Solicitar al usuario que llene la primera matriz 2x2
print("Ingrese los elementos de la primera matriz 2x2:")
matriz1 = []
for i in range(2):
    fila = []
    for j in range(2):
        elemento = int(input(f"Ingrese el elemento en la posición ({i+1},{j+1}): "))
        fila.append(elemento)
    matriz1.append(fila)

# Solicitar al usuario que llene la segunda matriz 2x2
print("\nIngrese los elementos de la segunda matriz 2x2:")
matriz2 = []
for i in range(2):
    fila = []
    for j in range(2):
        elemento = int(input(f"Ingrese el elemento en la posición ({i+1},{j+1}): "))
        fila.append(elemento)
    matriz2.append(fila)

# Multiplicar las matrices
resultado = multiplicar_matrices(matriz1, matriz2)

# Mostrar las matrices ingresadas y el resultado
print("\nLa primera matriz ingresada es:")
for fila in matriz1:
    print(fila)

print("\nLa segunda matriz ingresada es:")
for fila in matriz2:
    print(fila)

print("\nEl resultado de la multiplicación de las matrices es:")
for fila in resultado:
    print(fila)