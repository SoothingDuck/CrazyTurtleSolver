from Card import Card
from CardSet import *
import unittest

class CardSetTest(unittest.TestCase):

    def setUp(self):
        self.a = CardSet()
        self.a.init_crazy_turle_cardset()

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

if __name__ == "__main__":
    unittest.main()

        
