#!/usr/bin/python3

import requests  ## RELATING TO WEB REQUESTS SITUATION

class Employee():
    raise_amount = 1.05
    comp_email = 'theBigFirm.com'

    def __init__(self,firstname,name,age,salary):
        self.firstname = firstname
        self.name = name
        self.age = age
        self.salary = salary
    
    @property
    def email(self):
        return f'{self.firstname}.{self.name}@{self.comp_email}'

    @property
    def fullname(self):
        return f'{self.firstname} {self.name}'
    
    def apply_raise(self):
        self.salary = int( self.salary * self.raise_amount )

    ## SPECIFICALLY PROBLEM WITH WEBREQUESTS
    def monthly_schedule(self,month):
        response = requests.get(f'http://company.com/{self.name}/{month}')
        if response.ok:
            return response.text
        else:
            return 'Bad response'

