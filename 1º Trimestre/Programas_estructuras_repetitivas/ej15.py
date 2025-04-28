"""
Introducir una cadena de caracteres e indicar si es un palíndromo. Una palabra palíndroma es aquella que se lee
igual adelante que atrás.
Autor: Adrián Anta Bellido
"""

print("Programa que introduces una cadena e indica si es un palíndroma")
print("---------------------------------------------------------------\n")

main_string = input("Introduce una cadena: ").lower()

VOCALS_WITH_ACCENT = "áéíóú"
VOCALS = "aeiou"
string_to_check = ""
is_palindrome = True

for char in main_string:
    if char != "":
        if char in VOCALS_WITH_ACCENT:
            char = VOCALS[VOCALS_WITH_ACCENT.find(char)]
        string_to_check += char

if string_to_check != "":
    is_palindrome = True
else:
    print("No has introducido una cadena")
    exit()

for i in range(len(string_to_check)):
        if string_to_check[i] != string_to_check[-(i + 1)]:
            is_palindrome = False
            break

if is_palindrome:
    print("La cadena es un palíndromo.")
else:
    print("La cadena no es un palíndromo.")