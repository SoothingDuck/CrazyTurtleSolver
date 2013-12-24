
class ColorException(Exception):
    pass

class Color:
    def __init__(self, letter):
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
        return self.color

