"""
Este programa solicita la base y el exponente al usuario y calcula la potencia.
Se manejan tres casos:
1. Exponente positivo: se calcula la potencia normalmente.
2. Exponente cero: el resultado es 1.
3. Exponente negativo: el resultado es 1 dividido por la potencia con el exponente positivo.
Autor: Adrián Anta Bellido
"""

# Solicitar la base y el exponente al usuario
base = float(input("Introduce la base: "))
exponent = int(input("Introduce el exponente: "))

# Calcular la potencia según el valor del exponente
if exponent > 0:
    result = base ** exponent
    print(f"{base} elevado a {exponent} es: {result}")
elif exponent == 0:
    print(f"Cualquier número elevado a 0 es: 1")
else:  # exponent < 0
    result = 1 / (base ** abs(exponent))
    print(f"{base} elevado a {exponent} es: {result}")
