"""
Este programa pide 10 números por teclado y luego muestra los números introducidos junto con las palabras
“máximo” y “mínimo” al lado del número máximo y mínimo respectivamente.

Autor: Adrián Anta Bellido
"""

print("Este programa solicita 10 números al usuario y luego muestra los números introducidos junto con las palabras")
print("“máximo” y “mínimo” al lado del número máximo y mínimo respectivamente.")
print("----------------------------------------------------------------------------------------------------------\n")

numbers = []

for i in range(10):
    number = int(input(f"Introduce el número {i + 1}: "))
    numbers.append(number)

max_value = max(numbers)
min_value = min(numbers)

for num in numbers:
    print(f"\n{num}", end=" ")
    if num == min_value:
        print(f"mínimo", end=" ")
    if num == max_value:
        print(f"máximo")