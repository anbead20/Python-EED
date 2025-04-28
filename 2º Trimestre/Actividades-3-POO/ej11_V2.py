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
import os

@typechecked
class Terminal:
    __phone_file = "phones.txt"

    def __init__(self, phone_number: str):
        self.__validate_number(phone_number)
        self.__phone_number = phone_number
        self.__call_time = 0
        self.__register_number(phone_number)

    @classmethod
    def __existing_numbers(cls):
        if not os.path.exists(cls.__phone_file):
            return set()
        with open(cls.__phone_file, "r") as file:
            return set(line.strip() for line in file)

    @classmethod
    def __register_number(cls, number: str):
        with open(cls.__phone_file, "a") as file:
            file.write(f"{number}\n")

    def __validate_number(self, number: str):
        if not number.isdigit():
            raise ValueError("Solo puede haber dígitos")
        if len(number) != 9:
            raise ValueError("Debe haber 9 dígitos")
        if number[0] not in {"6", "7", "9"}:
            raise ValueError("El número debe empezar por 6, 7 o 9")
        if number in self.__existing_numbers():
            raise ValueError(f"El número {number} ya esta registrado")

    @property
    def phone_number(self):
        return self.__phone_number

    @property
    def call_time(self):
        return self.__call_time

    def call(self, other: Terminal, time: int):
        if self.__phone_number == other.phone_number:
            raise ValueError("No puedes llamar al mismo número")
        if time < 0:
            raise ValueError("La duración de la llamada debe ser positiva")

        self.__call_time += time
        other.__call_time += time
        return f"{self.phone_number} ha llamado a {other.phone_number} durante {time} segundos"

    def __str__(self):
        return f"Teléfono {self.__phone_number} - {self.__call_time}s de conversación"

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
