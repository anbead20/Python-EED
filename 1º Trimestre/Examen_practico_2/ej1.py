"""
Haz un programa que utilice una matriz de 3x3 y ofrezca un menú con las siguientes opciones:

1. Rellenar la matriz con números aleatorios entre 1 y 100.
2. Rellenar la matriz con números aleatorios entre 1 y 100 sin que se repitan.
3. Desplazar todos los números una posición hacia la derecha.
4. Desplazar todos los números una posición hacia abajo.
5. Calcular la suma de los elementos de una fila.
6. Modificar un elemento de la matriz.
7. Mostrar la matriz.
8. Salir del programa.

La matriz tiene que ser una variable global, llámala matrix. Créala, antes de mostrar el menú, rellena de
ceros.
Cada opción del menú, excepto la de salir, llama a una función. Si no sabes hacerlo con funciones, hazlo
sin ellas, pero se penalizará con 2 puntos.
Si la opción 1 o 2 del menú no se han ejecutado, las demás (salvo la de salir) no funcionan y debes
mostrar que hasta que alguna de esas opciones no se ejecute, no funcionará.
Controla que las opciones del menú introducidas por el usuario son correctas.

Autor: Adrián Anta Bellido
"""

import random

ROWS = 3
COLUMNS = 3
LOWEST_NUM = 1
BIGGEST_NUM = 100
WIDTH_NUMBER = 3

matrix = [[0] * COLUMNS for _ in range(ROWS)]
data_initialized = False

def main():
    print("Programa que utiliza una matriz 3x3 y ofrece un menú")
    print("----------------------------------------------------")
    while True:
        menu()

def menu():
    global data_initialized

    print("\nMenú de opciones:")
    print("-----------------")
    print("1. Rellenar la matriz con números aleatorios entre 1 y 100.")
    print("2. Rellenar la matriz con números aleatorios entre 1 y 100 sin que se repitan.")
    print("3. Desplazar todos los números una posición hacia la derecha.")
    print("4. Desplazar todos los números una posición hacia abajo.")
    print("5. Calcular la suma de los elementos de una fila.")
    print("6. Modificar un elemento de la matriz.")
    print("7. Mostrar la matriz.")
    print("8. Salir del programa.")

    option = input("\nElige una de las opciones (1-8): ")

    if option in ("3", "4", "5", "6", "7") and not data_initialized:
        print("Debes rellenar la matriz primero usando las opciones 1 o 2.")
        return

    if option == "1":
        fill(LOWEST_NUM, BIGGEST_NUM)
    elif option == "2":
        fill(LOWEST_NUM, BIGGEST_NUM, repeatable=False)
    elif option == "3":
        shift_right()
    elif option == "4":
        shift_down()
    elif option == "5":
        show_sum_row()
    elif option == "6":
        update_element()
    elif option == "7":
        show()
    elif option == "8":
        print("Has salido del programa.")
        exit()
    else:
        print("No has introducido una opción correcta.")

def fill(low, high, repeatable=True):
    global matrix, data_initialized
    used_numbers = []
    for row in range(ROWS):
        for column in range(COLUMNS):
            while True:
                number = random.randint(low, high)
                if repeatable or number not in used_numbers:
                    matrix[row][column] = number
                    used_numbers.append(number)
                    break
    data_initialized = True
    print("Matriz rellenada correctamente.")

def shift_right():
    print("\nDesplazando la matriz una posición hacia la derecha...")
    for row in matrix:
        last = row[COLUMNS - 1]
        for i in range(COLUMNS - 1, 0, -1):
            row[i] = row[i - 1]
        row[0] = last

def shift_down():
    print("\nDesplazando la matriz una posición hacia abajo...")
    for col in range(COLUMNS):
        last = matrix[ROWS-1][col]
        for row in range(ROWS-1, -1, -1):
            matrix[row][col] = matrix[row-1][col]
        matrix[0][col] = last

def show_sum_row():
    while True:
        row = input("\nIntroduce el número de fila (1-3): ")
        if row.isdigit() and 1 <= int(row) <= 3:
            row = int(row) - 1
            break
        else:
            print("Fila no válida. Debe ser un número entre 1 y 3.")

    row_sum = 0
    for col in range(COLUMNS):
        row_sum += matrix[row][col]
    print(f"La suma de los elementos de la fila {row + 1} es: {row_sum}")

def update_element():
    while True:
        row = input("\nIntroduce la fila (1-3): ")
        column = input("Introduce la columna (1-3): ")
        if row.isdigit() and column.isdigit() and 1 <= int(row) <= 3 and 1 <= int(column) <= 3:
            row, column = int(row) - 1, int(column) - 1
            break
        else:
            print("Fila o columna no válida. Deben ser números entre 1 y 3.")

    print(f"El elemento actual en ({row + 1}, {column + 1}) es: {matrix[row][column]}")
    confirmation = input("¿Quieres cambiarlo? (Sí/No): ").strip().lower()
    if confirmation in ("sí", "si"):
        new_value = input("Introduce el nuevo valor: ")
        if new_value.isdigit():
            new_value = int(new_value)
            if 0 < new_value <= 100:
                matrix[row][column] = new_value
                print("Elemento actualizado correctamente.")
            else:
                print("ERROR. Has introducido un valor mayor a 100 o menor/igual a 0.")
        else:
            print("Valor no válido. Debe ser un número entero.")
    else:
        print("No se ha realizado ningún cambio.")

def show():
    print("\nMatriz actual:\n")
    for row in range(ROWS):
        for col in range(COLUMNS):
            print(f"{matrix[row][col]:{WIDTH_NUMBER}}", end=" ")
        print()

if __name__ == "__main__":
    main()
