
class ColorException(Exception):
    pass

class Color:
    def __init__(self, letter):
        """Initialisation
        R == Rouge
        V == Vert
        J == Jaune
        B == Bleu
        """
        if letter == "R":
            self.color = "Rouge"
        elif letter == "V":
            self.color = "Vert"
        elif letter == "J":
            self.color = "Jaune"
        elif letter == "B":
            self.color = "Bleu"
        else:
            raise ColorException

    def __str__(self):
        """Affichage de la color"""
        return self.color

    def __eq__(self, other):
        """Surcharge de =="""
        return self.color == other.color

    def __ne__(self, other):
        """Surcharge de !="""
        return self.color != other.color
        
