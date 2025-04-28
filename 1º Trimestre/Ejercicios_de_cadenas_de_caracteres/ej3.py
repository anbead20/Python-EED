"""
Este programa solicita al usuario una cadena y dos índices,
luego extrae y muestra la subcadena entre esos índices.
Permite continuar el proceso hasta que el usuario decida detenerse.
Autor: Adrián Anta Bellido
"""

print("Este programa le permite ingresar una cadena y dos índices")
print("----------------------------------------------------------\n")

while True:
    # Pedir la cadena y los índices
    cadena = input("Ingrese una cadena: ")
    try:
        inicio = int(input("Ingrese el índice inicial: "))
        fin = int(input("Ingrese el índice final: "))

        # Verificar y extraer la subcadena si los índices son válidos
        if 0 <= inicio < fin <= len(cadena):
            print("La subcadena es:", cadena[inicio:fin])
        else:
            print("Índices inválidos. Asegúrese de que están en el rango y que el inicial es menor que el final.")
    except ValueError:
        print("Por favor, ingrese números válidos para los índices.")

    # Preguntar si el usuario quiere continuar
    if input("¿Quiere continuar? (s/n): ").lower() != 's':
        print("Gracias por usar el programa.")
        break
