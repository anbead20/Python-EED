"""
Este programa sustituye las vocales 'a', 'e', 'i', 'o' por los números '4', '3', '1' y '0'
respectivamente en una cadena de texto proporcionada por el usuario.
Autor: Adrián Anta Bellido
"""

# Presentación del programa
print("Este programa sustituye las vocales 'a', 'e', 'i', 'o' por los números '4', '3', '1' y '0' respectivamente")
print("----------------------------------------------------------------------------------------------------------\n")

# Solicitar la cadena de texto al usuario
text = input("Ingrese la cadena de texto: ")

modified_text = ""
change = str.maketrans("aeio", "4310")

for char in text:
    if char == 'a':
        modified_text += char.translate(change)
    elif char == 'e':
        modified_text += char.translate(change)
    elif char == 'i':
        modified_text += char.translate(change)
    elif char == 'o':
        modified_text += char.translate(change)
    else:
        modified_text += char

# Mostrar la cadena resultante
print("La cadena modificada es:", modified_text)
