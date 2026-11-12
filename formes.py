
from abc import ABC, abstractmethod
import math

class Forme(ABC):

    @abstractmethod
    def aire(self):
        pass

    def __str__(self):
        return (
            f"{self.__class__.__name__} - "
            f"aire : {self.aire():.2f}"
        )

class Cercle(Forme):

    def __init__(self, rayon):
        self.rayon = rayon

    def aire(self):
        return math.pi * self.rayon ** 2


class Rectangle(Forme):

    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur

class Triangle(Forme):

    def __init__(self, base, hauteur):
        self.base = base
        self.hauteur = hauteur

    def aire(self):
        return 0.5 * self.base * self.hauteur


if __name__ == "__main__":

    formes = [
        Cercle(3),
        Rectangle(2, 5),
        Triangle(5, 2)
    ]

    for f in formes:
        print(f)
