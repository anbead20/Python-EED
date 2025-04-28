# Programa para calcular el total de dinero en euros y céntimos

# Solicitar la cantidad de monedas de cada tipo
coins_2e = int(input("Introduce la cantidad de monedas de 2 euros: "))
coins_1e = int(input("Introduce la cantidad de monedas de 1 euro: "))
coins_50c = int(input("Introduce la cantidad de monedas de 50 céntimos: "))
coins_20c = int(input("Introduce la cantidad de monedas de 20 céntimos: "))
coins_10c = int(input("Introduce la cantidad de monedas de 10 céntimos: "))

# Calcular el total en céntimos
total_cents = (coins_2e * 200) + (coins_1e * 100) + (coins_50c * 50) + (coins_20c * 20) + (coins_10c * 10)

# Convertir el total a euros y céntimos
total_euros = total_cents // 100
remaining_cents = total_cents % 100

# Mostrar el resultado
print(f"Tienes un total de {total_euros} euros y {remaining_cents} céntimos.")
