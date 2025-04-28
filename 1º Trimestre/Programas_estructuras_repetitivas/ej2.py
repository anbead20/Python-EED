"""
Realizar un algoritmo que pida números,se pedirá al usuario que introduzca números y que el programa
le diga si son mayores, menores o igual que 0.
Autor: Adrián Anta Bellido
"""

print("Introducir números y que te diga si son mayores, menores o igual que 0")
print("---------------------------------------------------------------------")

amount = int(input("Introduce la cantidad de números a introducir: "))
number = int(input("Introduce un número: "))

counter = 1

while counter < amount:
    if number > 0:
        print(f"El número {number} es mayor que 0")
        number = int(input("Introduce un número: "))
    elif number < 0:
        print(f"El número {number} es menor que 0")
        number = int(input("Introduce un número: "))
    else:
        print(f"El número {number} es igual que 0")
        number = int(input("Introduce un número: "))
    counter += 1

print(f"Has introducido la cantidad máxima: {amount}")