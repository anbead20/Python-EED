"""
Este programa pide repetidamente una cadena y un carácter, y muestra cuántas veces aparece el carácter en la cadena.
Autor: Adrián Anta Bellido
"""

# Presentación del programa
print("Bienvenido al programa que cuenta las ocurrencias de un carácter en una cadena.")
print("Introduzca 'salir' para finalizar el programa.\n")

string = input("Introduce una cadena: ")
char = input("Introduce un carácter: ")

counter = 0

for i in string:
    if i == char:
        counter += 1

# Mostrar el resultado
print(f"El carácter {char} aparece {counter} veces en la cadena.")
