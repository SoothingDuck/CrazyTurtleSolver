
from CardSet import CardSet
from Place import Place

class GridCardNotFound(Exception):
    pass

class Grid:
    
    def __init__(self):
        self.cardset = CardSet()

        self.matrix = []


    def copy(self):
        """Copie de la grille actuelle"""
        g = Grid()
        g.cardset = self.cardset.copy()
        
        for i in range(3):
            g.matrix.append([None, None, None])

        for i in range(3):
            for j in range(3):
                g.matrix[i][j] = self.matrix[i][j].copy(g)

        return g

    def init_crazy_turtle_game(self):
        
        self.cardset.init_crazy_turle_cardset()

        for i in range(3):
            self.matrix.append([None, None, None])

        for i in range(3):
            for j in range(3):
                self.matrix[i][j] = Place(self, i, j)


    def number_of_cards_left(self):
        return len(self.cardset)


    def set_card(self, card, x, y):
        place = self.matrix[x][y]

        if card not in self.cardset:
            raise GridCardNotFound
        
        self.cardset.delete_card(card)

        place.set_card(card)


    def get_card(self, x, y):
        return self.matrix[x][y].get_card()

    def get_new_places_for_cards(self):

        tmp = []

        for i in range(3):
            for j in range(3):
                place = self.matrix[i][j]
                if not place.has_card():
                    if place.has_adjacent_card():
                        tmp.append(place)

        return tmp



        
