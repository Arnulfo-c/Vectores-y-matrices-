def matriz_identidad(n):
    identidad = []

    for i in range(n):
        fila = [0] * n
        fila[i] = 1
        identidad.append(fila)
    return identidad

#El tamaño de la matriz identidad 
n = 4
matriz = matriz_identidad(n)

#Mostrar la matriz identidad
for fila in matriz:
    print(fila)