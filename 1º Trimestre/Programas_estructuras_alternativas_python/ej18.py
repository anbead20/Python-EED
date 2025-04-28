"""
Este programa pide un número del 1 al 7 y muestra el día de la semana correspondiente.
Autor: Adrián Anta Bellido
"""

# Entrada del número del día de la semana
day_number = int(input("Introduzca un número del 1 al 7 para indicar el día de la semana: "))

# Verificación del número y muestra del día correspondiente usando match-case
match day_number:
    case 1:
        print("El día es lunes.")
    case 2:
        print("El día es martes.")
    case 3:
        print("El día es miércoles.")
    case 4:
        print("El día es jueves.")
    case 5:
        print("El día es viernes.")
    case 6:
        print("El día es sábado.")
    case 7:
        print("El día es domingo.")
    case _:
        print("ERROR: número incorrecto.")
