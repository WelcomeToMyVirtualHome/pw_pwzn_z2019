"""
Część 1 (1 pkt): Uzupełnij klasę Vector tak by reprezentowała wielowymiarowy wektor.
Klasa posiada przeładowane operatory równości, dodawania, odejmowania,
mnożenia (przez liczbę i skalarnego), długości
oraz nieedytowalny (własność) wymiar.
Wszystkie operacje sprawdzają wymiar.
Część 2 (1 pkt): Klasa ma statyczną metodę wylicznia wektora z dwóch punktów
oraz metodę fabryki korzystającą z metody statycznej tworzącej nowy wektor
z dwóch punktów.
Wszystkie metody sprawdzają wymiar.
"""
from operator import add, sub, mul
from math import sqrt
from numbers import Number

class Vector:
    def __init__(self, *args):
        self.dims = list(args)
        
    @staticmethod
    def calculate_vector(beg, end):
        """
        Calculate vector from given points

        :param beg: Begging point
        :type beg: list, tuple
        :param end: End point
        :type end: list, tuple
        :return: Calculated vector
        :rtype: tuple
        """
        return tuple(list(map(sub, end, beg)))

    @classmethod
    def from_points(cls, beg, end):
        """"""
        """
        Generate vector from given points.

        :param beg: Begging point
        :type beg: list, tuple
        :param end: End point
        :type end: list, tuple
        :return: New vector
        :rtype: tuple
        """
        return Vector(*Vector.calculate_vector(beg, end))

    @property
    def dim(self):
        return len(self.dims)

    @property
    def len(self):
        return sqrt(sum(list(map(lambda x: x ** 2, self.dims))))
        
    def __len__(self):
        return len(self.dims)

    def __eq__(self, v):
        if type(v) == Vector:
            if v.dim == self.dim:
                return self.dims == v.dims
            else:
                raise TypeError
        else:
            raise TypeError

    def __add__(self, v): 
        if type(v) == Vector:
            if v.dim == self.dim:
                return Vector(*(list(map(add, self.dims, v.dims))))  
            else:
                raise TypeError
        elif isinstance(v, Number):
            return Vector(*(list(map(lambda x: x + v, self.dims))))  
        else:
            raise TypeError
        
    def __sub__(self, v):
        if type(v) == Vector:
            if v.dim == self.dim:
                return Vector(*(list(map(sub, self.dims, v.dims))))  
            else:
                raise TypeError
        elif isinstance(v, Number):
            return Vector(*(list(map(lambda x: x - v, self.dims))))  
        else:
            raise TypeError
        
    def __mul__(self, v):
        if type(v) == Vector:
            if v.dim == self.dim:
                return sum(list(map(mul, self.dims, v.dims)))
            else:
                raise TypeError
        elif isinstance(v, Number):
            return Vector(*(list(map(lambda x: x * v, self.dims))))
        else:
            raise TypeError

    
if __name__ == '__main__':
    v1 = Vector(1,2,3)
    v2 = Vector(1,2,3)
    assert v1 + v2 == Vector(2,4,6)
    assert v1 - v2 == Vector(0,0,0)
    assert v1 * 2 == Vector(2,4,6)
    assert v1 * v2 == 14
    assert len(Vector(3,4)) == 2
    assert Vector(3,4).dim == 2
    assert Vector(3,4).len == 5.
    assert Vector.calculate_vector([0, 0, 0], [1,2,3]) == (1,2,3)
    assert Vector.from_points([0, 0, 0], [1,2,3]) == Vector(1,2,3)
