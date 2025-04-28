"""
Este programa solicita dos números al usuario y realiza la división del primero entre el segundo.
Si el segundo número es cero, muestra un mensaje de advertencia en lugar de realizar la división.
Autor: Adrián Anta Bellido
"""

# Solicitar los dos números al usuario
number1 = float(input("Introduce el primer número: "))
number2 = float(input("Introduce el segundo número: "))

# Verificar si el segundo número es cero
if number2 != 0:
    # Realizar la división si el segundo número no es cero
    division = number1 / number2
    print(f"La división de {number1} entre {number2} es: {division}")
else:
    # Mostrar un mensaje de aviso si el segundo número es cero
    print("Error: No se puede dividir entre cero.")
