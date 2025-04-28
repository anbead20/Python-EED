"""
Implementa la clase Terminal. Un terminal tiene asociado un número de teléfono. Los terminales se pueden llamar unos
a otros y el tiempo de conversación corre para ambos. A continuación se proporciona el contenido del programa
principal que usa esta clase y el resultado que debe aparecer por pantalla. Los números de teléfono tienen que
validarse como tales al crear el objeto (solo dígitos, empiezan por 9, 6 o 7, su longitud es de nueve dígitos) y no
puede haber dos terminales con el mismo número.

Autor: Adrián Anta Bellido
"""
from __future__ import annotations
from typeguard import typechecked

@typechecked
class Terminal:
    __used_numbers = []  # Almacena números ya registrados

    def __init__(self, phone_number: str):
        if not phone_number.isdigit():
            raise ValueError("El número de teléfono solo debe contener dígitos")
        if len(phone_number) != 9:
            raise ValueError("La longitud del número de teléfono debe ser de 9 dígitos")
        if phone_number[0] not in {"6", "7", "9"}:
            raise ValueError("Los números de teléfono deben empezar por 9, 7 o 6")
        if phone_number in Terminal.__used_numbers:
            raise ValueError(f"El número {phone_number} ya está registrado")

        self.__phone_number = phone_number
        self.__call_time = 0
        Terminal.__used_numbers.append(phone_number)

    @property
    def phone_number(self):
        return self.__phone_number

    @property
    def call_time(self):
        return self.__call_time

    def call(self, other: Terminal, time: int):
        if self.__phone_number == other.phone_number:
            raise ValueError("No se puede llamar al mismo número")
        if time < 0:
            raise ValueError("El tiempo de llamada debe ser positivo")

        self.__call_time += time
        other.__call_time += time
        return f"El número {self.phone_number} ha llamado al {other.phone_number}, y ha durado {time} segundos"

    def __str__(self):
        return f"Nº {self.__phone_number} - {self.__call_time} s de conversación"


if __name__ == "__main__":
    t1 = Terminal("678112233")
    t2 = Terminal("644744469")
    t3 = Terminal("622328909")
    t4 = Terminal("664739818")
    print(t1)
    print(t2)
    print(t1.call(t2, 320))
    print(t1.call(t3, 200))
    print(t1)
    print(t2)
    print(t3)
    print(t4)
