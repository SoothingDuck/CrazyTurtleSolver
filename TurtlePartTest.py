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

if __name__ == "__main__":
    unittest.main()
