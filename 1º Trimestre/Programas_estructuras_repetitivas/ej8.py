"""
Este programa muestra un cronómetro que cuenta las horas, minutos y segundos.
Autor: Adrián Anta Bellido
"""

import time

# Presentación del programa
print("Bienvenido al cronómetro.")
print("El cronómetro comenzará a contar desde 0.")

# Inicializar horas, minutos y segundos
hours = 0
minutes = 0
seconds = 0

# Mostrar el cronómetro en un bucle
while True:
    print(f"\r{hours:02}:{minutes:02}:{seconds:02}", end="")

    # Esperar 1 segundo
    time.sleep(1)

    # Incrementar los segundos
    seconds += 1

    # Verificar si se debe incrementar los minutos
    if seconds == 60:
        seconds = 0
        minutes += 1

    # Verificar si se debe incrementar las horas
    if minutes == 60:
        minutes = 0
        hours += 1


