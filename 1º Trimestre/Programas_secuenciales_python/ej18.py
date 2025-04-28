# Programa para mostrar las iniciales de una persona

# Solicitar el nombre y los apellidos al usuario
first_name = input("Introduce el nombre: ")
last_name1 = input("Introduce el primer apellido: ")
last_name2 = input("Introduce el segundo apellido: ")

# Obtener las iniciales (la primera letra de cada palabra)
initials = first_name[0].upper() + last_name1[0].upper() + last_name2[0].upper()

# Mostrar las iniciales
print(f"Las iniciales de la persona son: {initials}")
