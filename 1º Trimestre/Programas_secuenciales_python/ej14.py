# Programa para invertir un número de dos cifras

# Solicitar un número de dos cifras al usuario
number = int(input("Introduce un número de dos cifras: "))

# Separar las decenas y las unidades
tens = number // 10
units = number % 10

# Invertir el número
inverted_number = (units * 10) + tens

# Mostrar el resultado
print(f"El número invertido es: {inverted_number}")
