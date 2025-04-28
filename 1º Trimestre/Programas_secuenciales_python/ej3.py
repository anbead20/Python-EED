# Programa para calcular la hipotenusa de un triángulo rectángulo

import math

# Solicitar los catetos al usuario
side1 = float(input("Introduce el valor del primer cateto: "))
side2 = float(input("Introduce el valor del segundo cateto: "))

# Calcular la hipotenusa usando el teorema de Pitágoras
hypotenuse = math.sqrt(side1**2 + side2**2)

# Mostrar el resultado
print(f"La hipotenusa del triángulo es: {hypotenuse}")
