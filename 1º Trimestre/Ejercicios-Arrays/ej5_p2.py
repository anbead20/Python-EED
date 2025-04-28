"""
Este programa trata de rellenar un array de 6 filas por 10 columnas con números enteros positivos entre 0 y 1000,
sin repeticiones, y luego muestra las posiciones tanto del máximo como del mínimo.

Autor: Adrián Anta Bellido
"""

import random

print("Este programa llena un array de 6 filas por 10 columnas con números entre 0 y 1000,")
print("sin repeticiones, y muestra las posiciones del número más grande y más pequeño.")
print("-------------------------------------------------------------------------------------------------------")

ROWS, COLS = 6, 10
NUM_MIN, NUM_MAX = 0, 1000

# Crear la matriz de 6x10 con números únicos
matrix = []
used_numbers = []

# Llenar la matriz
for i in range(ROWS):
    row = []
    for j in range(COLS):
        while True:
            num = random.randint(NUM_MIN, NUM_MAX)
            if num not in used_numbers:  # Si no ha sido usado, lo agregamos
                row.append(num)
                used_numbers.append(num)
                break
    matrix.append(row)

# Encontrar el máximo y el mínimo
max_value = matrix[0][0]
min_value = matrix[0][0]
max_pos = min_pos = (0, 0)

# Recorrer la matriz para encontrar el máximo y mínimo
for i in range(ROWS):
    for j in range(COLS):
        if matrix[i][j] > max_value:
            max_value = matrix[i][j]
            max_pos = (i, j)
        if matrix[i][j] < min_value:
            min_value = matrix[i][j]
            min_pos = (i, j)

# Mostrar la matriz
print("\nMatriz generada:")
for row in matrix:
    for num in row:
        print(f"{num:4}", end=" ")
    print()

# Mostrar los resultados
print(f"\nEl valor máximo es {max_value} y se encuentra en la posición {max_pos}.")
print(f"El valor mínimo es {min_value} y se encuentra en la posición {min_pos}.")
