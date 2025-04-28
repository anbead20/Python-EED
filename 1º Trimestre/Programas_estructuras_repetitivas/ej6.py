"""
Este programa calcula la potencia de un número real (base) elevado a un exponente entero positivo,
sin utilizar el operador de potencia ni funciones predefinidas.
Autor: Adrián Anta Bellido
"""

# Presentación del programa
print("Bienvenido al programa que calcula la potencia de un número real.")
print("Introduzca la base (número real) y el exponente (número entero positivo).")

# Entrada de datos
base = int(input("Introduzca la base (número real): "))
exponent = int(input("Introduzca el exponente (entero positivo): "))

# Verificar que el exponente es positivo
if exponent < 0:
    print("ERROR: El exponente debe ser un número entero positivo.")
else:
    result = 1  # Inicializamos el resultado

    # Calcular la potencia usando un bucle
    for _ in range(exponent):
        result *= base

    # Mostrar el resultado
    print(f"{base} elevado a {exponent} es: {result}")