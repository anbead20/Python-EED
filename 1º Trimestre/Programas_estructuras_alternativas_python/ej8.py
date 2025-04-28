"""
Este programa solicita la nota, la edad y el sexo de una persona,
y determina si la solicitud es aceptada, posible o no aceptada
según las condiciones establecidas.
Autor: Adrián Anta Bellido
"""

# Solicitar la nota, la edad y el sexo al usuario
nota = float(input("Introduce la nota: "))
edad = int(input("Introduce la edad: "))
sexo = input("Introduce el sexo (F/M): ").strip().upper()

# Determinar el mensaje según las condiciones
if nota >= 5 and edad >= 18:
    if sexo == 'F':
        print("ACEPTADA")
    elif sexo == 'M':
        print("POSIBLE")
    else:
        print("NO ACEPTADA")  # En caso de que el sexo no sea F ni M
else:
    print("NO ACEPTADA")
