"""
Este programa solicita las coordenadas y radios de dos circunferencias y
las clasifica en uno de los siguientes estados: exteriores, tangentes exteriores,
secantes, tangentes interiores, interiores o concéntricas.
Autor: Adrián Anta Bellido
"""

import math

# Solicitar los puntos centrales y radios de las circunferencias
x1 = float(input("Introduce la coordenada x del centro de la primera circunferencia: "))
y1 = float(input("Introduce la coordenada y del centro de la primera circunferencia: "))
r1 = float(input("Introduce el radio de la primera circunferencia: "))

x2 = float(input("Introduce la coordenada x del centro de la segunda circunferencia: "))
y2 = float(input("Introduce la coordenada y del centro de la segunda circunferencia: "))
r2 = float(input("Introduce el radio de la segunda circunferencia: "))

# Calcular la distancia entre los centros
distance_centers = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
sum_radius = r1 + r2
sub_radius = abs(r1 - r2)

# Clasificar las circunferencias
if distance_centers > sum_radius:
    state = "exteriores"
elif distance_centers == sum_radius:
    state = "tangentes exteriores"
elif r1 + distance_centers > r2 and r2 + distance_centers > r1:
    state = "secantes"
elif distance_centers == sub_radius:
    state = "tangentes interiores"
elif distance_centers < sub_radius:
    state = "interiores"
elif distance_centers == 0 and r1 == r2:
    state = "concéntricas"
else:
    state = "no clasificada"

# Mostrar el resultado
print(f"Las circunferencias son: {state}.")
