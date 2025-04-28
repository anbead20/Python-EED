from __future__ import annotations
from dice import Dice
from typeguard import typechecked

@typechecked
class LudoDice(Dice):
    def __init__(self):
        super().__init__(1, 2, 3, 4, 5, 6)

    def __lt__(self, other: LudoDice):
        return self.sides < other.sides

    def __le__(self, other: LudoDice):
        return self.sides <= other.sides

    def __gt__(self, other: LudoDice):
        return self.sides > other.sides

    def __ge__(self, other: LudoDice):
        return self.sides >= other.sides

dice1 = LudoDice()
dice2 = LudoDice()

print(f"{dice1} < {dice2}: {dice1 < dice2}")
print(f"{dice1} <= {dice2}: {dice1 <= dice2}")
print(f"{dice1} > {dice2}: {dice1 > dice2}")
print(f"{dice1} >= {dice2}: {dice1 >= dice2}")
print(f"{dice1} == {dice2}: {dice1 == dice2}")
print(f"{dice1} != {dice2}: {dice1 != dice2}")