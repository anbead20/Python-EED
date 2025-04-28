"""
Desarrolla un programa en Python que simule el juego clásico "Piedra, papel o tijera" contra el
ordenador.

Autor: Adrián Anta Bellido
"""

import random

print("Programa que simula el juego de 'Piedra, papel o tijera'")
print("-------------------------------------------------------\n")

rounds_played = 0
end_game = True
rounds_won = 0
rounds_lost = 0
tied_rounds = 0

user = input("¿Piedra, papel o tijera?: ").lower()
while end_game:
    if user != "piedra" and user != "papel" and user != "tijera":
        print("ERROR. Introduce una opción válida ")
        user = input("¿Piedra, papel o tijera?: ").lower()
    else:
        break

computer = random.choice(["piedra", "papel", "tijera"])
print(f"El ordenador eligió: {computer}")

while end_game:
    if user == "piedra" and computer == "tijera":
        print("¡Ganaste! Piedra gana a tijera.")
        rounds_won += 1
    elif user == "tijera" and computer == "papel":
        print("¡Ganaste! Tijera gana a papel.")
        rounds_won += 1
    elif user == "papel" and computer == "piedra":
        print("¡Ganaste! Papel gana a piedra.")
        rounds_won += 1
    elif computer == "piedra" and user == "tijera":
        print("¡Perdiste! Piedra gana a tijera.")
        rounds_lost += 1
    elif computer == "tijera" and user == "papel":
        print("¡Perdiste! Tijera gana a papel.")
        rounds_lost += 1
    elif computer == "papel" and user == "piedra":
        print("¡Perdiste! Papel gana a piedra.")
        rounds_lost += 1
    else:
        print("Es un empate")
        tied_rounds += 1

    rounds_played += 1
    question_end = input("\n¿Quieres jugar otra vez? (S/N): ").upper()

    while end_game:
        if question_end == "S":
            user = input("¿Piedra, papel o tijera?: ").lower()
            if user != "piedra" and user != "papel" and user != "tijera":
                print("ERROR. Introduce una opción válida ")
                user = input("¿Piedra, papel o tijera?: ").lower()
            else:
                computer = random.choice(["piedra", "papel", "tijera"])
                print(f"El ordenador eligió: {computer}")
            break
        elif question_end == "N":
            end_game = False
        else:
            print("ERROR. No has introducido ni 'S' ni 'N'")
            question_end = input("\n¿Quieres jugar otra vez? (S/N): ").upper()

print(f"\nFin del juego. Has jugado {rounds_played} rondas: {rounds_won} ganadas, {rounds_lost} perdidas, {tied_rounds} empate.")