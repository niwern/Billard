import math


class vektor(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __add__(self, other):
        return vektor(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return self.x*other.x + self.y*other.y

    def __imul__(self, other):
        return vektor(self.x*other, self.y*other)

    def norm(self):
        return vektor(self.x/abs(self), self.y/abs(self))

    def __repr__(self):
        return "({}, {})".format(self.x, self.y)

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

if __name__ == "__main__":
    v = vektor(0, 2)
    print(abs(v))
    print(v.norm())
