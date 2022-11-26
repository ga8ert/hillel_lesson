# import

# import - in top of the file

# import random
#
# print(random.randint(1, 10))

# import random as RANDOM
#
# print(RANDOM.randint(1, 10))


# # from random import randint, choice
#
# # from random import randint
# # from random import choice
#
# from random import (
#     randint,
#     choice,
# )
#
# print(randint(1, 10))
# print(choice((1, 10)))


# from random import randint as R, choice as C

# from random import randint as R
# from random import choice as C

# from random import (
#     randint as R,
#     choice as C,
# )
#
# print(R(1, 10))
# print(C((1, 10)))


# print(dir())
#
# from random import *  #
#
# print(dir())
#
# print(randint(1, 10))
# print(choice((1, 10)))


# import lib
#
# lib.foo()
# print(lib.var1)
# print(lib.var2)


# from lib import foo as FOO, var2 as V2
#
# FOO()
#
# print(V2)

#
# import lib  # python3 lib.py
#
# print('inside example.py')
#
# lib.foo()


# from lib import foo
#
# print('example.py', __name__)
#
# # print('inside example.py')
#
# # foo()
#
# a = 10

# from lib import *
#
# print(dir())


# from lib import foo
#
# foo()

#
# import e1
#
#
# from e1 import a
#
# print(e1.m)


# useful functions

# creation / transform
#
#
# res = int('12345')
# res = bool([])
#
# lst = list('12345')
#
#
# dct = dict()
#
# dct = dict([(1, 2), (3, 4)])
#
# print(dct)
#
# dct = dict(
#     a=10,
#     b=20,
# )
#
# print(dct)
#
#
# # math
#
# value = max(1, 20, 3, 4, 5, 5)
#
# print(value)
#
# value = max(('1', '20', '3', '4', '5', '5'))
#
# print(value)
#
#
# def foo(arg):
#     return arg[-1]
#
#
# value = max(('1234', '20', '3239', '4234543', '5', '5'), key=foo)
# print(value)
#
# value = max(('1234', '20', '3234', '4234543', '5', '5'), key=len)
# print(value)
#
#
# value = min(('1234', '20', '3234', '4234543', '5', '5'), key=len)
# print(value)
#
#
# val = sum([1, 2, 3, 4, 5])
# print(val)
#
# val = sum([])
# print(val)

# iteration

# r = range(1, 10, 2)
#
# for i in r:
#     print(i)

#
# enum = enumerate('LoremIpsum')
# for i in enum:
#     print(i)

#
# data = (1, 2, 3, 4, 5)
#
#
# def foo(arg):
#     return arg % 2
#
#
# for i in data:
#     i = foo(i)
#     print(i)
#
#
# mapped = map(foo, data)
#
#
# for i in mapped:  # i = foo(i)
#     print(i)
#
#
# for i in (foo(j) for j in data):
#     print(i)

#
# lst = {1, 2, 3, 4, 5, 6}
# my_string = '123456789'
#
# zipped = zip(lst, my_string, 'adf')
#
# for i in zipped:
#     print(i)


# rev = reversed('1234567')
#
# for i in rev:
#     print(i)

# def foo(arg):
#     return arg % 3
#
#
# res = sorted([1, 3, 5, 1, 3, 8, 2, 6], reverse=True, key=foo)
#
# print(res)

#
# def foo(arg):
#     return arg % 3
#
#
# res = list(filter(foo, [1, 3, 5, 1, 3, 8, 2, 6]))
#
# print(res)

#
# res = list(filter(lambda x: x % 3, [1, 3, 5, 1, 3, 8, 2, 6]))
#
# print(res)
#
# # lambda
#
# # lambda *args, **kwargs: actions *args, **args
#
#
# foo = lambda x: x % 3  # bad idea!
#
# res = list(filter(foo, [1, 3, 5, 1, 3, 8, 2, 6]))


# # foo = lambda x, y: (x % 3) * y
# # print(foo(2, 4))
#
# res = list(sorted(['1', '3', '5', '1', '3', '8', '2', '6'], key=lambda x: int(x)))  # bad idea
#
# # res = list(sorted(['1', '3', '5', '1', '3', '8', '2', '6'], key=int))
#
# res = list(sorted(['1', '3', '5', '1', '3', '8', '2', '6'], key=lambda x: int(x) % 2))
#
#
# print(res)


# file = open('example.txt', 'wt')
# file.write('Hello world')
# file.close()

# file = open('example.txt', 'rt')
# for line in file:
#     print(line)
# file.close()


with open('example.txt', 'rt') as file:
    for line in file:
        print(line)
