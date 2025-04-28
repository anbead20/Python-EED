"""
Este programa pide la temperatura media de cada mes de un año y luego muestra un diagrama de barras horizontales
con esos datos usando asteriscos.

Autor: Adrián Anta Bellido
"""

print("Este programa solicita la temperatura media de cada mes de un año y muestra un diagrama de barras horizontales")
print("con esos datos usando asteriscos.")
print("----------------------------------------------------------------------------------------------------------\n")

temperatures = []

# Pedimos la temperatura media para cada mes
for month in range(1, 13):
    temperature = float(input(f"Introduce la temperatura media de mes {month}: "))
    temperatures.append(temperature)

# Mostramos el diagrama de barras horizontales
print("\nDiagrama de barras horizontales (temperaturas medias):")
for i, temp in enumerate(temperatures, start=1):
    print(f"Mes {i}: {'*' * int(temp)}")
