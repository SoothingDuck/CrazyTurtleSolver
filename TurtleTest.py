from Turtle import *
from Color import *
from TurtlePart import *
import unittest

class TurtleTest(unittest.TestCase):
    
    def test_initturtle(self):
        t1 = Turtle("CR")
        
        self.assertEqual(t1.part, TurtlePart("C"))
        self.assertEqual(t1.color, Color("R"))

        t2 = Turtle("TV")

        self.assertEqual(t2.part, TurtlePart("T"))
        self.assertEqual(t2.color, Color("V"))

        t3 = Turtle("CJ")

        self.assertEqual(t3.part, TurtlePart("C"))
        self.assertEqual(t3.color, Color("J"))

        t4 = Turtle("TB")

        self.assertEqual(t4.part, TurtlePart("T"))
        self.assertEqual(t4.color, Color("B"))

    def test_equality(self):
        t1 = Turtle("TB")
        t2 = Turtle("TB")

        self.assertEqual(t1, t2)

    def test_inequality(self):
        t1 = Turtle("TB")
        t2 = Turtle("TV")
        t3 = Turtle("CB")

        self.assertNotEqual(t1, t2)
        self.assertNotEqual(t2, t3)
        self.assertNotEqual(t3, t1)

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
