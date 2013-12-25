
import unittest
from CardSet import *
from Grid import *

class GridTest(unittest.TestCase):
    
    def setUp(self):
        self.grid = Grid()
        self.grid.init_crazy_turtle_game()

    def test_init(self):

        self.assertTrue(isinstance(self.grid, Grid))

        self.assertEqual(self.grid.number_of_cards_left(), 9)

        self.grid.set_card(0,1,1)

        self.assertEqual(self.grid.number_of_cards_left(), 8)

        new_places = self.grid.get_new_places_for_cards()

        self.assertEqual(len(new_places), 4)

        place = new_places[0]

        print place

        self.assertTrue(isinstance(place, Place))

        card_configuration_list = place.get_possible_card_configuration()

        self.assertEqual(len(card_configuration_list), 5)

        self.assertTrue(isinstance(card_configuration_list[0], Card))

        next_grid = place.get_grid_for_card_configuration(card_configuration_list[0])
        
        self.assertEqual(self.next_grid.number_of_cards_left(), 7)



if __name__ == "__main__":
    unittest.main()
