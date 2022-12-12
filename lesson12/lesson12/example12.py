# OOP

# main principles

# abstraction
# encapsulation
# inheritance
# polymorphism

# __magic_methods__


# class A:
#     a = 10
#     _a = 10
#     __a = 10
#
#     def foo(self):
#         return self.a
#
#     def __init__(self, new_a):
#         self.a = new_a
#
#
# obj_a = A(50)
#
# print(obj_a.a)
# print(obj_a.foo())
#
# obj_a.a = 30
#
# print(A.mro())

#
# class A:
#     a = 10
#     _instance = None
#
#     def __new__(cls, *args, **kwargs):
#         """"""
#         print(f'inside __new__ {args}, {kwargs}')
#         if cls._instance is None:
#             cls._instance = object.__new__(cls)
#         print(f'instance {cls._instance}')
#
#         return cls._instance
#
#     def __init__(self, new_a):
#         print(f'inside __init__ {new_a}')
#         self.a = new_a
#
#
# obj_a = A(50)
#
# print(id(obj_a))
#
# obj_a2 = A(50)
#
# print(id(obj_a2))

#
# class A:
#     a = 10
#
#     def __init__(self, new_a):
#         print(f'inside __init__ {new_a}')
#         self.a = new_a
#
#     # def __repr__(self):
#     #
#     #     return f'Object of class {self.__class__.__name__} with data {self.a}'
#
#     def __str__(self):
#         return f'STR Object of class {self.__class__.__name__} with data {self.a}'
#
#     def __bool__(self):
#         print('inside bool')
#         return False
#
#     def __int__(self):
#         return self.a
#
#
# obj_a2 = A(50)
#
# print(obj_a2)
# print(str(obj_a2))
# print(bool(obj_a2))
# print(int(obj_a2))
#
# if obj_a2:  # bool(obj_a2)
#     print('--->')


# class A:
#     a = 10
#
#     def __init__(self, val):
#         self.a = val
#
#     def __eq__(self, other):  # ==
#         if not isinstance(other, self.__class__):
#             raise TypeError
#         return self.a == other.a
#
#     # def __ne__(self, other):  # !=
#     #     return True
#     #
#     # def __gt__(self, other):  # >
#     #     return True
#     #
#     # def __ge__(self, other):  # >=
#     #     return True
#     #
#     # def __lt__(self, other):  # <
#     #     return True
#     #
#     # def __le__(self, other):  # <=
#     #     return True
#
#
# a = A(10)
# b = A(10)
#
# print(a != 1)
# # print(a > b)
#
# # print(a < b)
# # print(a >= b)
# # print(a <= b)
# # print(a == b)
# # print(a != b)


# class A:
#     a = 10
#
#     def __init__(self, val):
#         self.a = val
#
#     def __add__(self, other):
#         # return self.a + other.a
#         return self.__class__(self.a + other.a)
#
#
# print(1 + 3)
#
#
# a = A(10)
# b = A(10)
#
# c = a + b
# print(c)
# print(c.a)


# class A:
#     a = 10
#
#     def __init__(self, val):
#         # self.a = val
#         pass
#
#     def __getitem__(self, item):
#         print(f'__getitem__ ---> {item}')
#         return self.__dict__.get(item, self.__class__.__dict__.get(item, None))
#
#     def __setitem__(self, item, value):
#         self.__dict__[item] = value
#
#
# a = A(50)
#
# print(a['someattr'])
# print(a['a'])
#
# a['someattr'] = 150
# print(a['someattr'])


# class A:
#     a = 10
#
#     def __init__(self, val):
#         self.a = val
#
#     def __getattribute__(self, item):
#         print('__getattribute__', item)
#         return super().__getattribute__(item)
#
#     def __getattr__(self, item):
#         print('__getattr__', item)
#
#         try:
#             return self.__dict__.get(item) or self.__class__.__dict__.get(item)
#         except:
#             return None
#
#     def __setattr__(self, key, value):
#         print('__setattr__', key, value)
#
#         self.__dict__[key] = value
#
# obj_a = A(50)
# print(obj_a.b)
# obj_a.b = 1234
#
#
# class A:
#     pass
#
#
# class B(A):
#     pass
#
#
# class TimeMixin:
#     creation_time = None
#     deletion_time = None
#
#
# class D(TimeMixin, B):
#     def foo(self):
#
#         super().foo()
#
#
# class User(TimeMixin):
#     pass
#
#
# print(D.mro())

# association

# - aggregation  # object exists outside
# - composition  # object creates inside

#
# class Engine:
#     fuel_type = None
#     value = None
#
#     def __init__(self, fuel_type, value):
#         self.fuel_type = fuel_type
#         self.value = value
#
#     def start(self):
#         print('Engine started')
#
#
# class Car:
#     engine = None
#
#     def __init__(self, engine):  # aggregation
#         self.engine = engine
#         self.engine.start()
#
#
# engine1 = Engine('diesel', 2.7)
#
# car1 = Car(engine=engine1)
#
#
# class Car:
#     engine = None
#
#     def __init__(self, fuel_type, value):  # composition
#         self.engine = Engine(fuel_type, value)
#
#
# car2 = Car('diesel', 2.7)

from abc import ABC, abstractmethod


class Point:
    x = None
    y = None

    def __init__(self, x, y):
        # check here numbers
        self.x = x
        self.y = y


# class Figure:
#
#     def area(self):
#         return self._area()
#
#     def length(self):
#         return self._length()
#
#     def _area(self):
#         raise NotImplementedError
#
#     def _length(self):
#         raise NotImplementedError


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
        # check here Point
        self.begin = begin
        self.end = end

    def length(self):
        res = ((self.begin.x - self.end.x)**2 + (self.begin.y - self.end.y)**2)**0.5
        return res

    # area = length


p1 = Point(0, 0)
p2 = Point(3, 4)

my_line = Line(p1, p2)

print(my_line.length())
print(my_line.area())

