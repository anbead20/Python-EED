# Programa para mostrar suma, resta, división y multiplicación de dos números

# Solicitar dos números al usuario
number1 = float(input("Introduce el primer número: "))
number2 = float(input("Introduce el segundo número: "))

# Realizar las operaciones
sum_result = number1 + number2
difference = number1 - number2
multiplication = number1 * number2

# Comprobamos si el segundo número no es 0 para evitar división por cero
if number2 != 0:
    division = number1 / number2
else:
    division = "No se puede dividir por cero"

# Mostrar los resultados
print(f"La suma es: {sum_result}")
print(f"La resta es: {difference}")
print(f"La multiplicación es: {multiplication}")
print(f"La división es: {division}")
