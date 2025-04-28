"""
Este programa pide el resultado de un dado de seis caras y muestra el número en letras de la cara opuesta.
Autor: Adrián Anta Bellido
"""

# Entrada del número del dado
die_number = int(input("Introduzca número del dado (1-6): "))

# Verificación del número del dado y cálculo de la cara opuesta
match die_number:
    case 1:
        print('En la cara opuesta está el "seis".')
    case 2:
        print('En la cara opuesta está el "cinco".')
    case 3:
        print('En la cara opuesta está el "cuatro".')
    case 4:
        print('En la cara opuesta está el "tres".')
    case 5:
        print('En la cara opuesta está el "dos".')
    case 6:
        print('En la cara opuesta está el "uno".')
    case _:
        print("ERROR: número incorrecto.")
