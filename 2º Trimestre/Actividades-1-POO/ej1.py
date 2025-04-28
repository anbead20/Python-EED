"""
Crea una clase "Dado" que simule el funcionamiento de un dado con caras del 1 al 6 que tienen la misma probabilidad
de salir y un programa de prueba.

Autor: Adrián Anta Bellido
"""

import random

class Dice:
    def __init__(self):
        self.faces = 6

    def throw(self):
        return random.randint(1, self.faces)

if __name__ == "__main__":
    counter = 0
    dice = Dice()

    print("Simulación de lanzamiento de dado:")
    print("----------------------------------")

    for _ in range(3):
        result = dice.throw()
        counter += 1
        print(f"Resultado del lanzamiento dado {counter}: {result}")
