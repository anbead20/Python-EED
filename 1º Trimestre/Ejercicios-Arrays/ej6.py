"""
Este programa genera 20 números aleatorios entre 0 y 100, los almacena en un array y luego coloca los números
pares en las primeras posiciones del array y los impares en las posiciones restantes.

Autor: Adrián Anta Bellido
"""

import random

MIN_NUMBER = 0
MAX_NUMBER = 100
LEN_ARRAY = 20

print("Este programa genera 20 números aleatorios entre 0 y 100, los almacena en un array y luego coloca los números")
print("pares en las primeras posiciones y los impares en las posiciones restantes.")
print("-----------------------------------------------------------------------------------------------------------\n")

# Generar los 20 números aleatorios
numbers = [random.randint(MIN_NUMBER, MAX_NUMBER) for _ in range(LEN_ARRAY)]

# Crear arrays auxiliares para los pares e impares
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]

print(f"Números generados: {numbers}")

# Unir los arrays de números pares y impares
result = even_numbers + odd_numbers

print(f"Array después de mover los pares al principio: {result}")
