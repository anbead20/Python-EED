"""
Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ en caso contrario.
Autor: Adrián Anta Bellido
"""

print("Introducir caracteres e imprimir 'VOCAL' o 'NO VOCAL'")
print("-----------------------------------------------------")

VOCAL = "aeiouAEIOU"

character = input("Introduce caracteres: ")

while character != " ":
    if character in VOCAL:
        print("VOCAL")
        character = input("Introduce caracteres: ")
    else:
        print("NO VOCAL")
        character = input("Introduce caracteres: ")

print("Has introducido un espacio, fin del programa")