#!/usr/bin/python3
from datetime import date

print(f'successfully imported module {__file__}')

class Employee:
    emp_no = 0
    salary_raise_rate = 1.02
    paid = 0

    @staticmethod
    def is_workday(day):
        return -1 < day.weekday() < 5

    @classmethod
    def set_raise_amount(cls,amount):
        cls.salary_raise_rate = amount

    @classmethod
    def from_string(cls,string):
        firstname,name = string.split('-')
        return cls(firstname,name)

    def __init__(self, firstname = 'John', name = 'Doe', salary = 1000):
        self.emp_no = Employee.emp_no
        self.firstname = firstname
        self.name = name
        self.salary = salary
        print (f'New Employee begins his work \n\t{self}\n')
        Employee.emp_no += 1

    def raise_salary(self):
        old_salary = self.salary
        self.salary *= self.salary_raise_rate
        print( f'Salary of {self.fullname} raised by {self.salary-old_salary}' )

    def pay(self):
        self.paid += self.salary
        print( f'{self.fullname} has been paid {self.salary} and now owns {self.paid}' )

## Concept of a property

    @property
    def fullname(self):
        return f'{self.firstname} {self.name}'

    @fullname.setter
    def fullname(self,full_name):
        print(f'Changing full name from {self.fullname} to {full_name}')
        self.firstname, self.name = full_name.split('|')

    @fullname.deleter
    def fullname(self):
        print(f'Deleting name of {self.fullname}')
        self.firstname = None
        self.name = None

## //Concept of a property 

    def __repr__(self):
        return(f'Employee({self.firstname},{self.name},{self.salary})')

    def __str__(self):
        return f'EmpNo:{self.emp_no}, Name: {self.fullname}, Profession: {self.__class__.__name__}, Salary: {self.salary} ({self.salary_raise_rate}), Paid: {self.paid}'


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
# print(f'Salary raise rate of {emp_2.fullname} set to {emp_2.salary_raise_rate}')

# emp_0.raise_salary()
# emp_1.raise_salary()
# emp_2.raise_salary()

# print(f'''
# {emp_0}

# {emp_1}

# {emp_2}
# ''')

# print( f'Today {date.today().strftime("%c")} is{ [" not "," "][int( Employee.is_workday( date.today() ) )] }a workday')
    
class Manager(Employee):
    salary_raise_rate = 1.075
    def __init__(self,firstname,name,salary=3000,employees=None):
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
        super().__init__(firstname,name,salary)
    
    def add_emp(self, emp):
        if not self is emp and emp not in self.employees:
            self.employees.append(emp)
            print(f'{emp.fullname} is now managed by {self.fullname}')
    
    def remove_emp(self, emp):
        if not self is emp and emp in self.employees:
            self.employees.remove(emp)
            print(f'{emp.fullname} is no longer managed by {self.fullname}')
    
    def __add__(self, emp):
        self += emp
        return self

    def __sub__(self, emp):
        self -= emp
        return self

    def __iadd__(self, emp):
        self.add_emp(emp)
        return self

    def __isub__(self, emp):
        self.remove_emp(emp)
        return self
    
    def emps_str(self):
        str = f'-- Employees managed by {self.fullname} --'
        if len(self.employees) < 1: 
            str += '\n\tNone'
        for emp in self.employees:
            str += f'\n\t{emp.fullname}'
        return str

    def print_emps(self):
        print(self.emps_str())

    def __str__(self):
        return f'{super().__str__()}\n{self.emps_str()}'

class Developer(Employee):
    salary_raise_rate = 1.05
    prog_langs = []
    
    def __init__(self,firstname,name,prog_langs = None,salary=2000):
        if prog_langs is None: 
            raise TypeError(f'{__class__.__name__} need at least one prog_lang!')
        elif type(prog_langs) is type(str()): 
            prog_langs = [prog_langs]
        elif not type(prog_langs) is type([]):
            raise TypeError()

        for prog_lang in prog_langs:
            if not prog_lang in self.prog_langs:
                self.prog_langs.append( prog_lang )

        super().__init__(firstname,name,salary)
    
    def __iadd__(self, prog_langs):
        if type(prog_langs) is type(str()): 
            prog_langs = [prog_langs]
        elif not type(prog_langs) is type([]):
            raise TypeError()

        for prog_lang in prog_langs:
            if not prog_lang in self.prog_langs:
                print(f'{self.fullname} learned {prog_lang}')
                self.prog_langs.append( prog_lang )

        return self

    
    def __str__(self):
        return f'{super().__str__()}, Programming language: {self.prog_langs}'

## TESTBASE CLASS INHERITANCE, OPERATOR OVERLOADING ##

dev_0 = Developer('Ackthay', 'Neet','JavaScript')
dev_0.fullname = 'Hacka|Lot'

del dev_0.fullname
dev_0.fullname = 'Ackthay|Loot'

dev_0.pay()

man_0 = Manager('Owen','Ju')
man_0.raise_salary()
man_0.pay()

man_0 -= dev_0
man_0 += dev_0
man_0 += dev_0

dev_0 += ['Python','JavaScript','C++']
dev_0.raise_salary()
dev_0.pay()

dev_0 += 'R-Programming Lang'
dev_0.raise_salary()
dev_0.pay()

man_0 -= dev_0