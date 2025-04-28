"""
Este programa genera automáticamente 20 números aleatorios entre 100 y 999,
los organiza en una matriz de 4x5 y muestra las sumas parciales de filas y columnas,
además de la suma total en la esquina inferior derecha, con un pequeño retardo al mostrar los resultados.

Autor: Adrián Anta Bellido
"""

import random
import time

print("Este programa genera 20 números aleatorios entre 100 y 999, los organiza en una matriz de 4x5")
print("---------------------------------------------------------------------------------------------")

ROWS, COLUMNS = 4, 5
NUM_MIN, NUM_MAX = 100, 999

matrix = [[random.randint(NUM_MIN, NUM_MAX) for _ in range(COLUMNS)] for _ in range(ROWS)]

row_sums = [sum(row) for row in matrix]
column_sums = [sum(matrix[row][column] for row in range(ROWS)) for column in range(COLUMNS)]
total_sum = sum(row_sums)

print("\nGenerando matriz y sumas parciales...\n")
time.sleep(1)

print("Matriz con sumas parciales:")
for row in range(ROWS):
    time.sleep(0.5)
    for column in range(COLUMNS):
        print(f"{matrix[row][column]:3}", end=" | ")
    print(f"{row_sums[row]:5}")

time.sleep(0.5)
print("-" * 37)
time.sleep(0.5)

for column in range(COLUMNS):
    print(f"{column_sums[column]:3}", end=" | ")
print(f"{total_sum:5}")
