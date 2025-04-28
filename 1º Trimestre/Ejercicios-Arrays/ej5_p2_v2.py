import random


# Definición de la función para llenar la matriz con números únicos
def fill_matrix(rows, cols, num_min, num_max):
    matrix = []
    used_numbers = []

    # Llenar la matriz con números únicos
    for i in range(rows):
        row = []
        for j in range(cols):
            while True:
                num = random.randint(num_min, num_max)
                if num not in used_numbers:  # Si el número no ha sido usado
                    row.append(num)
                    used_numbers.append(num)
                    break
        matrix.append(row)

    return matrix


# Definición de la función para encontrar el máximo y el mínimo
def find_max_min(matrix):
    max_value = matrix[0][0]
    min_value = matrix[0][0]
    max_pos = min_pos = (0, 0)

    # Recorrer la matriz para encontrar el máximo y el mínimo
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > max_value:
                max_value = matrix[i][j]
                max_pos = (i, j)
            if matrix[i][j] < min_value:
                min_value = matrix[i][j]
                min_pos = (i, j)

    return max_value, min_value, max_pos, min_pos


# Definición de la función para mostrar la matriz
def print_matrix(matrix):
    print("\nMatriz generada:")
    for row in matrix:
        for num in row:
            print(f"{num:4}", end=" ")
        print()


def main():
    print("Este programa llena un array de 6 filas por 10 columnas con números entre 0 y 1000,")
    print("sin repeticiones, y muestra las posiciones del número más grande y más pequeño.")
    print("-------------------------------------------------------------------------------------------------------")

    rows, cols = 6, 10
    num_min, num_max = 0, 1000

    # Llamar a la función para llenar la matriz
    matrix = fill_matrix(rows, cols, num_min, num_max)

    # Llamar a la función para encontrar el máximo y el mínimo
    max_value, min_value, max_pos, min_pos = find_max_min(matrix)

    # Mostrar la matriz generada
    print_matrix(matrix)

    # Mostrar los resultados
    print(f"\nEl valor máximo es {max_value} y se encuentra en la posición {max_pos}.")
    print(f"El valor mínimo es {min_value} y se encuentra en la posición {min_pos}.")


if __name__ == "__main__":
    main()
