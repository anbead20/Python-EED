"""
Este programa determina el tipo de triángulo basado en las longitudes de sus lados.
Autor: Adrián Anta Bellido
"""
# TODO mensaje presentación

# Entrada de los valores de los lados del triángulo
a = float(input("Ingrese el lado A: "))
b = float(input("Ingrese el lado B: "))
c = float(input("Ingrese el lado C: "))

# Verificación de triángulo rectángulo (teorema de Pitágoras)
if (a ** 2 + b ** 2 == c ** 2) or (a ** 2 + c ** 2 == b ** 2) or (b ** 2 + c ** 2 == a ** 2):
    print("Es un triángulo rectángulo.")

# Verificación de triángulo equilátero (todos los lados iguales)
elif a == b == c:
    print("Es un triángulo equilátero.")

# Verificación de triángulo isósceles (dos lados iguales)
elif a == b or a == c or b == c:
    print("Es un triángulo isósceles.")

# Si no se cumple ninguna de las condiciones anteriores, es escaleno
else:
    print("Es un triángulo escaleno.")
