# Programa para convertir minutos a horas y minutos

# Solicitar la cantidad de minutos al usuario
total_minutes = int(input("Introduce la cantidad de minutos: "))

# Calcular horas y minutos
hours = total_minutes // 60
minutes = total_minutes % 60

# Mostrar el resultado
print(f"{total_minutes} minutos son {hours} horas y {minutes} minutos.")
