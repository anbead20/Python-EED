# Programa para calcular las comisiones y el total a recibir de un vendedor

# Solicitar el sueldo base al usuario
base_salary = float(input("Introduce el sueldo base del vendedor: "))

# Solicitar las tres ventas al usuario
sale1 = float(input("Introduce el valor de la primera venta: "))
sale2 = float(input("Introduce el valor de la segunda venta: "))
sale3 = float(input("Introduce el valor de la tercera venta: "))

# Calcular el total de las ventas
total_sales = sale1 + sale2 + sale3

# Calcular la comisión (10% de las ventas)
commission = total_sales * 0.10

# Calcular el total que recibirá el vendedor
total_payment = base_salary + commission

# Mostrar los resultados
print(f"Las comisiones por ventas son: {commission}")
print(f"El total que recibirá en el mes es: {total_payment}")
