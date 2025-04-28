"""
Este programa realiza varias operaciones con arrays en Python, incluyendo el acceso a elementos específicos,
inicialización, suma de elementos, copia entre arrays y cálculo del valor máximo y mínimo.

Autor: Adrián Anta Bellido
"""

import random

print("Este programa realiza varias operaciones con arrays en Python, incluyendo el acceso a elementos específicos,")
print("inicialización, suma de elementos, copia entre arrays y cálculo del valor máximo y mínimo.")
print("----------------------------------------------------------------------------------------------------------\n")

f = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Valor del elemento 6 del array f: {f[5]}")

array = [0] * 10
array[:5] = [8] * 5
print(f"Array después de inicializar los 5 primeros elementos a 8: {array}")

c = [0] * 100
total = sum(c)
print(f"Total de los 100 elementos de punto flotante del array c: {total}")

a = [i for i in range(11)]
b = [0] * 34
b[:11] = a
print(f"Array b después de copiar los elementos de a: {b}")

w = [random.randint(0, 100) for _ in range(99)]
max_value = max(w)
min_value = min(w)
print(f"Valor mayor en el array w: {max_value}")
print(f"Valor menor en el array w: {min_value}")


