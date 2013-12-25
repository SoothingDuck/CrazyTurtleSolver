from Card import *
from Turtle import *
import unittest

class CardTest(unittest.TestCase):
    
    def setUp(self):
        self.c1 = Card("CRCVTVTJ")
        self.c2 = Card("CVCJTRTV")
        self.c3 = Card("CBCBTBTB")
        self.c4 = Card("CBCBTBTB")

    def test_init(self):

        self.assertRaises(CardException, Card, "CR")

        self.assertTrue(self.c1.turtle_north, Turtle("CR"))
        self.assertTrue(self.c1.turtle_east, Turtle("CV"))
        self.assertTrue(self.c1.turtle_south, Turtle("TV"))
        self.assertTrue(self.c1.turtle_west, Turtle("TJ"))

        self.assertTrue(self.c2.turtle_north, Turtle("CV"))
        self.assertTrue(self.c2.turtle_east, Turtle("CJ"))
        self.assertTrue(self.c2.turtle_south, Turtle("TR"))
        self.assertTrue(self.c2.turtle_west, Turtle("TV"))


    def test_rotate_right(self):
        
        self.c2 = self.c1.rotate_right()

        self.assertTrue(self.c2.turtle_east, Turtle("CR"))
        self.assertTrue(self.c2.turtle_south, Turtle("CV"))
        self.assertTrue(self.c2.turtle_west, Turtle("TV"))
        self.assertTrue(self.c2.turtle_north, Turtle("TJ"))

        self.assertTrue(self.c1.turtle_north, Turtle("CR"))
        self.assertTrue(self.c1.turtle_east, Turtle("CV"))
        self.assertTrue(self.c1.turtle_south, Turtle("TV"))
        self.assertTrue(self.c1.turtle_west, Turtle("TJ"))

    def test_rotate_left(self):

        self.c2 = self.c1.rotate_left()

        self.assertTrue(self.c2.turtle_west, Turtle("CR"))
        self.assertTrue(self.c2.turtle_north, Turtle("CV"))
        self.assertTrue(self.c2.turtle_east, Turtle("TV"))
        self.assertTrue(self.c2.turtle_south, Turtle("TJ"))

        self.assertTrue(self.c1.turtle_north, Turtle("CR"))
        self.assertTrue(self.c1.turtle_east, Turtle("CV"))
        self.assertTrue(self.c1.turtle_south, Turtle("TV"))
        self.assertTrue(self.c1.turtle_west, Turtle("TJ"))

    def test_matches(self):

        self.assertTrue(self.c1.matches_west(self.c2))
        self.assertTrue(self.c1.matches_east(self.c2))
        self.assertTrue(self.c1.matches_north(self.c2))
        self.assertTrue(self.c1.matches_south(self.c2))

        self.assertTrue(self.c2.matches_west(self.c1))
        self.assertTrue(self.c2.matches_east(self.c1))
        self.assertTrue(self.c2.matches_north(self.c1))
        self.assertTrue(self.c2.matches_south(self.c1))

        self.assertFalse(self.c1.matches_west(self.c3))
        self.assertFalse(self.c1.matches_east(self.c3))
        self.assertFalse(self.c1.matches_north(self.c3))
        self.assertFalse(self.c1.matches_south(self.c3))

    def test_equality(self):
        self.assertEqual(self.c3, self.c4)

    def test_str(self):
        
        self.assertEqual(
            str(self.c1),
            """
**************
*     CR     *
* TJ      CV *
*     TV     *
**************
"""
            )


        

if __name__ == "__main__":
    unittest.main()
