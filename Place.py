
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
                
