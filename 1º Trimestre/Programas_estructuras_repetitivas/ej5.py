"""
Este programa pide un límite inferior y un límite superior para un intervalo. Luego, permite ingresar números
hasta que se introduce el 0. Al final, muestra la suma de los números dentro del intervalo, la cantidad de números
fuera del intervalo y si se ingresó algún número igual a los límites del intervalo.

Autor: Adrián Anta Bellido
"""

# Presentación del programa
print("Bienvenido al programa que analiza un intervalo.")
print("Por favor, introduzca el límite inferior y superior del intervalo.")

# Solicitar límites del intervalo
lower_limit = int(input("Introduzca el límite inferior: "))
upper_limit = int(input("Introduzca el límite superior: "))

while lower_limit >= upper_limit:
    print("ERROR: El límite inferior debe ser menor que el límite superior. Inténtelo de nuevo.")
    lower_limit = int(input("Introduzca el límite inferior: "))
    upper_limit = int(input("Introduzca el límite superior: "))

total_sum = 0
outside_count = 0
equal_limits = False

number = int(input("Introduce números (introduzca 0 para terminar): "))

while number != 0:
    if lower_limit < number < upper_limit:
        total_sum += number
    else:
        outside_count += 1

    if number == lower_limit or number == upper_limit:
        equal_limits = True

    number = int(input("Introduce números (introduzca 0 para terminar): "))

# Mostrar resultados
print(f"La suma de los números dentro del intervalo es: {total_sum}")
print(f"Cantidad de números fuera del intervalo: {outside_count}")

if equal_limits:
    print("Se ingresó al menos un número igual a los límites del intervalo.")
else:
    print("No se ingresó ningún número igual a los límites del intervalo.")
