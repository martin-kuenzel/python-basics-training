# integers
num = 3 
# floats
fnum = 3.0

### arithmetic operators
print(f'''
### arithmetic operators
type(3)   = {type(num)}
type(3.0) = {type(3.0)}

Subtraction: 3-1 = {3-1}
Addition: 3+1 = {3+1}
Division: 3/2 = {3/2}
Multiplication: 3*2 = {3*2}

math.floor(3/2) ## requires 'import math' ##
Floor division: 3//2 = {3//2} ## doesn't require import math

Modulus: 3%2 = {3%2} 
Exponent: 3**2 = {3**2}

Binding calculations:
3+2*2 = {3+2*2}
3+(2*2) = {3+(2*2)}
(3+2)*2 = {(3+2)*2}

''')

num=1
num+=1
print(f'''
Bindoperators
num  = 1 
num += 1
num  = {num}
''')

num=2
num-=1
print(f'''num  = 2
num -= 1
num  = {num}
''')

num=1
num*=2
print(f'''num  = 1 
num *= 2
num  = {num}
''')

num=1
num/=2
print(f'''num  = 1 
num /= 2
num  = {num}
''')

num=1
num//=2
print(f'''num  = 1 
num //= 2
num  = {num}
''')

num=3
num%=2
print(f'''num  = 3 
num %= 2
num  = {num}
''')

num=3
num**=2
print(f'''num  = 3 
num **= 2
num  = {num}
''')

print(f'''
### builtin functions
abs(-1) = {abs(-1)}
round(1.25) = {round(1.25)}

### comparing numbers
1 == 2 = {1==2}
2 == 2 = {2==2}
2 >= 1 = {2>=1}
2 <= 1 = {2<=1}
''')

num_1 = '100'
num_2 = '200'
print(f'''
### type casting
num_1 = '100'
num_2 = '200'
num_1 + num_2 = {num_1 + num_2}
''')

num_1 = int(num_1)
num_2 = int(num_2)
print(f'''num_1 = int(num_1)
num_2 = int(num_2)
num_1 + num_2 = {num_1 + num_2}
''')
