#     Доопрацюйте класс Point так, щоб в атрибути x та y обʼєктів цього класу можна було записати тільки обʼєкти класу int або float
#     Доопрацюйте класс Line так, щоб в атрибути begin та end обʼєктів цього класу можна було записати тільки обʼєкти класу Point
#     Створіть класс Triangle (трикутник), який задається трьома точками (обʼєкти классу Point).
#     Реалізуйте перевірку даних, аналогічно до класу Line.
#     Визначет метод, що містить площу трикутника. Для обчислень можна використати формулу Герона (https://en.wikipedia.org/wiki/Heron%27s_formula)
from abc import ABC, abstractmethod


class Point:
    x = None
    y = None

    def __init__(self, x, y):
        if not (isinstance(x, int) or (isinstance(x, float))):
            raise Exception
        if not (isinstance(y, int) or (isinstance(y, float))):
            raise Exception
        self.x = x
        self.y = y


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
    begin = None
    end = None

    def __init__(self, begin, end):
        if not isinstance(begin, Point):
            raise Exception
        if not isinstance(end, Point):
            raise Exception
        self.begin = begin
        self.end = end

    def length(self):
        res = ((self.begin.x - self.end.x) ** 2 + (self.begin.y - self.end.y) ** 2) ** 0.5
        return res


class Triangle():
    a = None
    b = None
    c = None
    p = None
    lineA = None
    lineB = None
    lineC = None

    def __init__(self, a, b, c):
        if not isinstance(a, Point):
            raise Exception
        if not isinstance(b, Point):
            raise Exception
        if not isinstance(c, Point):
            raise Exception

        self.a = a
        self.b = b
        self.c = c
        self.lineAB = Line(a, b)
        self.lineBC = Line(b, c)
        self.lineCA = Line(c, a)
        self.p = (self.lineAB.length() + self.lineBC.length() + self.lineCA.length()) / 2

    def area(self):
        area_result = (self.p * (self.p - self.lineAB.length()) * (self.p - self.lineBC.length()) * (self.p - self.lineCA.length())) ** 0.5
        return area_result


p1 = Point(-3,-3)
p2 = Point(2,7)
p3 = Point(11,-5)

my_line = Line(p1, p2)
my_triangle = Triangle(p1, p2, p3)

print(my_line.length())
print(my_triangle.area())

