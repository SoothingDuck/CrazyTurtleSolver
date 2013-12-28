
from Color import *
from TurtlePart import *

class TurtleException(Exception):
    pass

class Turtle:
    
    ROUGE = Color("R")
    BLEU = Color("B")
    JAUNE = Color("J")
    VERT = Color("V")

    CORPS = TurtlePart("C")
    TETE = TurtlePart("T")

    ASSOC_PART = { "C" : CORPS, "T" : TETE }
    ASSOC_COLOR = {
        "R" : ROUGE,
        "B" : BLEU,
        "J" : JAUNE,
        "V" : VERT
    }

    def __init__(self, init_string):
        """Initialisation

        Exemples : 
        CR == Corps Rouge
        TV == Tete Verte
        """
        if len(init_string) != 2:
            raise TurtleException

        self.init_string = init_string

        turtle_part_string = init_string[0]

        try:
            self.part = Turtle.ASSOC_PART[turtle_part_string]
        except KeyError:
            raise TurtlePartException

        color_string = init_string[1]

        try:
            self.color = Turtle.ASSOC_COLOR[color_string]
        except KeyError:
            raise ColorException
        
    def equals(self, other):
        """Test d'egalite entre tortues"""
        return (self.color.equals(other.color)) and (self.part.equals(other.part))

    def copy(self):
        """Retourne une copie de la tortue"""
        return self


    def __str__(self):
        """Affichage des caracteristiques de la tortue
        Exemples :
        TB
        CJ
        """
        return "%s%s" % (self.part, self.color)

    def matches(self, other):
        """Test si une tortue peut s'emboiter avec une autre"""
        if not self.color.matches(other.color):
            return False
        else:
            return (self.part.matches(other.part))
