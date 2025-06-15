from simple_calculator import SimpleCalculator
import unittest

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(3,5), 8)
        self.assertEqual(self.calc.add(3,-3), 0)
        self.assertEqual(self.calc.add(3,-5), -2)
    
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(90, 10), 80)
        self.assertEqual(self.calc.subtract(10, 10), 0)
        self.assertEqual(self.calc.subtract(-25, -10), -15)


    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(9, 5), 45)
        self.assertEqual(self.calc.multiply(2, 15), 30)
        self.assertEqual(self.calc.multiply(0, 0), 0)


    def test_division(self):
        self.assertEqual(self.calc.divide(2,1), 2)
        self.assertEqual(self.calc.divide(3,0), None)
        self.assertEqual(self.calc.divide(-84,2), -42)

    
if __name__ == "__main__":
    unittest.main()  
