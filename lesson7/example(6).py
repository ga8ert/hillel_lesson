#

# def foo(a, b=0, *args, **kargs):
#     #
#     #
#     #
#     #
#     return 1
#
#
# res = foo(1, 2)
# res = foo(a=1, b=2)


# # annotation & docstring
#
# def get_number(message='Enter the number: '):
#     """
#     reStructured bla - bla
#     :param message: message for displaying to user
#     :type message: str|int
#     :return:
#     :rtype: int
#     """
#
#     while True:
#         try:
#             value = int(input(message))
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
# def get_number(message='Enter the number: '):
#     """
#     Args:
#         message (str|int):
#     Returns:
#         (int):
#     """
#
#     while True:
#         try:
#             value = int(input(message))
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
# # annotations
#
# def foo(a: str, b: int = 1) -> str:
#     """ """
#     return a * b
#
#
# res = foo(1, 'asdfg')


# namespaces

# global_value = 100
#
#
# def foo(global_data):
#
#     local_value = 200
#
#     print('local value inside function', local_value)
#     print('global value inside function', global_data)
#
#
# foo(global_value)


# global_value = 100
#
#
# def foo():
#
#     local_value = 200
#     local_value += 1
#     print('local value inside function', local_value)
#     global_value = 0
#     # global_value += 1
#     print('global value inside function', global_value)
#
#
#
# print(global_value)
#
# foo()
#
# print(global_value)


# global_value = [100]
#
#
# def foo(global_value):
#
#     local_value = 200
#     local_value += 1
#     print('local value inside function', local_value)
#
#     global_value.append(1)  # BAD IDEA!
#
#     print('global value inside function', global_value)
#
#     return global_value
#
#
# print(global_value)
#
# global_value = foo(global_value)
#
# print(global_value)


# global_value = 100
#
#
# def foo():
#
#     local_value = 200
#     local_value += 1
#     print('local value inside function', local_value)
#
#     global global_value
#
#     global_value += 1
#
#     print('global value inside function', global_value)
#
#
# print(global_value)
#
# foo()
#
# print(global_value)

# local_value = 1


# def foo():
#
#     local_value = 200
#
#     def bar():
#         # local_value = 10
#         nonlocal local_value
#         local_value += 1
#
#     bar()
#
#     print('local value inside function', local_value)
#
#
# foo()


# recursion

'''

a = !5

a = 5 * 4 * 3 * 2 * 1
!5  = 5 * !4
!4  = 4 * !3
!3  = 3 * !2
!2  = 2 * !1
!1  = 1

!n = n * (n-1) * (n-2) .... * 1

!5 = f(5)

5 * f(4)

4 * f(3)

'''
#
#
# def factorial_recursive(n):
#     print(f'factorial_recursive {n}')
#
#     if n <= 1:
#         return 1
#
#     return n * factorial_recursive(n-1)
#
#
# res = factorial_recursive(5)
#
# print(res)


'''
1 1 2 3 5 8 13 21 34 55 89

n[x] = n[x-1] + n[x-2]


'''

# counter = 0
#
#
# def fib_rec(n):
#     # O(n) = 2 ** n
#
#     global counter
#     counter += 1
#
#     if n == 1 or n == 2:
#         return 1
#
#     return fib_rec(n-1) + fib_rec(n-2)
#
#
# res = fib_rec(35)
#
# print(res)
# print('counter ', counter)


# def fib_plan(n):
#
#     fib1 = fib2 = 1
#
#     if n == 1 or n == 2:
#         return fib1
#
#     for i in range(n - 2):
#         fib1, fib2 = fib2, fib1 + fib2
#
#     return fib2


# res = fib_plan(4000)
#
# print(res)

#
# dct = {
#     'a': 1,
#     'b': 2,
#     'c': {
#         'a2': 1,
#         'b2': 1,
#         'c2': {
#             'a3': 1,
#             'b3': 1,
#             'c3': {
#                 'a2': 1,
#                 'b2': 1,
#                 'c2': {
#                     'a3': 1,
#                     'b3': 1,
#                 }
#             },
#         },
#     },
# }
#
# # for k, v in dct.items():
# #     print(k, v)
# #     if isinstance(v, dict):
# #         for k2, v2 in v.items():
# #             print(k2, v2)
#
#
# def get_key_value(data_dict):
#     for key, value in data_dict.items():
#         print(key, value)
#         if isinstance(value, dict):
#             return get_key_value(value)
#
#
# get_key_value(dct)


# def add(a, b):
#     return a + b


# get data

# processing data
# processing data

# response


# Rock Scissors Paper

# rules = {  # key - fig, value - > loser
#     'Rock': 'Scissors',
#     'Scissors': 'Paper',
#     'Paper': 'Rock',
# }

# get_player_figure
    # while
        # input -> rules
    # return figure


# from random import choice
# get_ai_figure
    # random -> rules
    # return figure


# define_winner
    # f1, f2, rules
    # return text message


# text_msg
    # (print(text message))


# game ()
    # get_player_figure
    # get_ai_figure
    # define_winner
    # text_msg














