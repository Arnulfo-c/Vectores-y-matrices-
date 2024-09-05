# Inicializamos un vector de 8 elementos
numeros = []

# Solicitamos al usuario que ingrese 8 números
for i in range(8):
    numero = float(input(f"Ingrese el número {i + 1}: "))
    numeros.append(numero)

# Contamos cuántos números son positivos
contador_positivos = sum(1 for num in numeros if num > 0)

# Mostramos el resultado
print(f"Cantidad de números positivos ingresados: {contador_positivos}")
