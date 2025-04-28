"""
Este programa pide dos valores (a y b) y muestra un menú con cinco opciones: sumar, restar, multiplicar, dividir y
terminar. Cada opción llama a una función correspondiente, pasando las dos variables, y muestra el resultado de la
operación. Si se introduce una opción incorrecta, se muestra un mensaje de error. El menú se volverá a mostrar hasta
que se seleccione la opción de terminar.

Autor: Adrián Anta Bellido
"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def split(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

def show_menu():
    print("Menú:")
    print("0. Introducir valores")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Terminar")

def main():
    print("Este programa realiza operaciones matemáticas con dos valores: a y b.")
    print("----------------------------------------------------------------------------------------------------------\n")

    a = float(input("Introduce el valor de a: "))
    b = float(input("Introduce el valor de b: "))

    while True:
        show_menu()
        option = input("Selecciona una opción: ")

        if option == "0":
            a = float(input("Introduce el valor de a: "))
            b = float(input("Introduce el valor de b: "))
        elif option == "1":
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