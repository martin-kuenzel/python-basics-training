#!/usr/bin/python3
from datetime import date

print(f'successfully imported module {__file__}')

class Employee:
    emp_no = 0
    salary_raise_rate = 1.02
    paid = 0

    @classmethod
    def set_raise_amount(cls,amount):
        cls.salary_raise_rate = amount

    @classmethod
    def from_string(cls,string):
        firstname,name = string.split('-')
        return cls(firstname,name)

    @staticmethod
    def is_workday(day):
        return -1 < day.weekday() < 5

    def __init__(self, firstname = 'John', name = 'Doe', salary = 1000):
        self.emp_no = Employee.emp_no
        self.firstname = firstname
        self.name = name
        self.salary = salary
        print (f'New Employee begins his work \n\t{self}\n')
        Employee.emp_no += 1

    def fullname(self):
        return f'{self.firstname} {self.name}'

    def raise_salary(self):
        old_salary = self.salary
        self.salary *= self.salary_raise_rate
        print( f'Salary of {self.fullname()} raised by {self.salary-old_salary}' )

    def pay(self):
        self.paid += self.salary
        print( f'{self.fullname()} has been paid {self.salary} and now owns {self.paid}' )


    def __str__(self):
        
        return f'EmpNo:{self.emp_no}, Name: {self.fullname()}, Profession: {self.__class__.__name__}, Salary: {self.salary} ({self.salary_raise_rate}), Paid: {self.paid}'


## TESTBASE BASIC CLASSES ##
# emp_0 = Employee('Jim','Bow')

# print(emp_0)

# Employee.set_raise_amount( 1.025 )
# print(f'Salary raise rate of {Employee} set to {Employee.salary_raise_rate}')

# #emp_1 = Employee('Ten','Isbal')
# emp_1 = Employee.from_string('Ten-Isbal')
# emp_2 = Employee('Whee','El Chair')

# print(f'''
# {emp_0}

# {emp_1}

# {emp_2}
# ''')

# emp_2.salary_raise_rate = 1.05
# print(f'Salary raise rate of {emp_2.fullname()} set to {emp_2.salary_raise_rate}')

# emp_0.raise_salary()
# emp_1.raise_salary()
# emp_2.raise_salary()

# print(f'''
# {emp_0}

# {emp_1}

# {emp_2}
# ''')

# print( f'Today {date.today().strftime("%c")} is{ [" not "," "][int( Employee.is_workday( date.today() ) )] }a workday')

## TESTBASE CLASS INHERITANCE ##

class Developer(Employee):
    salary_raise_rate = 1.05
    def __init__(self,firstname,name,prog_lang,salary=2000):
        self.prog_lang = prog_lang
        super().__init__(firstname,name,salary)
    
    def __str__(self):
        return f'{super().__str__()}, Programming language: {self.prog_lang}'
    
class Manager(Employee):
    salary_raise_rate = 1.075
    def __init__(self,firstname,name,salary=3000,employees=None):
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
        super().__init__(firstname,name,salary)
    
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
            print(f'{emp.fullname()} is now managed by {self.fullname()}')
    
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
            print(f'{emp.fullname()} is no longer managed by {self.fullname()}')
    
    def emps_str(self):
        str = f'-- Employees managed by {self.fullname()} --'
        if len(self.employees) < 1: 
            str += '\n\tNone'
        for emp in self.employees:
            str += f'\n\t{emp.fullname()}'
        return str

    def print_emps(self):
        print(self.emps_str())

    def __str__(self):
        return f'{super().__str__()}\n{self.emps_str()}'

dev_0 = Developer('Hacka', 'Lot','JavaScript')

dev_0.pay()
dev_0.raise_salary()

dev_0.pay()

man_0 = Manager('Iown','Ju')
man_0.raise_salary()
man_0.pay()

man_0.add_emp(dev_0)
man_0.print_emps()
man_0.remove_emp(dev_0)
man_0.print_emps()