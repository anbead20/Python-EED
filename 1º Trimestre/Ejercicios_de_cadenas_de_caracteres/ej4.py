"""
Este programa reemplaza todas las ocurrencias de una subcadena especificada por el usuario
con otra subcadena dentro de una cadena proporcionada inicialmente.
Autor: Adrián Anta Bellido
"""

print("Este programa le permitirá reemplazar todas las ocurrencias de una subcadena en una cadena de texto")
print("---------------------------------------------------------------------------------------------------\n")

# Bucle principal
while True:
    # Solicitar la cadena original y las subcadenas
    original_string = input("Ingrese la cadena original: ")
    substring_to_replace = input("Ingrese la subcadena que desea reemplazar: ")
    replacement_substring = input("Ingrese la subcadena con la que desea reemplazar: ")

    # Reemplazar todas las ocurrencias de la subcadena
    modified_string = original_string.replace(substring_to_replace, replacement_substring)

    # Mostrar la cadena modificada
    print("Cadena modificada:", modified_string)

    # Preguntar si el usuario quiere continuar
    if input("¿Quiere continuar? (s/n): ").lower() != 's':
        print("Gracias por usar el programa.")
        break
