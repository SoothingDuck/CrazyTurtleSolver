
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

        self.init_string = init_string

        turtle_part_string = init_string[0]

        self.part = TurtlePart.TurtlePart(turtle_part_string)

        color_string = init_string[1]

        self.color = Color.Color(color_string)
        
    def equals(self, other):
        """Test d'egalite entre tortues"""
        return (self.color.equals(other.color)) and (self.part.equals(other.part))

    def copy(self):
        """Retourne une copie de la tortue"""
        return Turtle(self.init_string)


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
