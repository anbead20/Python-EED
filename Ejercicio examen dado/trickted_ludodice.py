from __future__ import annotations
from ludodice import LudoDice
from typeguard import typechecked

@typechecked
class TrickedLudoDice(LudoDice):
    __MIN_DICE_ROLLS = 3

    def __init__(self):
        self.__normal_dice_rolls = 0
        super().__init__()

    def roll(self):
        self.__normal_dice_rolls += 1
        return super().roll()

    def put(self, n: int):
        self.__check_put(n)
        self.__roll_until_n(n)
        self.__normal_dice_rolls = 0

    def __check_put(self, n):
        if n not in self.sides:
            raise ValueError(f"Valor incorrecto de cara del dado: {n}")
        if self.__normal_dice_rolls < self.__MIN_DICE_ROLLS:
            raise ValueError(f"No ha tirado aún {self.__MIN_DICE_ROLLS} veces.")

    def __roll_until_n(self, n):
        while True:
            super().roll()
            if self.side == n:
                break

d = TrickedLudoDice()
print("Tiramos el dado trucado tres veces de manera normal:")
for i in range(3):
    d.roll()
    print(f"Tirada {i+1}: {d}")

d.put(5)
print(f"Le hemos asignado al dado un 5: {d}")

d.roll()
print(f"Tiramos el dado de nuevo: {d}")

input("Y si intentamos asignarle un valor de nuevo saltará una excepción por no haber tirado tres veces. Pulsa Intro")
d.put(5)