"""
Este programa lee 10 números introducidos por teclado y los muestra en orden inverso al de su introducción.

Autor: Adrián Anta Bellido
"""

print("Este programa solicita 10 números al usuario y los muestra en orden inverso al que fueron introducidos.")
print("----------------------------------------------------------------------------------------------------------\n")

numbers = []

for n in range(10):
    number = int(input(f"Introduce el número {n + 1}: "))
    numbers.append(number)

print("\nLos números en orden inverso son:")
print(numbers[::-1])
