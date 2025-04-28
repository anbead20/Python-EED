"""
Este programa calcula la ganancia obtenida por un productor de uva según el tipo, tamaño y precio inicial del kilo de uva.
Autor: Adrián Anta Bellido
"""

import sys

print("Programa calcula la ganancia obtenida por un productor de uva")
print("-------------------------------------------------------------")

# Entrada de los datos
type_uva = input("Ingrese el tipo de uva (A o B): ").upper()
if type_uva != "A" and type_uva != "B":
    print("No has introducido ni A ni B", file=sys.stderr)
    exit(1)

size_uva = int(input("Ingrese el tamaño de la uva (1 o 2): "))
if size_uva != 1 and size_uva != 2:
    print("No has introducido ni 1 ni 2", file=sys.stderr)
    exit(1)

initial_price = float(input("Ingrese el precio inicial por kilo de uva: "))
kilos = float(input("Ingrese la cantidad de kilos de uva: "))

final_price = 0

# Determinación del ajuste al precio por tipo y tamaño
if type_uva == 'A' and size_uva == 1:
    final_price = initial_price + 0.20

elif type_uva == 'A' and size_uva == 2:
    final_price = initial_price + 0.30

elif type_uva == 'B' and size_uva == 1:
    final_price = initial_price - 0.30

elif type_uva == 'B' and size_uva == 2:
    final_price = initial_price - 0.50

# Cálculo de la ganancia total
total_gain = final_price * kilos

# Mostrar la ganancia obtenida
print(f"La ganancia obtenida por el productor es: {total_gain:.2f} euros.")