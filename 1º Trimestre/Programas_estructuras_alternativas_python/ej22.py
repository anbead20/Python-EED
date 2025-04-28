"""
Este programa pide cinco números enteros y muestra cuál de ellos es el mayor.
Autor: Adrián Anta Bellido
"""

# Presentación del programa
print("Bienvenido al programa para determinar el mayor de cinco números.")
print("Ingrese cinco números enteros para ver cuál es el mayor.\n")

# Inicializar el mayor número como None para comparar en el bucle
max_number = None

# Solicitar cinco números en un bucle
for i in range(1, 6):
    number = int(input(f"Introduzca el número {i}: "))

    # Comparar y actualizar el número mayor
    if max_number is None or number > max_number:
        max_number = number

# Mostrar el número mayor
print(f"El número mayor es: {max_number}")
