"""
Este programa solicita dos números al usuario y verifica si el primero es mayor que el segundo.
Autor: Adrián Anta Bellido
"""

# Programa para comparar dos números

# Solicitar los dos números al usuario
number1 = float(input("Introduce el primer número: "))
number2 = float(input("Introduce el segundo número: "))

# Comparar los números y mostrar el resultado
if number1 > number2:
    print(f"El primer número ({number1}) es mayor que el segundo número ({number2}).")
else:
    print(f"El primer número ({number1}) no es mayor que el segundo número ({number2}).")
