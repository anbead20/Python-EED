"""
Este programa pide al usuario que ingrese una cadena y un delimitador, luego divide la cadena
en una lista utilizando el delimitador proporcionado, y finalmente une esa lista con un delimitador
diferente también dado por el usuario.
Autor: Adrián Anta Bellido
"""

print("Este programa le permitirá dividir una cadena usando un delimitador y luego unirla usando otro delimitador")
print("----------------------------------------------------------------------------------------------------------\n")

# Solicitar la cadena, el delimitador de división y el delimitador de unión
text = input("Ingrese la cadena de texto: ")
split_delimiter = input("Ingrese el delimitador para dividir la cadena: ")
join_delimiter = input("Ingrese el delimitador para unir la lista: ")

# Dividir la cadena utilizando el delimitador de división
split_list = text.split(split_delimiter)

# Unir la lista usando el delimitador de unión
joined_text = join_delimiter.join(split_list)

# Mostrar el resultado
print("La cadena unida es:", joined_text)
