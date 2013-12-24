
class TurtlePartException(Exception):
    pass

class TurtlePart:

    def __init__(self, part_name):
        if part_name == "T":
            self.part_name = "Tete"
        elif part_name == "C":
            self.part_name = "Corps"
        else:
            raise TurtlePartException

    def __str__(self):
        return self.part_name



