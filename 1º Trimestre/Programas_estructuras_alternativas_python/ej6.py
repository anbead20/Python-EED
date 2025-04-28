"""
Este programa solicita una letra al usuario y verifica si es una letra mayúscula.
Autor: Adrián Anta Bellido
"""

# Solicitar una letra al usuario
letter = input("Introduce una letra: ")

# Verificar si es una letra
if letter != 1:
    print("No es una letra")

# Verificar si es una letra mayúscula
elif letter.isupper():
    print(f"La letra '{letter}' es mayúscula.")
else:
    print(f"La letra '{letter}' no es mayúscula.")
