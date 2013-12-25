from Card import Card
from CardSet import *
import unittest

class CardSetTest(unittest.TestCase):

    def test_init(self):
        
        a = CardSet()
        a.init_crazy_turle_cardset()

        self.assertTrue(Card("TVCRTJTB") in a)
        self.assertTrue(Card("CBCVTBTR") in a)
        self.assertTrue(Card("TRCJCRTV") in a)
        self.assertTrue(Card("CJCVTBCV") in a)
        self.assertTrue(Card("CBCJTRTV") in a)
        self.assertTrue(Card("TRTRCVTJ") in a)
        self.assertTrue(Card("CBTJCRTJ") in a)
        self.assertTrue(Card("CRTBTJCJ") in a)
        self.assertTrue(Card("TVCBCVCB") in a)

if __name__ == "__main__":
    unittest.main()

        
