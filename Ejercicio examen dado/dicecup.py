from __future__ import annotations
from dice import Dice
from ludodice import LudoDice
from pokerdice import PokerDice
from typeguard import typechecked

@typechecked
class DiceCup:
    def __init__(self, *dices: Dice):
        self.__dices = list(dices)

    @property
    def dices(self):
        return self.__dices.copy()

    @property
    def size(self):
        return len(self.__dices)

    def add(self, dice: Dice):
        self.__dices.append(dice)

    def remove(self, dice: Dice):
        if dice not in self.__dices:
            raise ValueError(f"El dado {dice} no está en el cubilete")
        self.__dices.remove(dice)

    def __str__(self):
        return f"Cubilete: {self.__dices}"


cup = DiceCup(LudoDice(), PokerDice(), Dice('X','Y','Z'))
print(f"Creado cubilete de dados: {cup} con {cup.size} dados")

d = Dice(100,200,300)
cup.add(d)
print(f"Cubilete después de haber añadido el dado {d}: {cup}. Tamaño {cup.size}")

cup.remove(d)
print(f"Cubilete después de haber borrado el dado {d}: {cup}. Tamaño {cup.size}")

input(f"Y si volvemos a borrar {d} del cubilete saltará una excepción. Pulsa Intro para seguir...")
cup.remove(d)