#!/usr/bin/python3
'''
LEGB (LOCAL-ENCLOSING-GLOBAL-BUILTIN)
'''

x = 'String global x (main scope)'
print(x)

def testfunc(z):
    y = 'String local y (local scope)'
    #x = 'String local (local scope)'
    
    # global x # Should not be a standard used way
    # x = 'String now global x (global scope)'
    
    print(z)
    print(x)
    print(y)

testfunc('Strin local z (local scope)')
print(x)

# print(y) this will throw an error because y is local to testfunc
# print(z) this will throw an error because z is local to testfunc

# BUILTINs examples
m = min([29,39,2,19,4,0,3])
print(m)

# import builtins
# print(dir(builtins))

## the following will override min in the global scope (Should not be done)
# def min():
#     pass
# min([4,2,5]) ## will throw an error because min was overriden

## NESTED FUNCTION (ENCLOSING)
def outer():
    x = 'outer x'

    def inner_0():
        #x = 'inner x'
        print(x) ## uses the outer x because inner has no x in it's scope, but outer has an x defined

    def inner_1():
        x = 'inner x'
        print(x) ## uses the inner x because inner has an x in it's scope

    def inner_2():
        nonlocal x ## this keyword sets the affected x to the outer scope x
        x = 'outer x affected'
        print(x) ## uses the outer x because inner has no x in it's scope, but outer has an x defined
    
    inner_0()
    inner_1()

    inner_2()
    print(x)

outer()

def outer():
    #x = 'outer x'

    def inner_0():
        #x = 'inner x'
        print(x) ## uses the global scope x because inner and outer have no x in there scopes, but global has an x defined
    
    inner_0()

outer()
