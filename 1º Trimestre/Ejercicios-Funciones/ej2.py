"""
Crea una biblioteca de funciones numéricas que contenga las siguientes funciones. Recuerda que puedes usar unas dentro
de otras si es necesario.

Autor: Adrián Anta Bellido
"""


def is_palindrome(num):
    """Devuelve True si el número es capicúa, False en caso contrario."""
    return num == reverse_number(num)

def is_prime(num):
    """Devuelve True si el número es primo, False en caso contrario."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def next_prime(num):
    """Devuelve el menor primo mayor que el número dado."""
    num += 1
    while not is_prime(num):
        num += 1
    return num

def digit_count(num):
    """Devuelve el número de dígitos de un número entero."""
    return len(str(abs(num)))

def reverse_number(num):
    """Devuelve el número invertido."""
    reversed_num = 0
    while num != 0:
        reversed_num = reversed_num * 10 + num % 10
        num //= 10
    return reversed_num

def digit_at(num, pos):
    """Devuelve el dígito en la posición indicada."""
    num = abs(num)
    return int(str(num)[pos])

def digit_position(num, digit):
    """Devuelve la posición de la primera ocurrencia del dígito, o -1 si no está."""
    num = abs(num)
    num_str = str(num)
    return num_str.find(str(digit))

def remove_from_back(num, count):
    """Le quita count dígitos al número por detrás."""
    return num // (10**count)

def remove_from_front(num, count):
    """Le quita count dígitos al número por delante."""
    num = abs(num)
    return int(str(num)[count:]) if count < len(str(num)) else 0

def append_to_back(num, digit):
    """Añade un dígito al número por detrás."""
    return num * 10 + digit

def append_to_front(num, digit):
    """Añade un dígito al número por delante."""
    return int(str(digit) + str(num))

def slice_number(num, start, end):
    """Devuelve el trozo del número comprendido entre las posiciones start y end."""
    num = abs(num)
    return int(str(num)[start:end + 1])

def join_numbers(num1, num2):
    """Pega dos números para formar uno solo."""
    return int(str(num1) + str(num2))

# Pruebas de las funciones
def main():
    print(is_palindrome(121))
    print(is_palindrome(123))

    print(is_prime(7))
    print(is_prime(10))

    print(next_prime(7))
    print(next_prime(10))

    print(digit_count(12345))

    print(reverse_number(12345))

    print(digit_at(12345, 2))

    print(digit_position(12345, 3))
    print(digit_position(12345, 6))

    print(remove_from_back(12345, 2))

    print(remove_from_front(12345, 2))

    print(append_to_back(123, 4))

    print(append_to_front(123, 4))

    print(slice_number(12345, 1, 3))

    print(join_numbers(123, 456))

if __name__ == "__main__":
    main()
