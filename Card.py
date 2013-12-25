
from Turtle import Turtle
from Color import Color
from TurtlePart import TurtlePart

class CardException(Exception):
    pass

class Card:
    def __init__(self, card_string):
        """Initialisation d'une carte avec des tortues
        Ordre => North, East, South, West
        Exemple : CRCVTVTJ
        North : Corps Rouge
        East  : Corps Vert
        South : Tete Verte
        West  : Tete Jaune
        """

        if len(card_string) != 8:
            raise CardException

        self.card_string = card_string

        self.turtle_north = Turtle(card_string[0:2])
        self.turtle_east = Turtle(card_string[2:4])
        self.turtle_south = Turtle(card_string[4:6])
        self.turtle_west = Turtle(card_string[6:8])

    def matches_west(self, other):
        """Test si la tortue a l'ouest de la carte
        matche avec la tortue a l'est de l'autre carte
        """
        return self.turtle_west.matches(other.turtle_east)

    def matches_east(self, other):
        """Test si la tortue a l'est de la carte
        matche avec la tortue a l'ouest de l'autre carte
        """
        return self.turtle_east.matches(other.turtle_west)

    def matches_north(self, other):
        """Test si la tortue au nord de la carte
        matche avec la tortue au sud de l'autre carte
        """
        return self.turtle_north.matches(other.turtle_south)


    def matches_south(self, other):
        """Test si la tortue au sud de la carte
        matche avec la tortue au nord de l'autre carte
        """
        return self.turtle_south.matches(other.turtle_north)

    def rotate_left(self):
        """Cree une copie d'une rotation d'une carte vers la gauche"""
        return Card(self.card_string[2:8] + self.card_string[0:2])


    def rotate_right(self):
        """Cree une copie d'une rotation d'une carte vers la droite"""
        return Card(self.card_string[6:8] + self.card_string[0:6])


    def __eq__(self, other):
        """Test d'egalite de deux cartes"""
        return (self.turtle_north == other.turtle_north and
                self.turtle_east == other.turtle_east and
                self.turtle_south == other.turtle_south and
                self.turtle_west == other.turtle_west)

    def __str__(self):
        return """
**************
*     %s     *
* %s      %s *
*     %s     *
**************
""" % (str(self.turtle_north), str(self.turtle_west), str(self.turtle_east), str(self.turtle_south))
