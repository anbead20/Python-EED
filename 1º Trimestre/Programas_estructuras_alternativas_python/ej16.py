"""
Este programa calcula el costo de una llamada telefónica según su duración, el día y el turno en que se realizó.
Autor: Adrián Anta Bellido
"""

# Entrada de los datos
duration = int(input("Ingrese la duración de la llamada en minutos: "))
day = input("Ingrese el día de la semana (domingo o entre semana): ").lower()
turn = input("Ingrese el turno (mañana o tarde): ").lower()

# Cálculo del costo básico según la duración de la llamada
if duration <= 5:
    base_cost = duration * 1.00
elif duration <= 8:
    base_cost = 5 * 1.00 + (duration - 5) * 0.80
elif duration <= 10:
    base_cost = 5 * 1.00 + 3 * 0.80 + (duration - 8) * 0.70
else:
    base_cost = 5 * 1.00 + 3 * 0.80 + 2 * 0.70 + (duration - 10) * 0.50

# Cálculo del impuesto según el día y el turno
if day == "domingo":
    tax = base_cost * 0.03  # 3% si es domingo
else:
    if turn == "mañana":
        tax = base_cost * 0.15  # 15% en turno de mañana
    elif turn == "tarde":
        tax = base_cost * 0.10  # 10% en turno de tarde

# Cálculo del costo total
total_cost = base_cost + tax

# Mostrar los resultados
print(f"Costo básico de la llamada: {base_cost:.2f} euros.")
print(f"Impuesto aplicado: {tax:.2f} euros.")
print(f"Total a pagar: {total_cost:.2f} euros.")
