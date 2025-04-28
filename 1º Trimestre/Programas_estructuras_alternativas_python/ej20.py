"""
Este programa calcula el costo del servicio de transporte internacional basado en el peso del paquete y la zona de entrega.
Autor: Adrián Anta Bellido
"""

# Entrada de los datos
zone = int(input("Ingrese la zona (1-5): "))
weight_kg = float(input("Ingrese el peso del paquete en kg: "))

# Verificación del peso del paquete
if weight_kg > 5:
    print("El paquete no puede ser transportado. Peso máximo permitido es 5 kg.")
else:
    # Definición de costos por gramo según la zona
    match zone:
        case 1:
            cost_per_gram = 24.00
        case 2:
            cost_per_gram = 20.00
        case 3:
            cost_per_gram = 21.00
        case 4:
            cost_per_gram = 10.00
        case 5:
            cost_per_gram = 18.00
        case _:
            print("ERROR: Zona no válida. Debe ser un número entre 1 y 5.")
            exit()

    # Cálculo del costo
    cost = weight_kg * 1000 * cost_per_gram  # Convertir kg a gramos y calcular costo
    print(f"El costo de transporte del paquete es: {cost:.2f} euros.")
