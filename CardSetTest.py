from Card import Card
from CardSet import *
import unittest

class CardSetTest(unittest.TestCase):

    def setUp(self):
        self.a = CardSet()
        self.a.init_crazy_turle_cardset_internet()

    def test_copy(self):

        a = CardSet()
        a.init_crazy_turle_cardset_internet()

        b = a.copy()

        self.assertFalse(a == b)

        self.assertEqual(len(a), len(b))
        
        for card in b:
            self.assertTrue(card in a)

        a.delete_card(Card("TVCRTJTB"))

        self.assertFalse(a.equals(b))

        b.delete_card(Card("TVCRTJTB"))

        self.assertTrue(a.equals(b))


    def test_init(self):

        self.assertTrue(Card("TVCRTJTB") in self.a)
        self.assertTrue(Card("CBCVTBTR") in self.a)
        self.assertTrue(Card("TRCJCRTV") in self.a)
        self.assertTrue(Card("CJCVTBCV") in self.a)
        self.assertTrue(Card("CBCJTRTV") in self.a)
        self.assertTrue(Card("TRTRCVTJ") in self.a)
        self.assertTrue(Card("CBTJCRTJ") in self.a)
        self.assertTrue(Card("CRTBTJCJ") in self.a)
        self.assertTrue(Card("TVCBCVCB") in self.a)

    def test_taille(self):
        
        self.assertEqual(len(self.a), 9)

        card = self.a.pop()

        self.assertEqual(len(self.a), 8)

        self.assertTrue(not card in self.a)

    def test_del(self):

        card = Card("TVCRTJTB")

        self.assertTrue(card in self.a)

        self.a.delete_card(card)

        self.assertEqual(len(self.a), 8)

        self.assertTrue(not card in self.a)

if __name__ == "__main__":
    unittest.main()

        
