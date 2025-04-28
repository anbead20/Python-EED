# Programa para calcular la distancia entre dos puntos en el plano

import math

# Solicitar las coordenadas del primer punto
x1 = float(input("Introduce la coordenada x1: "))
y1 = float(input("Introduce la coordenada y1: "))

# Solicitar las coordenadas del segundo punto
x2 = float(input("Introduce la coordenada x2: "))
y2 = float(input("Introduce la coordenada y2: "))

# Calcular la distancia entre los puntos usando la fórmula de distancia
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Mostrar el resultado
print(f"La distancia entre los dos puntos es: {distance}")
