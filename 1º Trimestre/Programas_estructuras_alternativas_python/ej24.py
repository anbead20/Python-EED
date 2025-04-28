"""
Este programa convierte una calificación numérica de un examen en su equivalente cualitativo.
Autor: Adrián Anta Bellido
"""

# Presentación del programa
print("Bienvenido al programa de calificación cualitativa.")
print("Ingrese una calificación numérica para ver la calificación cualitativa correspondiente.\n")

# Entrada de la calificación numérica
score = float(input("Introduzca la calificación numérica (0 a 10): "))

# Determinación de la calificación cualitativa
if score < 0 or score > 10:
    print("ERROR: La calificación debe estar entre 0 y 10.")
elif score < 5:
    print("Calificación cualitativa: Suspenso")
elif score < 7:
    print("Calificación cualitativa: Aprobado")
elif score < 9:
    print("Calificación cualitativa: Notable")
elif score < 10:
    print("Calificación cualitativa: Sobresaliente")
else:
    print("Calificación cualitativa: Matrícula de Honor")
