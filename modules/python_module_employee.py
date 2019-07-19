#!/usr/bin/python3
from datetime import date

print(f'successfully imported module {__file__}')

class Employee:
    emp_no = 0
    salary_raise_rate = 1.02
    salary = 1000

    @classmethod
    def set_raise_amount(cls,amount):
        cls.salary_raise_rate = amount

    @classmethod
    def from_string(cls,string):
        pername,name = string.split('-')
        return cls(pername,name)

    @staticmethod
    def is_workday(day):
        return -1 < day.weekday() < 5

    def __init__(self, pername = 'John', name = 'Doe'):
        self.emp_no = Employee.emp_no
        self.pername = pername
        self.name = name
        self.salary = Employee.salary
        self.salary_raise_rate = Employee.salary_raise_rate
        Employee.emp_no += 1

    def fullname(self):
        return f'{self.pername} {self.name}'

    def raise_salary(self):
        new_salary = self.salary * self.salary_raise_rate
        print( f'Salary of {self.pername} {self.name} raised by {new_salary - self.salary}' )
        self.salary = new_salary

    def __str__(self):
        return f'EmpNo:{self.emp_no}, Name: {self.fullname()}, salary: {self.salary} ({self.salary_raise_rate})'

emp_0 = Employee('Jim','Bow')

print(emp_0)

Employee.set_raise_amount( 1.025 )
print(f'Salary raise rate of {Employee} set to {Employee.salary_raise_rate}')

#emp_1 = Employee('Ten','Isbal')
emp_1 = Employee.from_string('Ten-Isbal')
emp_2 = Employee('Whee','El Chair')

print(f'''
{emp_0}

{emp_1}

{emp_2}
''')

emp_2.salary_raise_rate = 1.05
print(f'Salary raise rate of {emp_2.fullname()} set to {emp_2.salary_raise_rate}')

emp_0.raise_salary()
emp_1.raise_salary()
emp_2.raise_salary()

print(f'''
{emp_0}

{emp_1}

{emp_2}
''')

print( f'Today {date.today().strftime("%c")} is{ [" not "," "][int( Employee.is_workday( date.today() ) )] }a workday')