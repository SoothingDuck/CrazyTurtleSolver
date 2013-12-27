
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
        self.letter = letter

        if letter == "R":
            self.color = "R"
        elif letter == "V":
            self.color = "V"
        elif letter == "J":
            self.color = "J"
        elif letter == "B":
            self.color = "B"
        else:
            raise ColorException

    def __str__(self):
        """Affichage de la color"""
        return self.color

    def equals(self, other):
        """Surcharge de =="""
        return self.color == other.color


    def copy(self):
        """Retourne une copie de la couleur"""
        return Color(self.letter)
