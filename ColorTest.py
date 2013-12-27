from Color import *
import unittest

class ColorTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_red(self):
        c = Color("R")
        self.assertEqual(str(c), "R")

    def test_blue(self):
        c = Color("B")
        self.assertEqual(str(c), "B")

    def test_yellow(self):
        c = Color("J")
        self.assertEqual(str(c), "J")

    def test_green(self):
        c = Color("V")
        self.assertEqual(str(c), "V")

    def test_wrong(self):
         self.assertRaises(ColorException, Color, "Y")

    def test_equality(self):
        b1 = Color("B")
        b2 = b1.copy()
        
        self.assertNotEqual(b1, b2)
        self.assertTrue(b1.equals(b2))
        
    def test_inequality(self):
        b = Color("B")
        v = Color("V")

        self.assertTrue(not b.equals(v))

if __name__ == "__main__":
    unittest.main()
