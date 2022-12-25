# 1 Доопрацюйте всі перевірки на типи даних (x, y в Point, begin, end в Line, etc) -
# зробіть перевірки за допомогою property або класса-дескриптора.
# 2 Доопрацюйте класс Triangle з попередньої домашки наступним чином:
# a) обʼєкти классу Triangle можна порівнювати між собою (==, !=, >, >=, <, <=) за площею. +
# b) перетворення обʼєкту классу Triangle на стрінг показує координати його вершин у форматі x1, y1 -- x2, y2 -- x3, y3
# print(str(triangle1))
# > (1,0 -- 5,9 -- 3,3)

from abc import ABC, abstractmethod


class Point:

    def __init__(self, x, y):
        if not (isinstance(x, int) or (isinstance(x, float))):
            raise TypeError
        if not (isinstance(y, int) or (isinstance(y, float))):
            raise TypeError
        self.x = x
        self.y = y

    def get_x(self):
        return self._x

    def set_x(self, x):
        if not (isinstance(x, int) or isinstance(x, float)):
            raise TypeError
        self._x = x

    x = property(get_x, set_x)

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        if not (isinstance(y, int) or isinstance(y, float)):
            raise TypeError
        self._y = y

    def __str__(self):
        return f'{self.x},{self.y}'


class Figure(ABC):

    @abstractmethod
    def __init__(self):
        pass

    def area(self):
        pass

    @abstractmethod
    def length(self):
        pass


class Line(Figure):

    def __init__(self, begin, end):
        if not isinstance(begin, Point):
            raise TypeError
        if not isinstance(end, Point):
            raise TypeError
        self.begin = begin
        self.end = end

    @property
    def begin(self):
        return self._begin

    @begin.setter
    def begin(self, begin):
        if not isinstance(begin, Point):
            raise TypeError
        self._begin = begin

    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, end):
        if not isinstance(end, Point):
            raise TypeError
        self._end = end

    def length(self):
        res = ((self.begin.x - self.end.x) ** 2 + (self.begin.y - self.end.y) ** 2) ** 0.5
        return res


class Triangle():

    def __init__(self, a, b, c):
        if not isinstance(a, Point):
            raise TypeError
        if not isinstance(b, Point):
            raise TypeError
        if not isinstance(c, Point):
            raise TypeError

        self.a = a
        self.b = b
        self.c = c

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, a):
        if not isinstance(a, Point):
            raise TypeError
        self._a = a

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, b):
        if not isinstance(b, Point):
            raise TypeError
        self._b = b

    @property
    def c(self):
        return self._c

    @c.setter
    def c(self, c):
        if not isinstance(c, Point):
            raise TypeError
        self._c = c

    @property
    def lineAB(self):
        return Line(self.a, self.b)

    @property
    def lineBC(self):
        return Line(self.b, self.c)

    @property
    def lineCA(self):
        return Line(self.c, self.a)

    @property
    def p(self):
        return (self.lineAB.length() + self.lineBC.length() + self.lineCA.length()) / 2


    @property
    def area(self):
        area_result = (self.p * (self.p - self.lineAB.length()) * (self.p - self.lineBC.length()) * (self.p - self.lineCA.length())) ** 0.5
        return area_result

    def __str__(self):
        return f'({self.a} -- {self.b} -- {self.c})'

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError
        return self.area == other.area

    def __ne__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError
        return self.area != other.area

    def __gt__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError
        return self.area > other.area

    def __ge__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError
        return self.area >= other.area

    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError
        return self.area < other.area

    def __le__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError
        return self.area <= other.area


p1 = Point(-3,-3)
p2 = Point(2,7)
p3 = Point(11,-5)
p4 = Point(-3, -2)
p5 = Point(2, 6)
p6 = Point(11, -4)


my_line = Line(p1, p2)
my_triangle = Triangle(p1, p2, p3)
my_triangle2 = Triangle(p4, p5, p6)

print(my_line.length())
print(my_triangle.area)
print(my_triangle2.area)
print(my_triangle < my_triangle2)
print(my_triangle > my_triangle2)
print(my_triangle >= my_triangle2)
print(my_triangle <= my_triangle2)
print(my_triangle == my_triangle2)
print(my_triangle != my_triangle2)

print(str(my_triangle))


