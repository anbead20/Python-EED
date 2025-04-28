"""
Este programa pide dos valores (a y b) y muestra un menú con cinco opciones: sumar, restar, multiplicar, dividir y
terminar. La primera opción permite introducir los valores de las variables a y b, que se inicializan a cero al
comenzar. Las demás opciones no se podrán ejecutar hasta que se introduzcan correctamente las variables.

Autor: Adrián Anta Bellido
"""

from ej1_v1 import add, subtract, multiply, split, show_menu

def main():
    print("Este programa realiza operaciones matemáticas con dos valores, a y b.")
    print("---------------------------------------------------------------------\n")

    a = 0
    b = 0
    values_set = False

    while True:
        show_menu()
        option = input("Selecciona una opción: ")

        if option == "0":
            a = float(input("Introduce el valor de a: "))
            b = float(input("Introduce el valor de b: "))
            values_set = True
        elif option in ["1","2", "3", "4"]:
            if not values_set:
                print("Error: ¡Primero debes introducir los valores de a y b!\n")
            else:
                if option == "1":
                    print(f"Resultado de la suma: {add(a, b)}")
                elif option == "2":
                    print(f"Resultado de la resta: {subtract(a, b)}")
                elif option == "3":
                    print(f"Resultado de la multiplicación: {multiply(a, b)}")
                elif option == "4":
                    print(f"Resultado de la división: {split(a, b)}")
        elif option == "5":
            print("Finalizando el programa...")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción correcta.")

if __name__ == "__main__":
    main()