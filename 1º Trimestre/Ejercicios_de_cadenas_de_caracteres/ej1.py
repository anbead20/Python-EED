"""
Programa que solicita al usuario una cadena de texto y la imprime en orden inverso.
Autor: Adrián Anta Bellido
"""

print("Este programa le permitirá ingresar una cadena de texto y la mostrará en orden inverso")
print("---------------------------------------------------------------------------------------\n")

# Solicitar la cadena de texto al usuario
text = input("Por favor, ingresa una cadena de texto: ")

# Invertir y mostrar la cadena
inverted_text = text[::-1]
print("La cadena en orden inverso es:", inverted_text)
