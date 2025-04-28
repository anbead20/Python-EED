"""
Este programa solicita un número entero entre 1 y 12 e imprime el nombre del mes y el número de días del mes correspondiente.
Autor: Adrián Anta Bellido
"""

# Entrada del número del mes
month_number = int(input("Introduzca un número entre 1 y 12 para el mes: "))

# Inicializar la variable days y month_name
days = 0
month_name = ""

# Días en cada mes y el nombre del mes usando match-case
match month_number:
    case 1:
        days = 31
        month_name = "Enero"
    case 2:
        days = 28  # Considerando año no bisiesto
        month_name = "Febrero"
    case 3:
        days = 31
        month_name = "Marzo"
    case 4:
        days = 30
        month_name = "Abril"
    case 5:
        days = 31
        month_name = "Mayo"
    case 6:
        days = 30
        month_name = "Junio"
    case 7:
        days = 31
        month_name = "Julio"
    case 8:
        days = 31
        month_name = "Agosto"
    case 9:
        days = 30
        month_name = "Septiembre"
    case 10:
        days = 31
        month_name = "Octubre"
    case 11:
        days = 30
        month_name = "Noviembre"
    case 12:
        days = 31
        month_name = "Diciembre"
    case _:
        print("ERROR: número incorrecto. Debe estar entre 1 y 12.")
        exit()

# Mostrar el nombre del mes y el número de días
print(f"El mes de {month_name} tiene {days} días.")