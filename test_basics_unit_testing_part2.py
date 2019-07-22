#!/usr/bin/python3

import unittest

from unittest.mock import patch ## RELATING TO WEB REQUESTS SITUATION

from python_basics_unit_testing_part2 import Employee

class TestTestBasicsUnitTestingPart2(unittest.TestCase):

    ### TESTS SHOULD BE ISOLATED, SO THEY CAN BE RUN EACH ON THERE OWN WITHOUT AFFECTING OTHERS ###

    ### IS RUN ONLY ONCE BEFORE TESTING STARTS (FOR EXAMPLE PREPARATION OF A DATABASE)
    @classmethod
    def setUpClass(self):
        print('\nstarted unit testing')

    ### IS RUN ONLY ONCE AFTER TESTING IS FINISHED (FOR EXAMPLE UNLOADING OF A DATABASE)
    @classmethod
    def tearDownClass(self):
        print('\nfinished unit testing')

    ### !! TO NOT FALL INTO DRY WE CAN USE THE FOLLOWING TWO METHODS !!
    
    ## IS RUN BEFORE EACH TEST
    def setUp(self):
        print('\nSetting up !!')
        self.emp_0 = Employee('John','Doe',23,1203)
        self.emp_1 = Employee('Jack','Miller',52,4003)
    
    ## IS RUN AFTER EACH TEST (USEFUL IF WE WORK WITH DATABASES)
    def tearDown(self):
        print('Tearing up !!')
        pass

    def test_email(self):
        print('testing email')
        self.assertEqual(self.emp_0.email,'John.Doe@theBigFirm.com')
        self.emp_0.firstname = 'Mike'
        self.assertEqual(self.emp_0.email,'Mike.Doe@theBigFirm.com')

    def test_fullname(self):
        print('testing fullname')
        self.assertEqual(self.emp_1.fullname,'Jack Miller')
        self.emp_1.name = 'Meyer'
        self.assertEqual(self.emp_1.fullname,'Jack Meyer')
    
    def test_apply_raise(self):
        print('testing apply_raise')
        self.emp_0.apply_raise()
        self.emp_1.apply_raise()

        self.assertEqual(self.emp_0.salary, int(1203*1.05))
        self.assertEqual(self.emp_1.salary, int(4003*1.05))

    ## SPECIFICALLY PROBLEM WITH WEBREQUESTS
    def test_monthly_schedule(self):
        print('testing test_monthly_schedule (web requests)')
        
        ## A SUCCESSFUL REQUEST
        with patch('python_basics_unit_testing_part2.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_0.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Doe/May')
            self.assertEqual(schedule,'Success')
        
        ## A FAILED REQUEST
        with patch('python_basics_unit_testing_part2.requests.get') as mocked_get:
            mocked_get.return_value.ok = False

            schedule = self.emp_1.monthly_schedule('Sep')
            mocked_get.assert_called_with('http://company.com/Miller/Sep')
            self.assertEqual(schedule,'Bad response')

## allows using the unittests directly from the module
## without the need for: python3 -m unittest test_basics_unit_testing.py
if __name__ == '__main__':
    unittest.main()


### HINT: THERE IS ALSO ANOTHER FRAMEWORK CALLED PYTEST FOR UNITTESTING ###