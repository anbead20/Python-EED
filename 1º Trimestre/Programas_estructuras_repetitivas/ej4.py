"""
Este programa imprime todos los números pares entre dos números pedidos al usuario.
Autor: Adrián Anta Bellido
"""

print("Imprime todos los números pares entre dos números pedidos al usuario")
print("------------------------------------------------------------")

number1 = int(input("Introduce el primer número: "))
number2 = int(input("Introduce el segundo número: "))

for peers in range(min(number1, number2), max(number1, number2) + 1):
    if peers % 2 == 0:
        print(peers)
