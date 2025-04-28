# Programa para calcular en qué tiempo un vehículo más rápido alcanzará al más lento

# Solicitar la distancia entre los vehículos (en km) y sus velocidades (en km/h)
distance = float(input("Introduce la distancia entre los dos vehículos (en km): "))
v1 = float(input("Introduce la velocidad del vehículo más lento (en km/h): "))
v2 = float(input("Introduce la velocidad del vehículo más rápido (en km/h): "))

# Comprobar que el vehículo más rápido realmente tiene una mayor velocidad
if v2 > v1:
    # Calcular el tiempo en horas en que el vehículo más rápido alcanzará al más lento
    time_hours = distance / (v2 - v1)

    # Convertir el tiempo a minutos
    time_minutes = time_hours * 60

    # Mostrar el resultado
    print(f"El vehículo más rápido alcanzará al más lento en {time_minutes:.2f} minutos.")
else:
    print("El vehículo más rápido debe tener una velocidad mayor que el más lento.")
