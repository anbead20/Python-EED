"""
Este programa lee 15 números por teclado, los almacena en un array, rota los elementos del array (el número en
la posición 0 pasa a la posición 1, el de la 1 a la 2, y el de la última posición pasa a la posición 0) y luego
muestra el contenido del array.

Autor: Adrián Anta Bellido
"""

print("Este programa lee 15 números, rota los elementos del array y muestra el resultado.")
print("--------------------------------------------------------------------------------\n")

LEN_ARRAY = 15
numbers = []

# Leer 15 números
for i in range(LEN_ARRAY):
    number = int(input(f"Introduce el número {i + 1}: "))
    numbers.append(number)

# Rotar el array
numbers = [numbers[-1]] + numbers[:-1]

# Mostrar el array rotado
print("\nArray después de rotarlo:")
print(numbers)
