
from CardSet import CardSet

class Place:

    def __init__(self, grid, x, y):
        self.grid = grid
        self.x = x
        self.y = y
        self.card = None


    def copy(self, other_grid):
        p = Place(other_grid, self.x, self.y)
        if not self.card is None:
            p.card = self.card.copy()

        return p


    def equals(self, other):
        if self.x != other.x:
            return False

        if self.y != other.y:
            return False

        if self.card is None:
            return (other.card is None)
        else:
            return (self.card.has_same_configuration_as(other.card))

    def set_card(self, card):
        self.card = card

    def has_card(self):
        return self.card != None

    def get_card(self):
        return self.card

    def has_adjacent_card(self):

        if self.x > 0 and self.grid.matrix[self.x - 1][self.y].has_card():
            return True

        if self.x < 2 and self.grid.matrix[self.x + 1][self.y].has_card():
            return True

        if self.y > 0 and self.grid.matrix[self.x][self.y - 1].has_card():
            return True

        if self.y < 2 and self.grid.matrix[self.x][self.y + 1].has_card():
            return True

        return False


    def __str__(self):
        return "Place(x = %d, y = %d)" % (self.x, self.y)


    def is_possible_card(self, card):

        if self.x > 0 and self.grid.matrix[self.x - 1][self.y].has_card():
            if not card.matches_west(self.grid.matrix[self.x - 1][self.y].card):
                return False

        if self.x < 2 and self.grid.matrix[self.x + 1][self.y].has_card():
            if not card.matches_east(self.grid.matrix[self.x + 1][self.y].card):
                return False

        if self.y > 0 and self.grid.matrix[self.x][self.y - 1].has_card():
            if not card.matches_north(self.grid.matrix[self.x][self.y - 1].card):
                return False

        if self.y < 2 and self.grid.matrix[self.x][self.y + 1].has_card():
            if not card.matches_south(self.grid.matrix[self.x][self.y + 1].card):
                return False

        return True


    def get_possible_card_configuration(self):
        
        result = []

        for card in self.grid.cardset:
            tmp = card.copy()
            for _ in range(4):
                tmp = tmp.rotate_right()
                
                if self.is_possible_card(tmp):
                    result.append(tmp.copy())

        return result
                

class GridCardNotFound(Exception):
    pass

class GridCardAlreadyInCardSet(Exception):
    pass

class Grid:
    
    def __init__(self):
        self.cardset = CardSet()

        self.matrix = []

    def equals(self, other):
        """Teste l'egalite entre 2 grilles"""
        if not self.cardset.equals(other.cardset):
            return False

        for i in range(3):
            for j in range(3):
                if not self.matrix[i][j].equals(other.matrix[i][j]):
                    return False

        return True

    def add_card_to_cardset(self, card):
        """Ajoute une carte au cardset"""
        if not card in self.cardset:
            self.cardset.append(card)
        else:
            raise GridCardAlreadyInCardSet

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



        
