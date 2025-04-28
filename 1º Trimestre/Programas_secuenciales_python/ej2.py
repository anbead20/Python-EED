# Programa para calcular el perímetro y área de un rectángulo

# Solicitar la base y altura al usuario
base = float(input("Introduce la base del rectángulo: "))
height = float(input("Introduce la altura del rectángulo: "))

# Calcular el área y el perímetro
area = base * height
perimeter = 2 * (base + height)

# Mostrar los resultados
print(f"El área del rectángulo es: {area}")
print(f"El perímetro del rectángulo es: {perimeter}")