from ej4 import *

# Test de la clase Dice
random.seed(42)  # Para reproducibilidad en los valores aleatorios

# Crear un vector de 4 dados con diferentes formas de inicialización
dice_list = [
    Dice(),  # Dado aleatorio de 6 caras
    Dice(3),  # Dado de 6 caras con el 3 arriba
    Dice(5, 10),  # Dado de 10 caras con el 5 arriba
    Dice(1, 20)  # Dado de 20 caras con el 1 arriba
]

# Imprimir los valores iniciales de los dados
print("Valores iniciales de los dados:")
for dice in dice_list:
    print(dice)

# Lanzar los dados varias veces
print("\nLanzando los dados...")
for _ in range(5):
    for dice in dice_list:
        dice.roll()
        print(dice)
