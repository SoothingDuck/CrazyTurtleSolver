from TurtlePart import *
import unittest

class TurtlePartTest(unittest.TestCase):

    def test_head(self):
        t = TurtlePart("T")
        self.assertEqual(str(t), "T")

    def test_body(self):
        t = TurtlePart("C")
        self.assertEqual(str(t), "C")

    def test_wrong(self):
        self.assertRaises(TurtlePartException, TurtlePart, "A")

    def test_equality(self):
        c1 = TurtlePart("C")
        c2 = TurtlePart("C")

        self.assertNotEqual(c1, c2)
        self.assertTrue(c1.equals(c2))

    def test_matches(self):
        c1 = TurtlePart("C")
        c2 = TurtlePart("C")
        c3 = TurtlePart("T")

        self.assertTrue(c1.matches(c3))
        self.assertFalse(c1.matches(c2))


    def test_copy(self):
        c1 = TurtlePart("C")
        c2 = c1.copy()

        self.assertTrue(c1.equals(c2))

    def test_inequality(self):
        c = TurtlePart("C")
        t = TurtlePart("T")

        self.assertTrue(not c.equals(t))

if __name__ == "__main__":
    unittest.main()
