# Programa para calcular la calificación final en Algoritmos

# Solicitar las calificaciones parciales al usuario
partial1 = float(input("Introduce la calificación del primer parcial (0-100): "))
partial2 = float(input("Introduce la calificación del segundo parcial (0-100): "))
partial3 = float(input("Introduce la calificación del tercer parcial (0-100): "))

# Calcular el promedio de los parciales
partial_average = (partial1 + partial2 + partial3) / 3

# Solicitar la calificación del examen final y del trabajo final
final_exam = float(input("Introduce la calificación del examen final (0-100): "))
final_project = float(input("Introduce la calificación del trabajo final (0-100): "))

# Calcular la calificación final
final_grade = (partial_average * 0.55) + (final_exam * 0.30) + (final_project * 0.15)

# Mostrar el resultado
print(f"La calificación final en la materia de Algoritmos es: {final_grade}")