"""
Este programa muestra los N primeros números primos, donde N es un número introducido por el usuario.
Autor: Adrián Anta Bellido
"""

# Presentación del programa
print("Bienvenido al programa que muestra los N primeros números primos.")
print("Por favor, introduzca la cantidad de números primos que desea ver.\n")

# Pedir al usuario la cantidad de números primos a mostrar
n = int(input("¿Cuántos números primos desea mostrar?: "))

# Inicializar variables
cont = 0
num = 2

# Mostrar los N primeros números primos
print(f"Los primeros {n} números primos son:")

while cont < n:
    es_primo = True  # Suponemos que el número es primo
    if num < 2:  # Si el número es menor que 2, no es primo
        es_primo = False
    else:
        for i in range(2, int(num ** 0.5) + 1):  # Verificamos si num tiene divisores
            if num % i == 0:
                es_primo = False
                break

    if es_primo:
        print(num, end=" ")
        cont += 1

    num += 1
