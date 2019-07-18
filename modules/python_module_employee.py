#!/usr/bin/python3

print(f'successfully imported module {__file__}')

class employee:
    emp_no = 0
    salary_raise_rate = 1.02
    name = 'John'
    pername = 'Doe'
    def set_salary_raise_rate(self,rate=1.0):
        self.salary_raise_rate = rate

    def __init__(self, pername = 'John', name = 'Doe', salary = 1000):
        self.emp_no = employee.emp_no
        self.pername = pername
        self.name = name
        self.salary = salary
        self.salary_raise_rate = employee.salary_raise_rate
        employee.emp_no += 1

    def fullname(self):
        return f'{self.pername} {self.name}'

    def raise_salary(self):
        new_salary = self.salary * self.salary_raise_rate
        print( f'Salary of {self.pername} {self.name} raised by {new_salary - self.salary}' )
        self.salary = new_salary

    def __str__(self):
        return f'EmpNo:{self.emp_no}, Name: {self.fullname()}, salary: {self.salary} ({self.salary_raise_rate})'

emp_0 = employee('Jim','Bow')

print(emp_0)

employee.set_salary_raise_rate(employee,1.025)
print(f'Salary raise rate of {employee} set to {employee.salary_raise_rate}')

emp_1 = employee('Ten','Isbal')
emp_2 = employee('Whee','El Chair')

print(f'''
{emp_0}

{emp_1}

{emp_2}
''')

emp_2.set_salary_raise_rate(1.05)
print(f'Salary raise rate of {emp_2.fullname()} set to {emp_2.salary_raise_rate}')

emp_0.raise_salary()
emp_1.raise_salary()
emp_2.raise_salary()

print(f'''
{emp_0}

{emp_1}

{emp_2}
''')