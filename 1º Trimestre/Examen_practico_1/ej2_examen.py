"""
Desarrolla un programa en Python que simule un juego de dados contra el ordenador, donde se
acumulen puntos basados en el resultado de los lanzamientos.

Autor: Adrián Anta Bellido
"""

import random

print("Programa que simula un juego de dados")
print("-------------------------------------\n")

player_points = 0
computer_points = 0
end_game = True

roll_dice = input("Presiona 'Intro' para lanzar dado: ")
while end_game:
    if roll_dice != "":
        print("No le has dado al 'Intro'")
        roll_dice = input("Presiona 'Intro' para lanzar dado: ")
    else:
        break

user = (random.randint(1, 6))
computer = (random.randint(1, 6))
print(f"Tu dado: {user}")
print(f"Dado del ordenador: {computer}")

while end_game:
    if user > computer:
        print("¡Ganaste la ronda!")
        player_points += user
    elif user < computer:
        print("El ordenador gana la ronda.")
        computer_points += computer
    else:
        print("¡EMPATE!")

    print(f"Puntos acumulados por ti: {player_points}")
    print(f"Puntos acumulados por el ordenador: {computer_points}")
    question_end = input("\n¿Quieres jugar otra vez? (S/N): ").upper()

    while end_game:
        if question_end == "S":
            roll_dice = input("Presiona 'Intro' para lanzar dado: ")
            if roll_dice != "":
                print("No le has dado al 'Intro'")
                roll_dice = input("Presiona 'Intro' para lanzar dado: ")
            else:
                user = (random.randint(1, 6))
                computer = (random.randint(1, 6))
                print(f"Tu dado: {user}")
                print(f"Dado del ordenador: {computer}")
            break
        elif question_end == "N":
            end_game = False
        else:
            print("ERROR. No has introducido ni 'S' ni 'N'")
            question_end = input("\n¿Quieres jugar otra vez? (S/N): ").upper()

print("\nFin del juego")
if player_points > computer_points:
    print(f"Has ganado {player_points} a {computer_points}")
elif player_points < computer_points:
    print(f"Gana el ordenador {computer_points} a {player_points}.")
else:
    print("Habéis empatado")