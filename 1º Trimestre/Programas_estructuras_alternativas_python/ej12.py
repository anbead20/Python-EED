"""
Este programa determina si un año es bisiesto o no.
Autor: Adrián Anta Bellido
"""

# Entrada del año
year = int(input("Ingrese un año: "))

# Verificación si es bisiesto
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"El año {year} es bisiesto.")
else:
    print(f"El año {year} no es bisiesto.")
