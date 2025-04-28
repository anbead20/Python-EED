from __future__ import annotations
from typeguard import typechecked
import random


@typechecked
class Card:
    palos = ['Espadas', 'Bastos', 'Oros', 'Copas']
    valores = ['As', '2', '3', '4', '5', '6', '7', 'Sota', 'Caballo', 'Rey']

    def __init__(self, palo: str, valor: str) -> None:
        if palo not in self.palos:
            raise ValueError(f"El palo {palo} no es válido")
        if valor not in self.valores:
            raise ValueError(f"El valor {valor} no es válido")

        self.__palo = palo
        self.__valor = valor

    def __repr__(self) -> str:
        return f"{self.__valor} de {self.__palo}"

    @property
    def palo(self) -> str:
        return self.__palo

    @property
    def valor(self) -> str:
        return self.__valor


@typechecked
class CardPlayer:
    def __init__(self, nombre: str) -> None:
        self.__nombre = nombre
        self.__cartas = []

    def robar(self, baraja: Deck) -> None:
        if len(baraja.cartas) == 0:
            raise ValueError("No hay cartas en la baraja para robar.")
        carta = baraja.robar_primera_carta()
        self.__cartas.append(carta)

    def deshacerse(self, carta: Card) -> None:
        if carta in self.__cartas:
            self.__cartas.remove(carta)
        else:
            raise ValueError("El jugador no tiene esta carta.")

    def recibir_cartas(self, cartas: list[Card]) -> None:
        self.__cartas.extend(cartas)

    def __repr__(self) -> str:
        return f"{self.__nombre} tiene {len(self.__cartas)} cartas."

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def cartas(self) -> list[Card]:
        return self.__cartas


@typechecked
class Deck:
    def __init__(self, cartas: list[Card] = None) -> None:
        if cartas is None:
            cartas = []
        self.__cartas = cartas

    def repartir(self, jugador: CardPlayer, num_cartas: int) -> None:
        if num_cartas > len(self.__cartas):
            raise ValueError("No hay suficientes cartas en la baraja.")
        cartas_repartidas = [self.robar_primera_carta() for _ in range(num_cartas)]
        jugador.recibir_cartas(cartas_repartidas)

    def robar_primera_carta(self) -> Card:
        return self.__cartas.pop(0)

    def barajar(self) -> None:
        random.shuffle(self.__cartas)

    def cantidad_cartas(self) -> int:
        return len(self.__cartas)

    def __repr__(self) -> str:
        return f"Baraja tiene {len(self.__cartas)} cartas."

    @property
    def cartas(self) -> list[Card]:
        return self.__cartas


@typechecked
class SpanishDeck(Deck):
    def __init__(self) -> None:
        # La baraja española tiene 40 cartas (10 valores por 4 palos)
        cartas = [Card(palo, valor) for palo in Card.palos for valor in Card.valores[:10]]
        super().__init__(cartas)


@typechecked
class EnglishDeck(Deck):
    def __init__(self) -> None:
        valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        palos = ['Corazones', 'Diamantes', 'Tréboles', 'Picas']
        cartas = [Card(palo, valor) for palo in palos for valor in valores]
        super().__init__(cartas)


# Ejemplo de uso:
if __name__ == "__main__":
    # Crear una baraja española
    baraja_espanola = SpanishDeck()
    print("Baraja Española:", baraja_espanola)

    # Crear un jugador
    jugador1 = CardPlayer("Juan")

    # Repartir cartas al jugador
    baraja_espanola.repartir(jugador1, 5)
    print(jugador1)

    # Crear una baraja inglesa
    baraja_inglesa = EnglishDeck()
    print("Baraja Inglesa:", baraja_inglesa)

    # Barajar la baraja inglesa
    baraja_inglesa.barajar()
    print("Baraja Inglesa barajada:", baraja_inglesa)

    # El jugador roba una carta de la baraja española
    jugador1.robar(baraja_espanola)
    print(jugador1)

    # El jugador se deshace de una carta
    carta_a_desechar = jugador1.cartas[0]
    jugador1.deshacerse(carta_a_desechar)
    print(jugador1)
