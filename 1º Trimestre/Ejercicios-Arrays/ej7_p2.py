"""
Este programa permite gestionar las calificaciones de los estudiantes en varios módulos.
Incluye funciones para registrar datos, calcular promedios, encontrar máximos y mínimos,
y listar alumnos ordenados por notas en un módulo específico.

Autor: Adrián Anta Bellido
"""

# Lista de módulos
MODULES = ("PROGRAMACIÓN", "LENGUAJE DE MARCAS", "BASES DE DATOS", "SISTEMAS INFORMÁTICOS")

# Lista para almacenar los datos de los alumnos
students = []

def input_student_data():
    while True:
        name = input("\nIntroduce nombre y apellidos del alumno (Deja el nombre vacío para terminar): ").strip()
        if name == "":
            break

        grades = []
        for module in MODULES:
            while True:
                try:
                    grade = float(input(f"Calificación en {module}: "))
                    if 0 <= grade <= 10:
                        grades.append(grade)
                        break
                    else:
                        print("Por favor, introduce una nota entre 0 y 10.")
                except ValueError:
                    print("Por favor, introduce un número válido.")
        students.append({"name": name, "grades": grades})

def print_all_grades():
    print("\nCalificaciones del curso completo:")
    for student in students:
        grades_str = ""
        for i in range(len(MODULES)):
            grades_str += f"{MODULES[i]}: {student['grades'][i]}"
            if i < len(MODULES) - 1:
                grades_str += ", "
        print(f"{student['name']}: {grades_str}")

def print_student_grades():
    name = input("Introduce el nombre y apellidos del alumno: ").strip()
    found = False
    for student in students:
        if student['name'].lower() == name.lower():
            found = True
            print(f"Calificaciones de {student['name']}:")
            for i in range(len(MODULES)):
                print(f"  {MODULES[i]}: {student['grades'][i]}")
            break
    if not found:
        print("Alumno no encontrado.")

def calculate_average_grade():
    module = input("Introduce el módulo: ").strip().upper()
    if module in MODULES:
        index = MODULES.index(module)
        total_grades = 0
        for student in students:
            total_grades += student['grades'][index]
        average = total_grades / len(students)
        print(f"Nota media en {module}: {average:.2f}")
    else:
        print("Módulo no encontrado.")

def calculate_max_grade():
    module = input("Introduce el módulo: ").strip().upper()
    if module in MODULES:
        index = MODULES.index(module)
        max_grade = -1
        max_student = None
        for student in students:
            if student['grades'][index] > max_grade:
                max_grade = student['grades'][index]
                max_student = student
        print(f"Nota máxima en {module}: {max_grade} ({max_student['name']})")
    else:
        print("Módulo no encontrado.")

def calculate_min_grade():
    module = input("Introduce el módulo: ").strip().upper()
    if module in MODULES:
        index = MODULES.index(module)
        min_grade = 11  # Dado que las notas son entre 0 y 10
        min_student = None
        for student in students:
            if student['grades'][index] < min_grade:
                min_grade = student['grades'][index]
                min_student = student
        print(f"Nota más baja en {module}: {min_grade} ({min_student['name']})")
    else:
        print("Módulo no encontrado.")

def list_sorted_by_grades():
    module = input("Introduce el módulo: ").strip().upper()
    if module in MODULES:
        index = MODULES.index(module)

        # Ordenamos manualmente con el algoritmo de burbuja
        for i in range(len(students)):
            for j in range(i + 1, len(students)):
                if students[i]['grades'][index] < students[j]['grades'][index]:
                    # Intercambiar los estudiantes
                    students[i], students[j] = students[j], students[i]

        print(f"Listado ordenado por notas en {module}:")
        for student in students:
            print(f"{student['name']}: {student['grades'][index]}")
    else:
        print("Módulo no encontrado.")

def menu():
    while True:
        print("\nMenú:")
        print("1. Imprimir todas las calificaciones.")
        print("2. Imprimir calificaciones de un alumno.")
        print("3. Calcular nota media de un módulo.")
        print("4. Calcular nota máxima de un módulo.")
        print("5. Calcular nota más baja de un módulo.")
        print("6. Listado ordenado por notas en un módulo.")
        print("0. Salir.")

        option = input("Elige una opción: ").strip()
        match option:
            case "1":
                print_all_grades()

            case "2":
                print_student_grades()

            case "3":
                calculate_average_grade()

            case "4":
                calculate_max_grade()

            case "5":
                calculate_min_grade()

            case "6":
                list_sorted_by_grades()

            case "0":
                break

            case _:
                print("Opción no válida. Por favor, elige una opción correcta.")

def main():

    # Función principal para ejecutar el programa.
    print("Gestionar las calificaciones de los estudiantes en varios módulos")
    print("-----------------------------------------------------------------")

    input_student_data()
    menu()

if __name__ == "__main__":
    main()
