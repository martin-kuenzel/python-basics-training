#!/usr/bin/python3

def add(a=0,b=0):
    return a + b

def sub(a=0,b=0):
    return a - b

def mul(a=0,b=0):
    return a * b

def div(a=0,b=1):
    if b == 0: 
        raise ValueError('Div/0 Exception')
    return a / b

