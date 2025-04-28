"""
Implementa la clase Rectángulo (determinado por dos objetos Point) que además de su constructor, tendrá dos métodos
para calcular su área y su perímetro que tienes que transformar en propiedades. Implementa también un test que cree
dos puntos y un rectángulo a partir de estos dos puntos y que muestre el área y perímetro de dicho rectángulo.

Autor: Adrián Anta Bellido
"""

class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    def __str__(self):
        return f"({self.x},{self.y})"


class Rectangle:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    @property
    def area(self):
        base = abs(self.point2.x - self.point1.x)
        height = abs(self.point2.y - self.point1.y)
        return base * height

    @property
    def perimeter(self):
        base = abs(self.point2.x - self.point1.x)
        height = abs(self.point2.y - self.point1.y)
        return 2 * (base + height)
