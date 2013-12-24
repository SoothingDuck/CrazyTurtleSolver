
import Color
import TurtlePart

class TurtleException(Exception):
    pass

class Turtle:
    
    def __init__(self, init_string):
        """Initialisation

        Exemples : 
        CR == Corps Rouge
        TV == Tete Verte
        """
        if len(init_string) != 2:
            raise TurtleException

        turtle_part_string = init_string[0]

        self.part = TurtlePart.TurtlePart(turtle_part_string)

        color_string = init_string[1]

        self.color = Color.Color(color_string)
        
    def __eq__(self, other):
        """Test d'egalite entre tortues"""
        return (self.color == other.color) and (self.part == other.part)

    def __str__(self):
        """Affichage des caracteristiques de la tortue
        Exemples :
        Tete Bleue
        Corps Jaune
        """
        if self.part == TurtlePart.TurtlePart("C"):
            return "%s %s" % (self.part, self.color)
        else:
            if self.color == Color.Color("B"):
                return "%s Bleue" % (self.part)
            elif self.color == Color.Color("V"):
                return "%s Verte" % (self.part)
            else:
                return "%s %s" % (self.part, self.color)
