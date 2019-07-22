#unit testing basics_unit_testing.py
#reference documentation about asserts
import unittest
from python_basics_unit_testing import add, sub, mul, div

class TestPythonBasicsUnitTesting(unittest.TestCase):

    ## !! TEST METHODS HAVE TO START WITH test_ TO BE CONSIDERED FOR THE UNITTESTING !!

    def test_add(self):
        self.assertEqual(add(2,5), 7)
        self.assertEqual(add(2), 2)
        self.assertNotEqual(add(2), 4)
        
    def test_sub(self):
        self.assertEqual(sub(2,5), -3)
        self.assertNotEqual(sub(2,2), 4)

    def test_mul(self):
        self.assertEqual(mul(2,5), 10)
        self.assertEqual(mul(2), 0)

    def test_div(self):
        self.assertEqual(div(2,5), 2/5)
        self.assertEqual(div(2), 2)
        
        # self.assertRaises( ValueError, div, 2, 0 )
        ### ASSERTION ON RAISES CAN BE USED WITH CONTEXT MANAGER AS FOLLOWS
        with self.assertRaises( ValueError ):
            div(2,0)

        with self.assertRaises( TypeError ):
            div(2,None)

## allows using the unittests directly from the module
## without the need for: python3 -m unittest test_basics_unit_testing.py
if __name__ == '__main__':
    unittest.main()