"""
Este programa verifica si una cadena ingresada por el usuario es un palíndromo.
Ignora espacios, signos de puntuación y mayúsculas.
Autor: Adrián Anta Bellido
"""

print("Este programa le permitirá ingresar una cadena de texto y verificará si es un palíndromo")
print("----------------------------------------------------------------------------------------\n")

# Solicitar al usuario que ingrese una cadena
user_input = input("Ingrese una cadena para verificar si es un palíndromo: ")

# Convertir a minúsculas y filtrar solo letras
processed_input = ""
for char in user_input:
    if char.isalpha():
        processed_input += char.lower()

# Verificar si la cadena es igual a su reverso
if processed_input == processed_input[::-1]:
    print("La cadena es un palíndromo.")
else:
    print("La cadena no es un palíndromo.")
