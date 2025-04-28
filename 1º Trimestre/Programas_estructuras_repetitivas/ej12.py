"""
Programa para reemplazar un carácter en una cadena por otro introducido por el usuario.
Solicita una cadena y dos caracteres individuales. Validar que los caracteres sean válidos antes de realizar el reemplazo.
Autor: Adrián Anta Bellido
"""

# Presentación del programa
print("Bienvenido al programa de reemplazo de caracteres.")
print("Introduce una cadena y dos caracteres. El primer carácter será reemplazado por el segundo en la cadena.\n")

# Solicitar la cadena
text = input("Introduce una cadena: ")

# Solicitar y validar el primer carácter
while True:
    char_to_replace = input("Introduce el carácter a reemplazar: ")
    if len(char_to_replace) == 1:
        break
    print("Por favor, introduce solo un carácter.")

# Solicitar y validar el segundo carácter
while True:
    replacement_char = input("Introduce el carácter de reemplazo: ")
    if len(replacement_char) == 1:
        break
    print("Por favor, introduce solo un carácter.")

# Reemplazar el primer carácter por el segundo en la cadena
new_text = text.replace(char_to_replace, replacement_char)

# Mostrar el resultado
print(f"\nCadena resultante: {new_text}")
