# # functions
#
#
# def foo(arg1, arg2):
#
#     result = arg1 + arg2
#
#     return result
#
#
# # DRY
# # KISS
# # YAGNI
#
#
# def my_function(arg1, arg2, arg3):
#
#     result = (arg1 + arg2) / arg3
#
#     return result
#
#
# a = my_function(3, 5, 7)
#
# print(a)
#
# a = 157
# b = 22
# c = 33
#
# res = my_function(b, a, c)  # positional
# print(res)
#
# res = my_function(arg1=a, arg2=b, arg3=c)  # named
# print(res)
#
# res = my_function(arg2=b, arg1=a, arg3=c)  # named
# print(res)
#
#
# def my_function(arg1, arg2, arg3, arg4):
#
#     result = (arg1 + arg2) / arg3
#
#     return result
#
#
# res = my_function(10, 33, arg4='asdfg', arg3=b)  # combine
# print(res)
#
# res = my_function(10, 33, arg4='asdfg', arg3=b)  # combine
# print(res)
#
# var1 = 'asdfghjhgfdsdghjhfdsg'
#
# res = my_function(
#     arg1=10,
#     arg2=33,
#     arg4='asdfg',
#     arg3=b,
# )  # combine
# print(res)


# def my_function(arg1, arg2, arg3, arg4):
#
#     result = (arg1 + arg2) / arg3
#
#     return result
#
#
# res = my_function(10, 33, arg4='asdfg', arg3=1)


# def my_function():
#
#     return
#
#
# res = my_function()


# def my_function(arg1=1, arg2=1, arg3=1):
#
#     result = (arg1 + arg2) / arg3
#
#     return result
#
#
# res = my_function(arg1=10, arg2=33, arg3=3)
#
# print(res)
#
# res = my_function(arg1=10, arg2=33)
#
# print(res)
#
# res = my_function()
#
# print(res)


# def my_function(value, lst=[]):
#
#     lst.append(value)
#
#     return lst
#
# def my_function(value, lst=None):
#
#     if lst is None:
#         lst = []
#
#     lst.append(value)
#
#     return lst
#
#
# my_list = [1, 2, 3]
#
# print(my_list)
# my_list = my_function(5, my_list)
# print(my_list)
#
# my_list = my_function(5)
#
# print(my_list)
#
# my_list = my_function('1234')
# print(my_list)
#
# my_list = my_function(True)
# print(my_list)


# def my_function(value, lst=None):
#
#     if lst is None:
#         lst = []
#     lst.append(value)
#
#     return lst
#
#
# my_list = [1, 2, 3]
#
# my_list = my_function(5, my_list)
#
# print(my_list)


# def get_number():
#
#     while True:
#         try:
#             return int(input('Enter the number: '))
#         except Exception as e:
#             print('It\'s not a number')


# def number_validation(number, min_limit=0, max_limit=100):
#     if max_limit >= number > min_limit:
#         return number
#     raise ValueError
#
#
# def get_number(message='Enter the number: '):
#
#     while True:
#         try:
#             value = int(input(message))
#         except Exception as e:
#             print('It\'s not a number')
#         else:
#             break
#
#     return value
#
#
# number = get_number('Enter your age: ')
# number = number_validation(number)
#
#
# def number_validation(number, min_limit=0, max_limit=100):
#     if max_limit >= number > min_limit:
#         return number
#     raise TypeError
#
#
# def get_number(message='Enter the number: ', min_limit=0, max_limit=100):
#
#     while True:
#         try:
#             value = number_validation(int(input(message)), min_limit, max_limit)
#         except TypeError as e:
#             print('Invalid value')
#         except Exception as e:
#             print('It\'s not a number')
#         else:
#             break
#
#     return value
#
#
# number = get_number(
#     message='Enter your age: ',
#     min_limit=1,
#     max_limit=125,
# )


#

# lst = [1, 3, 4]


# def foo(*args):  # positional
#     print(type(args))
#     print(args)
#
#
# foo()
# foo(1, 2, 3)
# foo(1, "2, 3", 1, 3, 4, 4, 5, 6, 8, 9, 4, 3, 2, 1, 1, 23)
#
# lst = [1, "2, 3", 1, 3, 4, 4]
#
# foo(*lst)  # foo(1, "2, 3", 1, 3, 4, 4)
# foo(lst)  # foo(1, "2, 3", 1, 3, 4, 4)

# lst = [1, "2", 1, 3, 4, 4]
#
#
# def foo(a, b, c=0, *args):  # positional
#     print(type(args))
#     print(args)
#
#
# foo(1, 2, 3, 4, 5, 6, 7, 8, 9)
# foo(*lst)
# foo(1, *lst)


# def foo(a, b, c=0, **kwargs):  # named
#     print(type(kwargs))
#     print(kwargs)


# dct = {
#     'a': 10,
#     'b': 10,
#     'c': 10,
#     'd': 10,
#     'e': 10,
# }
#
#
# # foo(10, 20, c=30, d='', e=None)
# foo(**dct)  # foo(a=10, b=20, c=30, d=10, e=10)


# def foo(a, b, c=0, d=0, *args, **kwargs):
#     print(type(args))
#     print(args)
#     print(type(kwargs))
#     print(kwargs)
#
#
# lst = [1, "2", 1, 3, 4, 4]
# #
# # foo(*lst)
#
# dct = {
#     # 'a': 10,
#     # 'b': 10,
#     # 'c': 10,
#     # 'd': 10,
#     'e': 10,
#     'f': 10,
# }
# foo(*lst, **dct)

