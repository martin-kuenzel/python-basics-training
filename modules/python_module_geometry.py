import math

print(f'successfully imported module {__file__}')

class geometry:
    def __init__(self):
        pass
    def __str__(self):
        return f'{type(self)}'

class circle(geometry):
    radius = 1
    def __init__(self,radius=1):
        super()
        self.radius = radius
    def get_area(self):
        return ( self.radius**2 ) * math.pi
    def get_diameter(self):
        return ( self.radius * 2 )
    def get_circumference(self):
        return self.get_diameter() * math.pi
    def __str__(self):
        return f'{super.__str__(self)}\ncircle with radius {self.radius}:\n\tDiameter: {self.get_diameter()}\n\tCircumference: {self.get_circumference()}\n'

class triangle(geometry):
    a = 1
    b = 1
    def __init__(self,a=1,b=1,**kwargs):
        super()
        self.a = a
        self.b = b
        if not kwargs.get('C') == None:
            self.C = kwargs.get('C')
        else:
            print('Triangle need either information about the angle between two given sides, but no argument C was found assuming 90° probably wrong')
            self.C = 90
        self.C_rad = math.radians(self.C)
        self.c = self.get_c()
    def get_c(self):
        return math.sqrt(
            self.a**2 + self.b**2 - ( 2 * self.a * self.b * round( math.cos( self.C_rad ) ) )
        )
    def get_circumcircle(self):
        radius = (
            ( self.a * self.b * self.c ) / 
            math.sqrt( ( self.a + self.b + self.c ) * ( self.b + self.c - self.a) * ( self.c + self.a - self.b ) * ( self.a + self.b - self.c ) )
        )
        return circle( radius= radius )

    def get_area(self):
        return 0.5 * ( self.a + self.b + self.get_c() )
    def __str__(self):
        return f'''{super.__str__(self)}\ntriangle with: \n\ta: {self.a}:\n\tb: {self.b}\n\tc: {self.get_c()}\n\tC: {math.degrees(self.C)}°\n\tArea: {self.get_area()}\n\tcircumcircle:\n{self.get_circumcircle()}'''

class square(geometry):
    def __init__(self,a=1,b=1):
        super()
        self.a = a
        self.b = b
    def get_area(self):
        return self.a * self.b
    def get_perimeter(self):
        return 2 * ( self.a + self.b )
    def get_diagonal(self):
        return triangle( self.a, self.b, C = 90 ).get_c()
    def get_circumcircle(self):
        return circle( radius = self.get_diagonal() )

    def __add__(self,s):
        return square(self.a+s.a,self.b+s.b)
    def __mul__(self,s):
        return square(self.a*s.a,self.b*s.b)
    def __sub__(self,s):
        return square(self.a-s.a,self.b-s.b)
    def __truediv__(self,s):
        return square(self.a/s.a,self.b/s.b)
    def __floordiv__(self,s):
        return square(self.a//s.a,self.b//s.b)
    def __mod__(self,s):
        return square(self.a%s.a,self.b%s.b)
    def __pow__(self,s):
        return square(self.a**s.a,self.b**s.b)

    def __iadd__(self,s):
        self.a += s.a
        self.b += s.b
        return self
    def __imul__(self,s):
        self.a *= s.a
        self.b *= s.b
        return self
    def __isub__(self,s):
        self.a -= s.a
        self.b -= s.b
        return self
    def __itruediv__(self,s):
        self.a /= s.a
        self.b /= s.b
        return self
    def __ifloordiv__(self,s):
        self.a //= s.a
        self.b //= s.b
        return self
    def __imod__(self,s):
        self.a %= s.a
        self.b %= s.b
        return self
    def __ipow__(self,s):
        self.a **= s.a
        self.b **= s.b
        return self

    def __lt__(self,s):
        return self.get_area() < s.get_area()
    def __gt__(self,s):
        return self.get_area() > s.get_area()
    def __eq__(self,s):
        return self.get_area() == s.get_area()
    def __ne__(self,s):
        return self.get_area() != s.get_area()
    def __le__(self,s):
        return self.get_area() <= s.get_area()
    def __ge__(self,s):
        return self.get_area() >= s.get_area()
    
    def __neg__(self):
        return square(-self.a, -self.b)
    def __pos__(self):
        return square(+self.a, +self.b)
    def __invert__(self):
        return square(~self.a, ~self.b)

    def __str__(self):
        return f'''{super.__str__(self)}\nsquare with: \n\ta: {self.a}:\n\tb: {self.b}\n\tdiagonal: {self.get_diagonal()}\n\tPerimeter: {self.get_perimeter()}\n\tArea: {self.get_area()}\n\tcircumcircle:\n{self.get_circumcircle()}'''