"""
Na (1 pkt.):
- Zaimplementuj klasy: Rectangle, Square, Circle dziedziczące z klasy Figure
oraz definiujące jej metody:
    - Rectangle powinien mieć dwa atrybuty odpowiadające bokom (a i b)
    - Klasa Square powinna dziedziczyć z Rectangle.
    - Circle ma posiadać tylko atrybut r (radius).
- Przekształć metody area i perimeter we własności (properties).
---------
Na (2 pkt.):
- Zwiąż ze sobą boki a i b klasy Square (tzn. modyfikacja boku a lub boku b
powinna ustawiać tę samą wartość dla drugiego atrybutu).
- Zaimplementuj metody statyczne pozwalające na obliczenie
pola (get_area) i obwodu (get_perimeter) figury
na podstawie podanych parametrów.
- Zaimplementuj classmethod "name" zwracającą nazwę klasy.
---------
Na (3 pkt.):
- Zaimplementuj klasę Diamond (romb) dziedziczącą z Figure,
po której będzie dziedziczyć Square,
tzn. Square dziediczy i z Diamond i Rectangle.
- Klasa wprowadza atrybuty przekątnych (e i f) oraz metody:
-- are_diagonals_equal: sprawdź równość przekątnych,
-- to_square: po sprawdzeniu równości przekątnych zwróci instancję
klasy Square o takich przekątnych lub None (jeżeli przekątne nie są równe).
- Zwiąż ze sobą atrybuty a, b, e i f w klasie Square.
"""

from math import sqrt, pi

class Figure:

    def area(self):
        raise NotImplementedError

    def perimeter(self):
        raise NotImplementedError

    def name(self):
        raise NotImplementedError

    def __str__(self):
        return (
            f'{self.name}: area={self.area:.3f}, '
            f'perimeter={self.perimeter:.3f}'
        )

    
class Circle(Figure):
   
    def __init__(self, r):
        super().__init__()
        self._r = r

    @property
    def area(self):
        return pi * self._r ** 2

    @property
    def perimeter(self):
        return 2 * pi * self._r

    @property
    def name(self):
        return "Circle"

    @staticmethod
    def get_area(self, r):
        return pi * r **2

    @staticmethod
    def get_perimeter(self, r):
        return 2 * pi * r


class Rectangle(Figure):
   
    def __init__(self, a, b, **kwargs):
        super().__init__(**kwargs)
        self._a = a
        self._b = b
    
    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

    @a.setter
    def a(self, a):
        self._a = a
    
    @b.setter
    def b(self, b):
        self._a = b
    
    @property
    def area(self):
        return self.a * self.b

    @property
    def perimeter(self):
        return 2 * (self.a  + self.b)

    @property
    def name(self):
        return "Rectangle"

    @staticmethod
    def get_area(a, b):
        return a * b

    @staticmethod
    def get_perimeter(a, b):
        return 2 * (a + b)


class Diamond(Figure):

    def __init__(self, e, f, **kwargs):
        super().__init__(**kwargs)
        self._e = e
        self._f = f

    @property
    def e(self):
        return self._e
    
    @property
    def f(self):
        return self._f

    @e.setter
    def e(self, e):
        self._e = e

    @f.setter
    def f(self, f):
        self._f = f

    @property
    def area(self):
        return 0.5 * self.e * self.f

    @property
    def perimeter(self):
        return 4 * sqrt((0.5 * self.e) ** 2 + (0.5 * self.f) ** 2)

    @property
    def name(self):
        return "Diamond"

    @staticmethod
    def get_area(e, f):
        return 0.5 * e * f

    @staticmethod
    def get_perimeter(e, f):
        return 4 * sqrt((0.5 * e) ** 2 + (0.5 * f) ** 2)

    def are_diagonals_equal(self):
        return self.e == self.f

    def to_square(self):
        return Square(sqrt(self.e / 2)) if self.are_diagonals_equal else None
    

class Square(Rectangle, Diamond):
    
    def __init__(self, a):
        super(Square, self).__init__(a = a, b = a, e = sqrt(2 * a ** 2), f = sqrt(2 * a ** 2))
    
    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

    @property
    def e(self):
        return self._e
    
    @property
    def f(self):
        return self._f

    @a.setter
    def a(self, a):
        self._a = a
        self._b = a
        self._e = sqrt(2 * a ** 2)
        self._f = sqrt(2 * a ** 2)

    @b.setter
    def b(self, b):
        self._a = b
        self._b = b
        self._e = sqrt(2 * b ** 2)
        self._f = sqrt(2 * b ** 2)

    @e.setter
    def e(self, e):
        self._e = e
        self._f = e
        self._a = 0.5 * e ** 2
        self._b = 0.5 * e ** 2

    @f.setter
    def f(self, f):
        self._e = f
        self._f = f
        self._a = 0.5 * f ** 2
        self._b = 0.5 * f ** 2

    @property
    def name(self):
        return "Square"

    @staticmethod
    def get_area(a):
        return a * a

    @staticmethod
    def get_perimeter(a):
        return 4 * a


if __name__ == '__main__':
    kolo1 = Circle(1)
    assert str(kolo1) == 'Circle: area=3.142, perimeter=6.283'

    rec_1 = Rectangle(2, 4)
    assert str(rec_1) == 'Rectangle: area=8.000, perimeter=12.000'
    
    # print("Square")
    sqr_1 = Square(4)
    assert str(sqr_1) == 'Square: area=16.000, perimeter=16.000'

    diam_1 = Diamond(6, 8)
    assert str(diam_1) == 'Diamond: area=24.000, perimeter=20.000'

    diam_2 = Diamond(1, 1)
    assert str(diam_2) == 'Diamond: area=0.500, perimeter=2.828'

    sqr_3 = diam_2.to_square()
    assert str(sqr_3) == 'Square: area=0.500, perimeter=2.828'