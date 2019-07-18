#!/usr/bin/python3
from modules.python_module_geometry import geometry, circle, triangle, square

## Trigonometry is not mine, but it's a good way to let classes interact with each other
geometry_1 = geometry()

circle_1 = circle(4)
print(circle_1)

triangle_1 = triangle(a=7,b=7)
print(triangle_1)

print('square_1 = square(2,2)')
square_1 = square(2,2)
print('square_2 = square(2,2)')
square_2 = square(2,2)

print('print(square_1+square_2)\n')
print(square_1+square_2)
print('print(square_1-square_2)\n')
print(square_1-square_2)
print('print(square_1*square_2)\n')
print(square_1*square_2)
print('print(square_1/square_2)\n')
print(square_1/square_2)
print('print(square_1//square_2)\n')
print(square_1//square_2)
print('print(square_1%square_2)\n')
print(square_1%square_2)
print('print(square_1**square_2)\n')
print(square_1**square_2)

print('print(square_1>square_2)\n')
print(square_1>square_2)
print('print(square_1<square_2)\n')
print(square_1<square_2)
print('print(square_1<=square_2)\n')
print(square_1<=square_2)
print('print(square_1>=square_2)\n')
print(square_1>=square_2)
print('print(square_1==square_2)\n')
print(square_1==square_2)
print('print(square_1!=square_2)\n')
print(square_1!=square_2)

print('''
print(-square_1)
''')
print(-square_1)
print('''
print(+square_1)
''')
print(+square_1)
print('''
print(~square_1)
''')
print(~square_1)

print('''
square_1 += square_2
print(square_1)
''')
square_1 += square_2
print(square_1)
print('''
square_1 -= square_2
print(square_1)
''')
square_1 -= square_2
print(square_1)
print('''
square_1 *= square_2
print(square_1)
''')
square_1 *= square_2
print(square_1)
print('''
square_1 /= square_2
print(square_1)
''')
square_1 /= square_2
print(square_1)
print('''
square_1 //= square_2
print(square_1)
''')
square_1 //= square_2
print(square_1)
print('''
square_1 **= square_2
print(square_1)
''')
square_1 **= square_2
print(square_1)
print('''
square_1 %= square_2
print(square_1)
''')
square_1 %= square_2
print(square_1)
