from Turtle import *
from Color import *
from TurtlePart import *
import unittest

class TurtleTest(unittest.TestCase):
    
    def test_initturtle(self):
        t1 = Turtle("CR")
        
        self.assertTrue(t1.part.equals(TurtlePart("C")))
        self.assertTrue(t1.color.equals(Color("R")))

        t2 = Turtle("TV")

        self.assertTrue(t2.part.equals(TurtlePart("T")))
        self.assertTrue(t2.color.equals(Color("V")))

        t3 = Turtle("CJ")

        self.assertTrue(t3.part.equals(TurtlePart("C")))
        self.assertTrue(t3.color.equals(Color("J")))

        t4 = Turtle("TB")

        self.assertTrue(t4.part.equals(TurtlePart("T")))
        self.assertTrue(t4.color.equals(Color("B")))

    def test_equality(self):
        t1 = Turtle("TB")
        t2 = Turtle("TB")

        self.assertNotEqual(t1, t2)
        self.assertTrue(t1.equals(t2))

    def test_inequality(self):
        t1 = Turtle("TB")
        t2 = Turtle("TV")
        t3 = Turtle("CB")

        self.assertFalse(t1.equals(t2))
        self.assertFalse(t2.equals(t3))
        self.assertFalse(t3.equals(t1))

    def test_copy(self):
        t1 = Turtle("TB")
        t2 = t1.copy()

        # self.assertFalse(t1 == t2)
        self.assertTrue(t1.equals(t2))

    def test_matches(self):
        t1 = Turtle("TB")
        t2 = Turtle("CB")
        t3 = Turtle("TJ")

        self.assertTrue(t1.matches(t2))
        self.assertTrue(t2.matches(t1))
        self.assertFalse(t1.matches(t3))
        self.assertFalse(t2.matches(t3))


    def test_wrongdef(self):

        self.assertRaises(TurtleException, Turtle, "TBB")
        self.assertRaises(TurtlePartException, Turtle, "BB")
        self.assertRaises(ColorException, Turtle, "CY")

    def test_string(self):

        t = Turtle("TV")
        self.assertEqual(str(t), "TV")

        t = Turtle("TB")
        self.assertEqual(str(t), "TB")

        t = Turtle("CJ")
        self.assertEqual(str(t), "CJ")

    def test_matching(self):

        t1 = Turtle("TV")
        t2 = Turtle("CV")
        t3 = Turtle("CB")
        t4 = Turtle("TV")

        self.assertTrue(t1.matches(t2))
        self.assertFalse(t1.matches(t3))
        self.assertFalse(t1.matches(t4))
        
        

if __name__ == "__main__":
    unittest.main()
