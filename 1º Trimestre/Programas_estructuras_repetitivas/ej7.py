"""
Este programa calcula el pago mensual y el total a pagar después de 20 meses
de acuerdo con un esquema de pagos en el que el monto a pagar aumenta cada mes.
Autor: Adrián Anta Bellido
"""

# Presentación del programa
print("Bienvenido al programa que calcula el pago mensual y total después de 20 meses")
print("------------------------------------------------------------------------------")

# Definir variables
TOTAL_MONTHS = 20  # Total de meses

monthly_payments = []  # Lista para almacenar los pagos mensuales
total_payment = 0  # Variable para almacenar el total a pagar

# Calcular los pagos mensuales y el total
for month in range(1, TOTAL_MONTHS + 1):
    monthly_payment = 10 * (2 ** (month - 1))  # Cálculo del pago mensual
    monthly_payments.append(monthly_payment)
    total_payment += monthly_payment  # Sumar al total

# Mostrar los resultados
print("Pagos mensuales:", monthly_payments)
print(f"Total a pagar después de {TOTAL_MONTHS} meses: {total_payment:.2f} €")
