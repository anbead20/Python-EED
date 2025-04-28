"""
Este programa solicita un número al usuario e indica si el número es par o impar.
Autor: Adrián Anta Bellido
"""

# Solicitar un número al usuario
number = int(input("Introduce un número: "))

# Determinar si es par o impar
if number % 2 == 0:
    print(f"El número {number} es par.")
else:
    print(f"El número {number} es impar.")
