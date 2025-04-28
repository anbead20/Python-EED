"""
Este programa determina el costo del viaje de estudios por alumno y el total a pagar a la compañía de autobuses.
Autor: Adrián Anta Bellido
"""
# TODO mensaje de bienvenida

# Entrada del número de alumnos
num_students = int(input("Ingrese el número de alumnos: "))

# Determinación del costo por alumno o costo total si son menos de 30
if num_students >= 100:
    cost_per_student = 65
elif num_students >= 50:
    cost_per_student = 70
elif num_students >= 30:
    cost_per_student = 95
else:
    cost_per_student = 4000 / num_students

total_cost = num_students * cost_per_student

# Mostrar el costo total y el costo por alumno
print(f"El pago total a la compañía de autobuses es: {total_cost:.2f} euros.")
print(f"Cada alumno debe pagar: {cost_per_student:.2f} euros.")
