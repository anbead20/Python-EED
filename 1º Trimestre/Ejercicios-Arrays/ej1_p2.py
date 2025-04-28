"""
Este programa pide 20 números enteros, los organiza en una matriz de 4x5 y muestra las sumas parciales.
La suma total aparece en la esquina inferior derecha.

Autor: Adrián Anta Bellido
"""

print("Este programa pide 20 números enteros, los organiza en una matriz de 4x5 y muestra las sumas parciales")
print("------------------------------------------------------------------------------------------------------")

ROWS, COLUMNS = 4, 5
matrix = [[0] * COLUMNS for _ in range(ROWS)]

print("Introduce 20 números enteros:")
for row in range(ROWS):
    for column in range(COLUMNS):
        matrix[row][column] = int(input(f"Número para posición [{row + 1}, {column + 1}]: "))

row_sums = [sum(matrix[row]) for row in range(ROWS)]
column_sums = [sum(matrix[row][column] for row in range(ROWS)) for column in range(COLUMNS)]
total_sum = sum(row_sums)

print("\nMatriz con sumas parciales:")
for row in range(ROWS):
    for column in range(COLUMNS):
        print(f"{matrix[row][column]:3}", end=" | ")
    print(f"{row_sums[row]:3}")

print("-" * 29)
for column in range(COLUMNS):
    print(f"{column_sums[column]:3}", end=" | ")
print(f"{total_sum:3}")