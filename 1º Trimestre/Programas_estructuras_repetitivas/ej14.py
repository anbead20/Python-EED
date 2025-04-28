"""
Programa para comprobar si una cadena contiene una subcadena introducida por el usuario.
El programa solicita dos cadenas: la cadena principal y la subcadena, y verifica si la subcadena está en la cadena principal.
Autor: Adrián Anta Bellido
"""

# Presentación del programa
print("Bienvenido al programa de búsqueda de subcadenas.")
print("Introduce una cadena y una subcadena. Comprobaré si la subcadena está presente en la cadena.\n")

main_string = input("Introduce la cadena principal: ")
substring = input("Introduce la subcadena: ")

# Comprobar si la subcadena está en la cadena principal usando una estructura repetitiva
found = False
for i in range(len(main_string) - len(substring) + 1):
    if main_string[i:i + len(substring)] == substring:
        found = True
        break

# Mostrar el resultado
if found:
    print(f"La subcadena '{substring}' está presente en la cadena principal.")
else:
    print(f"La subcadena '{substring}' NO está presente en la cadena principal.")
