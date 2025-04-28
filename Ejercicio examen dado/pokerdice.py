from __future__ import annotations
from dice import Dice
from typeguard import typechecked

@typechecked
class PokerDice(Dice):
    def __init__(self):
        super().__init__('A', 'K', 'Q', 'J', 'R', 'N')

    @property
    def score(self):
        scores = {'A': 6, 'K': 5, 'Q': 4, 'J': 3, 'R': 2, 'N': 1}
        return scores.get(self.side, 0)

dice = PokerDice()
print(f"Tiro cinco veces el dado {repr(dice)}:")
for i in range(5):
    dice.roll()
    print(f"Tirada {i+1}: {dice} con puntuación {dice.score}")