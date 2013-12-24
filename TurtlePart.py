
class TurtlePartException(Exception):
    pass

class TurtlePart:

    def __init__(self, part_name):
        """Initialisation
        T == Tete
        C == Corps
        """
        if part_name == "T":
            self.part_name = "Tete"
        elif part_name == "C":
            self.part_name = "Corps"
        else:
            raise TurtlePartException

    def __str__(self):
        """Affichage de la partie de la tortue"""
        return self.part_name

    def __eq__(self, other):
        """Test d'egalite avec une autre partie de tortue"""
        return self.part_name == other.part_name

    def __ne__(self, other):
        """Test d'inegalite avec une autre partie de tortue"""
        return self.part_name != other.part_name
