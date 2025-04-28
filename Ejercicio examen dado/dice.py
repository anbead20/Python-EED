"""
(2 PUNTOS): Crea una clase que modele un dado (Dice) de manera que:
El constructor recibe los valores de las caras que tiene el dado. Ejemplo:

dice1 = Dice(1, 2, 3, 4, 5, 6)
dice2 = Dice('A', 'K', 'Q', 'J', 'R', 'N')
Los valores de las caras los obtendremos mediante una propiedad (sides).

Dispondremos de un método para tirar el dado (roll) que devolverá el resultado (uno de los valores anteriores),
además actualizará una variable de instancia privada (side) que podrá consultarse mediante una propiedad.

Los métodos mágicos __str__() y __repr__() deben estar creados.

Puedo usar los operadores == y != para comparar dos dados.

(1 PUNTO) Crea una clase que modele un dado de póker (PokerDice) que derive de la clase anterior de manera que:
Los posibles valores del dado son 'A', 'K', 'Q', 'J', 'R' y 'N'.
El dado tiene una propiedad (score) que nos da la puntuación del dado (6, 5, 4, 3, 2, 1).
(1 PUNTO) Crea una clase que modele un dado de parchís (LudoDice) que derive de la clase del apartado 1. Un dado de
parchís tiene seis caras que van del 1 al 6 (valores enteros). En esta clase:
Tendremos la posibilidad de comparar dados entre sí con los operadores relaciones <, <=, > y >=.
(3 PUNTOS) Crea una clase que modele un dado de parchís trucado (TrickedLudoDice) que derive de la clase anterior y
que de cuando en cuando nos permita poner el valor que queramos en la cara del dado (entre 1 y 6), de manera que:
No puedo usar el método que pone el valor que queramos en la cara del dado (put) si no he tirado al menos tres veces
de forma normal, si lo llamo sin haberse cumplido esta excepción lanzaremos una excepción.
Ten en cuenta que NO PUEDES cambiar directamente el valor de la cara de un dado ya que se almacena en una variable
de instancia privada de una clase de la que heredas (Dice) y no tienes acceso.
(2 PUNTOS) Crea una clase que modele un cubilete de dados (DiceCup) de manera que:
Al construirla le paso una serie de dados. Ejemplo:

cup = DiceCup(LudoDace(), LudoDace(), LudoDace())
Dispondremos de una propiedad que devuelva los dados (dices) y otra que devuelva el número de dados que contiene (size).

Dispondremos de un método para añadir un dado (add).

Dispondremos de un método para quitar un dado (remove) pasándole el dado concreto que queremos quitar.

Debe estar creado el método mágico* __str__()*.

(1 PUNTO) Crea una clase que modele un cubilete de dados de póker (PokerDiceCup) que derive de la clase anterior de
manera que tenga una propiedad (score) que devuelva la puntuación total del cubilete (la suma de la de cada dado).
Hay que controlar los tipos de datos de los parámetros de los métodos. Usa los test proporcionados.

Autor: Adrián Anta Bellido
"""

from __future__ import annotations
from typeguard import typechecked
import random

@typechecked
class Dice:
    def __init__(self, *sides):
        self.__sides = sides
        self.__side = self.roll()

    @property
    def sides(self):
        return self.__sides

    @property
    def side(self):
        return self.__side

    def roll(self):
        self.__side = random.choice(self.__sides)
        return self.__side

    def __str__(self):
        return f"Valor actual: {self.__side}"

    def __repr__(self):
        return f"Dice({self.__sides})"

    def __eq__(self, other: Dice):
        return self.__sides == other.__sides

    def __ne__(self, other: Dice):
        return not self.__sides == other.__sides

dice1 = Dice(1,2,3,4,5,6)
dice2 = Dice('A','K','Q','J','R','N')

print(f"Tiro cinco veces los dados {repr(dice1)} y {repr(dice2)}:")
for i in range(5):
    dice1.roll()
    dice2.roll()
    print(f"Tirada {i+1}: {dice1} {dice2}")
