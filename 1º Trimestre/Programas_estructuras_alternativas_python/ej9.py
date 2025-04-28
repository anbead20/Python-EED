"""
Este programa lee un carácter del teclado y determina si es un signo de puntuación,
una letra, un dígito, otro carácter o si no es un carácter válido.
Autor: Adrián Anta Bellido
"""

# Solicitar un carácter al usuario
input_char = input("Introduce un carácter: ")

# Comprobar si el usuario ha introducido más de un carácter
if len(input_char) != 1:
    print("No es un carácter.")
else:
    # Definir los signos de puntuación
    punctuation = ".,;:!?¿¡\"'()[]{}<>"

    # Determinar la categoría del carácter
    if input_char in punctuation:
        print("Es signo de puntuación.")
    elif input_char.isalpha():
        print("Es una letra.")
    elif input_char.isdigit():
        print("Es un dígito.")
    else:
        print("Es otro carácter.")
