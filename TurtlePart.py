
class TurtlePartException(Exception):
    pass

class TurtlePart:

    def __init__(self, part_name):
        """Initialisation
        T == Tete
        C == Corps
        """
        if part_name == "T":
            self.part_name = "T"
        elif part_name == "C":
            self.part_name = "C"
        else:
            raise TurtlePartException

    def __str__(self):
        """Affichage de la partie de la tortue"""
        return self.part_name

    def equals(self, other):
        """Test d'egalite avec une autre partie de tortue"""
        return self.part_name == other.part_name

    def copy(self):
        """Retourne une copie de TurtlePart"""
        return TurtlePart(self.part_name)

    def matches(self, other):
        return (self.part_name != other.part_name)
