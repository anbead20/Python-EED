# Programa para intercambiar los valores de dos variables

# Solicitar los valores de A y B al usuario
A = float(input("Introduce el valor de A: "))
B = float(input("Introduce el valor de B: "))

# Intercambiar los valores
A, B = B, A

# Mostrar los valores intercambiados
print(f"Después del intercambio, el valor de A es: {A}")
print(f"Después del intercambio, el valor de B es: {B}")
