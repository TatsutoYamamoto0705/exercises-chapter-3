from numbers import Number
from math import sqrt


class Circle:

    def __init__(self, centre, radius):
        self.centre = centre
        self.radius = radius
    
    def __contains__(self, other):

        if isinstance(other, tuple):
            distance = sqrt((self.centre[0]-other[0])**2+(self.centre[1]-other[1])**2)
            if distance < self.radius:
                return True
            else:
                return False

        else:
            return NotImplemented
            

            