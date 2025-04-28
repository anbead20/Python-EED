"""
Este programa define tres arrays de 20 números enteros: uno con valores aleatorios, otro con sus cuadrados
y otro con sus cubos. Luego, muestra los tres arrays en tres columnas.

Autor: Adrián Anta Bellido
"""

import random

print("Este programa genera tres arrays: uno con números aleatorios entre 0 y 100, otro con sus cuadrados y otro con sus cubos.")
print("----------------------------------------------------------------------------------------------------------------------\n")

MIN_NUMBER = 0
MAX_NUMBER = 100
LEN_ARRAY = 20

numbers = [random.randint(MIN_NUMBER, MAX_NUMBER) for _ in range(LEN_ARRAY)]
squares = [num ** 2 for num in numbers]
cubes = [num ** 3 for num in numbers]

print(f"{'Número':<10}{'Cuadrado':<15}{'Cubo':<20}")
print("-" * 45)

for i in range(LEN_ARRAY):
    print(f"{numbers[i]:<10}{squares[i]:<15}{cubes[i]:<20}")
