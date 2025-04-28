"""
Programa para calcular la hora de llegada de un ciclista.
Autor: Adrián Anta Bellido
"""

print("Tienes que introducir los siguientes datos de un ciclista")
print("---------------------------------------------------------")

# Solicitar la hora de partida
start_hours = int(input("Introduce la hora de partida: "))
start_minutes = int(input("Introduce los minutos de partida: "))
start_seconds = int(input("Introduce los segundos de partida: "))

# Solicitar el tiempo de viaje en segundos
travel_time = int(input("Introduce el tiempo de viaje en segundos: "))

# Calcular el tiempo total de llegada en segundos
total_start_seconds = start_hours * 3600 + start_minutes * 60 + start_seconds
total_arrival_seconds = total_start_seconds + travel_time

# Convertir los segundos totales a horas, minutos y segundos
arrival_hours = total_arrival_seconds // 3600
arrival_minutes = (total_arrival_seconds % 3600) // 60
arrival_seconds = total_arrival_seconds % 60

# Mostrar la hora de llegada
print(f"La hora de llegada a la ciudad B es: {arrival_hours:02}:{arrival_minutes:02}:{arrival_seconds:02}")
