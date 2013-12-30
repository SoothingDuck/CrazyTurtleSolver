
import unittest
from CardSet import *
from Grid import *

class GridTest(unittest.TestCase):
    
    def setUp(self):
        self.grid = Grid()
        self.grid.init_crazy_turtle_game()

    def test_exception_grid_card(self):
        self.assertRaises(GridCardNotFound, self.grid.set_card, Card("TJTBTVCJ"), 1, 1)

    
    def test_change_cardset(self):

        c = CardSet()
        c.init_crazy_turtle_cardset_home()

        self.grid.set_cardset(c)

        self.assertTrue(Card("TRTBCVCJ") in self.grid.get_cardset())
        self.assertTrue(Card("CBTVTJCR") in self.grid.get_cardset())

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

        a = self.grid.matrix[0][1].get_possible_card_configurations()
        self.assertTrue(a[0].equals(Card("TRCJCRTV")))


    def test_exist_valid_card_for_all_places(self):
        
        self.grid.set_card(Card("TRTVCBCJ"), 0, 0)
        self.grid.set_card(Card("TBTRCBCV"), 0, 1)
        self.grid.set_card(Card("TBCVCJCV"), 0, 2)
        self.grid.set_card(Card("TJTBTVCR"), 1, 1)

        self.assertFalse(self.grid.exist_valid_card_for_all_next_places())

    def test_init(self):

        self.assertTrue(isinstance(self.grid, Grid))

        self.assertEqual(self.grid.number_of_cards_left(), 9)

        self.grid.set_card(Card("TJTBTVCR"),1,1)

        self.assertEqual(self.grid.number_of_cards_left(), 8)

        new_places = self.grid.get_new_places_for_cards()

        self.assertEqual(len(new_places), 4)

        place = new_places[0]

        self.assertTrue(isinstance(place, Place))

        card_configuration_list = place.get_possible_card_configurations()

        self.assertEqual(len(card_configuration_list), 5)

        self.assertTrue(isinstance(card_configuration_list[0], Card))

        next_grid = place.get_grid_for_card_configuration(card_configuration_list[0])
        
        self.assertEqual(next_grid.number_of_cards_left(), 7)

        self.assertNotEqual(self.grid, next_grid)

        self.assertTrue(next_grid.get_card(1,1).equals(Card("TJTBTVCR")))
        self.assertTrue(next_grid.get_card(0,1).equals(Card("TBTRCBCV")))

        next_new_places = next_grid.get_new_places_for_cards()

        self.assertEqual(len(next_new_places), 5)

        place = next_grid.get_place(x=1,y=0)

        card_list = place.get_possible_card_configurations()

        card = card_list[0]

        next_next_grid = place.get_grid_for_card_configuration(card)

        place = next_next_grid.get_place(0,0)

        card_list = place.get_possible_card_configurations()


    def test_next_step(self):
        
        cardset = self.grid.get_cardset()
        first_card = cardset[0]

        self.grid.set_card(first_card, 1, 1)

        grid_set = self.grid.next_step()

        for grid in grid_set:
            self.assertEquals(grid.number_of_cards_left(), 7)

        result = []
        for grid in grid_set:
            result += grid.next_step()

if __name__ == "__main__":
    unittest.main()
