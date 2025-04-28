"""
Implementar otra clase Dado. Por defecto el dado tendrá 6 caras. Tendremos tres formar de construir un dado (uno al
que no se le pasa nada e inicializa el dado al azar, otro al que sólo se le pasa que número tiene el dado en la cara
superior y otro con el número del dado en la cara superior y el número de caras del dado). Implementa los getters, el
método roll() que tirará el dado al azar y el __str__(). Implementa un tester que tenga un vector de 4 dados y los
lance una serie de veces.

Autor: Adrián Anta Bellido
"""

import random
from typeguard import typechecked

@typechecked
class Dice:
    def __init__(self, top_face=None, num_faces=6):
        if num_faces < 2:
            raise ValueError("El dado debe tener al menos 2 caras")

        self.__num_faces = num_faces

        if top_face is None:
            self._top_face = random.randint(1, self.__num_faces)
        elif 1 <= top_face <= self.__num_faces:
            self._top_face = top_face
        else:
            raise ValueError(f"El número de la cara superior debe estar entre 1 y {self.__num_faces}")

    @property
    def top_face(self):
        """Devuelve el número de la cara superior."""
        return self._top_face

    @property
    def num_faces(self):
        """Devuelve el número total de caras del dado."""
        return self.__num_faces

    def roll(self):
        """Lanza el dado al azar y actualiza la cara superior."""
        self._top_face = random.randint(1, self.__num_faces)

    def __str__(self):
        """Representación en cadena del dado."""
        return f"Dado de {self.__num_faces} caras, cara superior: {self._top_face}"