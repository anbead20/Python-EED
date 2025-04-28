from __future__ import annotations
from typeguard import typechecked
from ej11_V2 import Terminal

@typechecked
class Mobile(Terminal):
    __tariffs = {
        "rata": 0.06,
        "mono": 0.12,
        "bisonte": 0.30
    }

    def __init__(self, phone_number: str, tariff: str):
        if tariff not in Mobile.__tariffs:
            raise ValueError("Tarifa no válida. Usa 'rata', 'mono' o 'bisonte'")
        super().__init__(phone_number)
        self.__tariff = tariff
        self.__total_cost = 0.0

    @property
    def tariff(self):
        return self.__tariff

    @property
    def total_cost(self):
        return self.__total_cost

    def call(self, other: Terminal, time: int):
        result = super().call(other, time)
        cost = (time / 60) * Mobile.__tariffs[self.__tariff]
        self.__total_cost += cost
        return result

    def change_tariff(self, new_tariff: str):
        if new_tariff not in Mobile.__tariffs:
            raise ValueError("Tarifa no válida. Usa 'rata', 'mono' o 'bisonte'")
        self.__tariff = new_tariff

    def __str__(self):
        num = self.phone_number
        formatted = f"{num[:3]} {num[3:5]} {num[5:7]} {num[7:]}"
        return (f"Nº {formatted} - {self.call_time} s de conversación - "
                f"tarificados {self.__total_cost:.2f} euros")

if __name__ == "__main__":
    m1 = Mobile("678112233", "rata")
    m2 = Mobile("644744469", "mono")
    m3 = Mobile("622328909", "bisonte")

    print(m1)
    print(m2)

    m1.call(m2, 320)
    m1.call(m3, 200)
    m2.call(m3, 550)

    print(m1)
    print(m2)
    print(m3)