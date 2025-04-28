"""
Programa para convertir mayúsculas a minúsculas y viceversa en una cadena introducida por el usuario usando una estructura repetitiva.
El programa solicita una cadena y luego invierte el caso de cada letra usando un bucle.
Autor: Adrián Anta Bellido
"""

# Presentación del programa
print("Bienvenido al conversor de mayúsculas y minúsculas.")
print("Introduce una cadena y cambiaré cada letra mayúscula a minúscula y cada minúscula a mayúscula.")

# Solicitar la cadena
text = input("Introduce una cadena: ")

# Convertir mayúsculas a minúsculas y viceversa usando una estructura repetitiva
converted_text = ""
for char in text:
    if char.isupper():
        converted_text += char.lower()  # Convertir a minúscula si es mayúscula
    elif char.islower():
        converted_text += char.upper()  # Convertir a mayúscula si es minúscula
    else:
        converted_text += char  # Mantener el carácter sin cambio si no es una letra

# Mostrar el resultado
print(f"Cadena convertida: {converted_text}")
