
from CardSet import CardSet
from Place import Place

class Grid:
    
    def __init__(self):
        self.cardset = CardSet()

        self.matrix = []

    def init_crazy_turtle_game(self):
        
        self.cardset.init_crazy_turle_cardset()

        for i in range(3):
            self.matrix.append([None, None, None])

        for i in range(3):
            for j in range(3):
                self.matrix[i][j] = Place(self, i, j)


    def number_of_cards_left(self):
        return len(self.cardset)


    def set_card(self, num_card, x, y):
        place = self.matrix[x][y]

        card = self.cardset[num_card]
        
        self.cardset.delete_card(card)

        place.set_card(card)

    def get_new_places_for_cards(self):

        tmp = []

        for i in range(3):
            for j in range(3):
                place = self.matrix[i][j]
                if not place.has_card():
                    if place.has_adjacent_card():
                        tmp.append(place)

        return tmp



        
