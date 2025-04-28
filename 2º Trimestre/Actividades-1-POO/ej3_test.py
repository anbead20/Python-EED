from ej3 import Point, Rectangle
# Test de las clases Point y Rectangle
point1 = Point(1, 2)
point2 = Point(4, 6)

# Crear el rectángulo con los dos puntos
rectangle = Rectangle(point1, point2)

# Imprimir área y perímetro del rectángulo
print(f"Área del rectángulo: {rectangle.area}")
print(f"Perímetro del rectángulo: {rectangle.perimeter}")