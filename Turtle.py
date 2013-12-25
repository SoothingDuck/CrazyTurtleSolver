
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
        TB
        CJ
        """
        return "%s%s" % (self.part, self.color)

    def matches(self, other):
        """Test si une tortue peut s'emboiter avec une autre"""
        if self.color != other.color:
            return False
        else:
            return (self.part != other.part)
