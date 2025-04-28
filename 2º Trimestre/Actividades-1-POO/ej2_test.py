from ej2 import Point

# Test de la clase Point
point = Point(1, 3)

print(f"Punto inicial: {point}")

print(f"Coordenada x: {point.x}")

point.x = 0
print(f"Punto después de asignar x=0: {point}")

point.invert_coordinates()
print(f"Punto después de invertir las coordenadas: {point}")