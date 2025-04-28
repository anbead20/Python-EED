"""
Este programa pide cinco números enteros y determina cuál de los cuatro últimos números es más cercano al primero.
Autor: Adrián Anta Bellido
"""

# Presentación del programa
print("Bienvenido al programa para encontrar el número más cercano al primero.")
print("Ingrese cinco números enteros, y se determinará cuál de los cuatro últimos es el más cercano al primero.\n")

# Entrada de los cinco números
numbers = []
for i in range(1, 6):
    number = int(input(f"Introduzca el número {i}: "))
    numbers.append(number)

# El primer número de la lista
first_number = numbers[0]

# Determinar cuál de los cuatro últimos números es más cercano al primero
closest_number = numbers[1]
min_difference = abs(first_number - closest_number)

for i in range(2, 5):
    difference = abs(first_number - numbers[i])
    if difference < min_difference:
        min_difference = difference
        closest_number = numbers[i]

# Mostrar el resultado
print(f"El número más cercano a {first_number} es: {closest_number}")
