"""
Este programa simula las estaturas de personas en diferentes países mediante un array de 4 filas por 10 columnas
con números aleatorios generados entre 140 y 210. Luego, calcula la estatura media, mínima y máxima de cada país.

Autor: Adrián Anta Bellido
"""

import random

print("Este programa simula las estaturas de personas en diferentes países mediante un array de 4 filas por 10 columnas,")
print("-----------------------------------------------------------------------------------------------------------------\n")

# Constantes y datos
ROWS, COLUMNS = 4, 10
HEIGHT_MIN, HEIGHT_MAX = 140, 210
countries = ["España", "Rusia", "Japón", "Australia"]

# Generar la matriz de estaturas
heights = [[random.randint(HEIGHT_MIN, HEIGHT_MAX) for _ in range(COLUMNS)] for _ in range(ROWS)]

# Mostrar los datos por país
for row in range(ROWS):
    country = countries[row]
    height_values = heights[row]
    average_height = sum(height_values) / len(height_values)
    min_height = min(height_values)
    max_height = max(height_values)

    # Mostrar datos del país
    print(f"{country}: ", end="")
    for height in height_values:
        print(f"{height:3}", end=" ")
    print(f"| Media: {average_height:.2f} | Mín: {min_height} | Máx: {max_height}")
