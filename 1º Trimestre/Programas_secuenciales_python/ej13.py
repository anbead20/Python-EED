# Programa para calcular la raíz cuadrada y la raíz cúbica de un número

import math

# Solicitar un número al usuario
number = float(input("Introduce un número: "))

# Calcular la raíz cuadrada
square_root = math.sqrt(number)

# Calcular la raíz cúbica
cube_root = number ** (1/3)

# Mostrar los resultados
print(f"La raíz cuadrada de {number} es: {square_root}")
print(f"La raíz cúbica de {number} es: {cube_root}")
