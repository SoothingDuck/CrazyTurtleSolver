from Color import *
import unittest

class ColorTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_red(self):
        c = Color("R")
        self.assertEqual(str(c), "Rouge")

    def test_blue(self):
        c = Color("B")
        self.assertEqual(str(c), "Bleu")

    def test_yellow(self):
        c = Color("J")
        self.assertEqual(str(c), "Jaune")

    def test_green(self):
        c = Color("V")
        self.assertEqual(str(c), "Vert")

    def test_wrong(self):
         self.assertRaises(ColorException, Color, "Y")

    def test_equality(self):
        b1 = Color("B")
        b2 = Color("B")
        
        self.assertEqual(b1, b2)
        
    def test_inequality(self):
        b = Color("B")
        v = Color("V")

        self.assertTrue(b != v)

if __name__ == "__main__":
    unittest.main()
