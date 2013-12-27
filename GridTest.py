
import unittest
from CardSet import *
from Grid import *

class GridTest(unittest.TestCase):
    
    def setUp(self):
        self.grid = Grid()
        self.grid.init_crazy_turtle_game()

    def test_exception_grid_card(self):
        self.assertRaises(GridCardNotFound, self.grid.set_card, Card("TJTBTVCJ"), 1, 1)

    
    def test_equals(self):

        self.grid.set_card(Card("TBTVCRTJ"), 1, 1)
        self.grid.set_card(Card("CBTJCRTJ"), 0, 0)

        other_grid = self.grid.copy()

        self.assertNotEqual(self.grid, other_grid)
        self.assertTrue(self.grid.equals(other_grid))

        self.grid.add_card_to_cardset(Card("TVCRTJTB"))
        self.assertRaises(GridCardAlreadyInCardSet, self.grid.add_card_to_cardset, Card("TVCRTJTB"))

        self.grid.set_card(Card("TVCRTJTB"), 1, 1)

        self.assertFalse(self.grid.equals(other_grid))

        self.grid.add_card_to_cardset(Card("TBTVCRTJ"))
        self.grid.set_card(Card("TBTVCRTJ"), 1, 1)

        self.assertTrue(self.grid.equals(other_grid))


    def test_copy(self):

        self.grid.set_card(Card("TBTVCRTJ"), 1, 1)
        self.grid.set_card(Card("CBTJCRTJ"), 0, 0)

        other_grid = self.grid.copy()

        self.assertNotEqual(self.grid, other_grid)

        self.assertNotEqual(self.grid.cardset, other_grid.cardset)
        self.assertTrue(self.grid.cardset.equals(other_grid.cardset))

        self.assertNotEqual(self.grid.get_card(1,1), other_grid.get_card(1,1))
        self.assertTrue(self.grid.get_card(1,1).has_same_configuration_as(other_grid.get_card(1,1)))

        self.assertNotEqual(self.grid.get_card(0,0), other_grid.get_card(0,0))
        self.assertTrue(self.grid.get_card(0,0).has_same_configuration_as(other_grid.get_card(0,0)))

        for i in range(3):
            for j in range(3):
                self.assertNotEqual(self.grid.matrix[i][j], other_grid.matrix[i][j])
                self.assertTrue(self.grid.matrix[i][j].equals(other_grid.matrix[i][j]))


    def test_configuration(self):
        
        self.grid.set_card(Card("TBTVCRTJ"), 1, 1)
        self.grid.set_card(Card("CBTJCRTJ"), 0, 0)

        self.assertEqual(self.grid.number_of_cards_left(), 7)

        a = self.grid.matrix[0][1].get_possible_card_configuration()
        self.assertTrue(a[0].equals(Card("TRCJCRTV")))

    def test_init(self):

        self.assertTrue(isinstance(self.grid, Grid))

        self.assertEqual(self.grid.number_of_cards_left(), 9)

        self.grid.set_card(Card("TJTBTVCR"),1,1)

        self.assertEqual(self.grid.number_of_cards_left(), 8)

        new_places = self.grid.get_new_places_for_cards()

        self.assertEqual(len(new_places), 4)

        place = new_places[0]

        self.assertTrue(isinstance(place, Place))

        card_configuration_list = place.get_possible_card_configuration()

        self.assertEqual(len(card_configuration_list), 5)

        self.assertTrue(isinstance(card_configuration_list[0], Card))

        next_grid = place.get_grid_for_card_configuration(card_configuration_list[0])
        
        self.assertEqual(self.next_grid.number_of_cards_left(), 7)



if __name__ == "__main__":
    unittest.main()
