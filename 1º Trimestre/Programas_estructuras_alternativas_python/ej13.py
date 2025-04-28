"""
Este programa calcula el desglose mínimo en billetes y monedas de una cantidad exacta de euros.
Autor: Adrián Anta Bellido
"""

# Entrada de la cantidad de euros
amount = int(input("Ingrese la cantidad exacta de euros: "))

# Definición de los billetes y monedas disponibles
bills = [500, 200, 100, 50, 20, 10, 5]
coins = [2, 1]

# Desglose de billetes
print("Desglose de billetes y monedas:")
for bill in bills:
    num_bills = amount // bill
    if num_bills > 0:
        print(f"{num_bills} billete(s) de {bill} euros.")
        amount %= bill

# Desglose de monedas
for coin in coins:
    num_coins = amount // coin
    if num_coins > 0:
        print(f"{num_coins} moneda(s) de {coin} euros.")
        amount %= coin
