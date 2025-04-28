"""
Este programa reemplaza las palabras en una lista negra por asteriscos en una cadena dada.
Las palabras en la lista negra y la cadena son ingresadas por el usuario.
Autor: Adrián Anta Bellido
"""

# Presentación del programa
print("Este programa reemplaza las palabras en una lista negra por asteriscos en una cadena dada")
print("-----------------------------------------------------------------------------------------\n")

# Solicitar la cadena y las palabras de la lista negra
text = input("Ingrese la cadena de texto: ")
blacklist_input = input("Ingrese las palabras de la lista negra, separadas por comas: ")

# Convertir la lista negra en una lista real
blacklist = blacklist_input.split(',')

# Reemplazar las palabras de la lista negra con asteriscos
for word in blacklist:
    word = word.strip()  # Eliminar espacios extra alrededor de la palabra
    text = text.replace(word, '*' * len(word))

# Mostrar la cadena resultante
print("La cadena después de los reemplazos es:", text)
