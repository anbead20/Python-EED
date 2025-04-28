# Programa para calcular el monto final después de un descuento

# Solicitar el total de la compra al usuario
total_purchase = float(input("Introduce el total de la compra: "))

# Calcular el descuento (15% del total de la compra)
discount = total_purchase * 0.15

# Calcular el monto final a pagar
final_amount = total_purchase - discount

# Mostrar los resultados
print(f"El monto del descuento es: {discount}")
print(f"El monto final a pagar es: {final_amount}")
