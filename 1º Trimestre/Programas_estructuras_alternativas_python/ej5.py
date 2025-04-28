"""
Este programa solicita la edad de dos personas y determina quién es más joven.
Si ambas personas tienen la misma edad, se muestra un mensaje indicando dicha igualdad.
Autor: Adrián Anta Bellido
"""

# Solicitar la edad de la primera persona
age1 = int(input("Introduce la edad de la primera persona: "))

# Solicitar la edad de la segunda persona
age2 = int(input("Introduce la edad de la segunda persona: "))

# Comparar las edades y mostrar el resultado
if age1 < age2:
    print("La primera persona es más joven que la segunda.")
elif age1 > age2:
    print("La segunda persona es más joven que la primera.")
else:
    print("Ambas personas tienen la misma edad.")
