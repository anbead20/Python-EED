"""
Este programa encuentra todas las posiciones de una subcadena dentro de una cadena más larga.
Ambas cadenas son ingresadas por el usuario.
Autor: Adrián Anta Bellido
"""

print("Este programa encuentra todas las posiciones de una subcadena dentro de una cadena más larga")
print("--------------------------------------------------------------------------------------------\n")

# Solicitar la cadena principal y la subcadena
main_string = input("Ingrese la cadena más larga: ")
substring = input("Ingrese la subcadena a buscar: ")

# Inicializar una lista para almacenar las posiciones
positions = []

# Buscar todas las posiciones de la subcadena
start = 0

while True:
    start = main_string.find(substring, start)
    if start == -1:
        break
    positions.append(start)
    start += 1

# Mostrar los resultados
if positions:
    print("Las posiciones de la subcadena son:", positions)
else:
    print("La subcadena no se encontró en la cadena principal.")
