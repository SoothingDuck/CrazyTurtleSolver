from TurtlePart import *
import unittest

class TurtlePartTest(unittest.TestCase):

    def test_head(self):
        t = TurtlePart("T")
        self.assertEqual(str(t), "Tete")

    def test_body(self):
        t = TurtlePart("C")
        self.assertEqual(str(t), "Corps")

    def test_wrong(self):
        self.assertRaises(TurtlePartException, TurtlePart, "A")

    def test_equality(self):
        c1 = TurtlePart("C")
        c2 = TurtlePart("C")

        self.assertEqual(c1, c2)

    def test_inequality(self):
        c = TurtlePart("C")
        t = TurtlePart("T")

        self.assertNotEqual(c, t)

if __name__ == "__main__":
    unittest.main()
