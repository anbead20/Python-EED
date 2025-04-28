"""
Este programa trata de rellenar un array de 6 filas por 10 columnas con números enteros positivos entre 0 y 1000,
y luego muestra las posiciones tanto del máximo como del mínimo.

Autor: Adrián Anta Bellido
"""

import random

print("Este programa rellena un array de 6 filas por 10 columnas con números enteros positivos entre 0 y 1000,")
print("y luego muestra las posiciones tanto del máximo como del mínimo.")
print("----------------------------------------------------------------------------------------------------------------------")

ROWS, COLUMNS = 6, 10
NUM_MIN, NUM_MAX = 0, 1000

matrix = [[random.randint(NUM_MIN, NUM_MAX) for _ in range(COLUMNS)] for _ in range(ROWS)]

# Inicialización de variables para máximo y mínimo
max_value = NUM_MIN - 1
min_value = NUM_MAX + 1
max_pos = (-1, -1)
min_pos = (-1, -1)

# Búsqueda de los valores máximo y mínimo
for row in range(ROWS):
    for column in range(COLUMNS):
        if matrix[row][column] > max_value:
            max_value = matrix[row][column]
            max_pos = (row, column)
        if matrix[row][column] < min_value:
            min_value = matrix[row][column]
            min_pos = (row, column)

# Mostrar la matriz
print("Matriz generada:")
for row in range(ROWS):
    for column in range(COLUMNS):
        print(f"{matrix[row][column]:4}", end=" ")
    print()

# Mostrar resultados
print(f"\nEl valor máximo es {max_value} y se encuentra en la posición {max_pos}.")
print(f"El valor mínimo es {min_value} y se encuentra en la posición {min_pos}.")
