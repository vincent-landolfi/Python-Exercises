import math


class Parallelogram():
    "A four sided shape with parallel pairs of sides"

    def __init__(self, base, side, theta):
        '''(Parallelogram,int,int,float) -> NoneType
        Create a new parallelogram with the given
        base length, side length, and angle theta
        REQ: base,side,theta >= 0
        '''
        # assign all parameters to class variables
        self._base = base
        self._side = side
        self._theta = theta

    def area(self):
        '''(Parallelogram) -> int or float
        Returns the area of the parallelogram
        '''
        # convert to radians
        self._radians = math.radians(self._theta)
        # return the area with the formula
        return (self._base * self._side * (math.sin(self._radians)))

    def bst(self):
        '''(Parallelogram) -> list or int/float
        Returns a list of base and side lengths as
        well as angle theta`
        '''
        # return a list of the three values
        return [self._base, self._side, self._theta]

    def __str__(self):
        '''(Parallelogram) -> str
        Returns a string telling the area of
        the parallelogram
        '''
        # make the string to return
        return "I am a " + self.__class__.__name__ +\
               " with area " + str(self.area())


class Rectangle(Parallelogram):
    "A rectangle inheriting all methods from paralleogram"

    def __init__(self, base, side):
        '''(Rectangle,int,int) -> NoneType
        Make a new rectangle with the given base
        and side length, with a preset theta of 90
        REQ: base,side >= 0
        '''
        # use the init from parallelogram since rectangle is parallelogram
        Parallelogram.__init__(self, base, side, 90)


class Rhombus(Parallelogram):
    "A rhombus inheriting all methods from parallelogram"

    def __init__(self, base, theta):
        '''(Rhombus,int) -> NoneType
        Makes a new rhombus with the given base and
        side length (since equal) and a preset theta
        REQ: base,theta >= 0
        '''
        # use the init from parallelogram since rhombus is parallelogram
        Parallelogram.__init__(self, base, base, theta)


class Square(Rhombus):
    "A square inheriting methods from rhombus"

    def __init__(self, base):
        '''(Square,int) -> NoneType
        Makes a new square with given side base length
        since all side are equal
        REQ: base >= 0
        '''
        # use init from rhombus since square is a rhombus
        # could also inherit from rectanlge, either works
        Rhombus.__init__(self, base, 90)
