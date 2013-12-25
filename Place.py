
class Place:

    def __init__(self, grid, x, y):
        self.grid = grid
        self.x = x
        self.y = y
        self.card = None

    def set_card(self, card):
        self.card = card

    def has_card(self):
        return self.card != None


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

        if self.x > 0 and self.grid[self.x - 1][y].has_card():
            if not card.matches_west(self.grid[self.x - 1][y].card):
                return False

        raise


    def get_possible_card_configuration(self):
        
        result = []

        for card in self.grid.cardset:
            for _ in range(4):
                tmp = card.rotate_right()
                
                if self.is_possible_card(tmp):
                    result.append(tmp.copy())


        return result
                
