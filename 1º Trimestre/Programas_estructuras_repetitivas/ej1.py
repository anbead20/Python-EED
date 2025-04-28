"""
Este programa pedirá repetidamente al usuario un número entre 1 y 100, hasta que lo adivine.
Autor: Adrián Anta Bellido
"""

import random

MIN_TO_GUESS = 1
MAX_TO_GUESS = 100
MAX_TRY = 10

# Presentación del programa
print(f"Programa para adivinar número entre {MIN_TO_GUESS} y {MAX_TO_GUESS}")
print("-------------------------------------------")

num_to_guess = random.randint(MIN_TO_GUESS, MAX_TO_GUESS)
tries = 1
limit_min = MIN_TO_GUESS
limit_max = MAX_TO_GUESS

# Programa
n = int(input(f"Introduce un número del {MIN_TO_GUESS} al {MAX_TO_GUESS}: "))

while n != num_to_guess and tries < MAX_TRY:
    print("No has acertado")
    if n < num_to_guess:
        limit_min = n
        print("El número es mayor")
    else:
        limit_max = n
        print("El número es menor")
    n = int(input(f"Dame un número entre {limit_min} y {limit_max}: "))
    tries += 1

# Fin del programa
if tries == MAX_TRY:
    print(f"Has agotado los {MAX_TRY} intentos")
else:
    print(f"Acertaste en {tries} intento/s")