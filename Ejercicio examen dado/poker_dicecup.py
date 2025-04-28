from __future__ import annotations
from dicecup import DiceCup
from pokerdice import PokerDice
from ludodice import LudoDice
from typeguard import typechecked

@typechecked
class PokerDiceCup(DiceCup):
    def __init__(self, *dices: PokerDice):
        super().__init__(*dices)

    @property
    def score(self):
        score_ = 0
        for d in self.dices:
            score_ += d.score
        return score_

    def add(self, dice: PokerDice):
        if not isinstance(dice, PokerDice):
            raise TypeError(f"No se puede añadir un dado que no sea PokerDice: {dice}")
        super().add(dice)

    def __lt__(self, other: PokerDice):
        return self.score < other.score

    def __le__(self, other: PokerDice):
        return self.score <= other.score

    def __gt__(self, other: PokerDice):
        return self.score > other.score

    def __ge__(self, other: PokerDice):
        return self.score >= other.score

    def __eq__(self, other: PokerDice):
        return self.score == other.score

    def __ne__(self, other: PokerDice):
        return self.score != other.score

cup = PokerDiceCup(PokerDice(), PokerDice(), PokerDice())
print(f"La puntuación de {cup} es {cup.score}")

other = PokerDice()
print(f"Hemos creado el dado {other} y se lo añadimos al cubilete")

cup.add(other)
print(f"La puntuación de {cup} ahora es {cup.score}")

other = LudoDice()
input(f"Hemos creado el dado de parchís {other} y si lo añado al cubilete saltará una excepción...")
cup.add(other)