import unittest
from mymodule import square, double, add

class TestSquare(unittest.TestCase): 
    """
    A test class for the 'square' function in mymodule.
    """
    def test1(self): 
        self.assertEqual(square(2), 4) # test when 2 is given as input the output is 4.
        self.assertEqual(square(3.0), 9.0)  # test when 3.0 is given as input the output is 9.0.
        self.assertNotEqual(square(-3), -9)  # test when -3 is given as input the output is not -9.
        

class TestDouble(unittest.TestCase): 
    """
    A test class for the 'Double' function in mymodule.
    """
    def test1(self): 
        self.assertEqual(double(2), 4) # test when 2 is given as input the output is 4.
        self.assertEqual(double(-3.1), -6.2) # test when -3.1 is given as input the output is -6.2.
        self.assertEqual(double(0), 0) # test when 0 is given as input the output is 0.

class TestAddFunction(unittest.TestCase):
    """
    A test class for the 'add' function in mymodule.
    """
    def test_positive_integers(self):
        """
        Test the 'add' function with positive integers.
        """
        result = add(2, 4)  # Call the 'add' function with 2 and 4 as input
        self.assertEqual(result, 6)  # Check if the result is equal to 6

    def test_both_zeros(self):
        """
        Test the 'add' function with both input numbers as zero.
        """
        result = add(0, 0)  # Call the 'add' function with 0 and 0 as input
        self.assertEqual(result, 0)  # Check if the result is equal to 0

    def test_floats(self):
        """
        Test the 'add' function with floating-point numbers.
        """
        result = add(2.3, 3.6)  # Call the 'add' function with float numbers
        self.assertEqual(result, 5.9)  # Check if the result is equal to 5.9

    def test_strings(self):
        """
        Test the 'add' function with string inputs.
        """
        result = add('hello', 'world')  # Call the 'add' function with strings
        self.assertEqual(result, 'helloworld')  # Check if the result is 'helloworld'

    def test_float_inputs(self):
        """
        Test the 'add' function with floating-point inputs.
        """
        result = add(2.3000, 4.300)  # Call the 'add' function with float numbers
        self.assertEqual(result, 6.6)  # Check if the result is equal to 6.6

    def test_negative_integers(self):
        """
        Test the 'add' function with negative integers.
        """
        result = add(-2, -2)  # Call the 'add' function with negative integers
        self.assertNotEqual(result, 0)  # Check if the result is not equal to 0

if __name__ == '__main__':
    unittest.main()  # Run the unit tests
