"""
Este programa cifra una cadena utilizando el cifrado César, desplazando cada letra un número
específico de lugares en el alfabeto, según un desplazamiento proporcionado por el usuario.
Autor: Adrián Anta Bellido
"""

print("Este programa cifra una cadena de texto utilizando el cifrado César")
print("-------------------------------------------------------------------\n")

# Solicitar la cadena y el desplazamiento
text = input("Ingrese la cadena de texto a cifrar: ")
shift = int(input("Ingrese el número de desplazamiento: "))

encrypted_text = ""

for char in text:
    if char.isalpha():
        # Determinar si la letra es mayúscula o minúscula
        start = ord('A') if char.isupper() else ord('a')
        # Desplazar la letra en el alfabeto
        encrypted_text += chr(start + (ord(char) - start + shift) % 26)
    else:
        encrypted_text += char

# Mostrar la cadena cifrada
print("La cadena cifrada es:", encrypted_text)
