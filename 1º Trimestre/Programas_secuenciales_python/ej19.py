# Programa para calcular la nota final de un examen

# Definir los puntos por respuesta
points_per_correct_answer = 5
points_per_wrong_answer = -1
points_per_blank_answer = 0

# Solicitar el número de respuestas correctas, incorrectas y en blanco
correct_answers = int(input("Introduce el número de respuestas correctas: "))
wrong_answers = int(input("Introduce el número de respuestas incorrectas: "))
blank_answers = int(input("Introduce el número de respuestas en blanco: "))

# Calcular la nota total
total_score = (correct_answers * points_per_correct_answer) + (wrong_answers * points_per_wrong_answer) + (blank_answers * points_per_blank_answer)

# Mostrar la puntuación total
print(f"La puntuación total obtenida por el estudiante es: {total_score}")

# Calcular la nota normalizada entre 0 y 10
if total_score < 0:
    normalized_score = 0  # Si la puntuación es negativa, la nota normalizada es 0
else:
    # Supongamos que la puntuación máxima sería la cantidad de respuestas correctas * puntos por respuesta correcta
    max_score = (correct_answers + wrong_answers + blank_answers) * points_per_correct_answer
    normalized_score = (total_score / max_score) * 10 if max_score > 0 else 0

# Mostrar la nota normalizada
print(f"La nota normalizada entre 0 y 10 es: {normalized_score:.2f}")
