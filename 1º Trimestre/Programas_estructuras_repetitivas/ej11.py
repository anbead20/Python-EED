"""
Programa para contar el número de palabras en una frase introducida por el usuario usando una estructura repetitiva simple.
El programa solicita una frase y cuenta las palabras considerando los espacios como separadores.
Autor: Adrián Anta Bellido
"""

# Presentación del programa
print("Bienvenido al contador de palabras.")
print("Introduce una frase y contaré cuántas palabras tiene.\n")

# Solicitar la entrada de una frase
phrase = input("Introduce una frase: ")

# Contador de palabras
word_count = 1 if phrase else 0  # Inicia en 1 si la frase no está vacía

# Contar espacios para determinar el número de palabras
for char in phrase:
    if char == " ":
        word_count += 1

# Mostrar el resultado
print(f"La frase introducida tiene {word_count} palabras.")
