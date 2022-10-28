"""

Ternary operator

Data types:
    list

Loop:
    While
    For


3 questions (optional):
    - what is the result of this course for me
    - how I plane to use this result
    - what I am ready to sacrifice for the result

"""


# condition = True
#
# KISS
# if condition:
#     variable = 100
# else:
#     variable = 500
#
# # Ternary operator
# condition1 = True
# condition2 = True
#
# variable = 100 if condition else 500
#
# variable = 100 if condition else ('abc' if condition2 else '123')
#
# option1 = 100
# option2 = 'abc' if condition2 else '123'
#
# variable = option1 if condition else option2

# list

# my_lst = [1, '2', True, 4.4, None]
#
# print(type(my_lst))
#
# a = 10
# b = 20
# c = 'wert'
#
# my_lst = [a, b, c, a, 2, a]
#
# print(my_lst)
#
# my_lst.append(100)
#
# print(my_lst)
#
# my_lst2 = my_lst + [1, 3, 4]
#
# print(my_lst2)
#
# my_lst2 *= 2
#
# print(my_lst2)
#
# my_lst2 += 1
#
# print(my_lst2)
#
# my_str = '1234567890'
#
# print(my_str[0])
# print(type(my_str[0]))
#
# my_lst = [1, '2', True, 4.4, None, 2, 3, '123']
#
# print(my_lst[0])
# print(type(my_lst[0]))
# print(type(my_lst[1]))
# print(my_lst[1].isalpha())
#
# print(my_lst[4])
# print(my_lst[-2])
# print(my_lst[1:4])
# print(type(my_lst[1:4]))
#
# print(my_lst)
# my_lst.append(100)
# print(my_lst)
#
# my_str = '1234567890'
#
# # print(my_str[0])
# # my_str[0] = 'w'

#
# my_lst = [1, '2', True, 4.4, None, 2, 3, '123']
# print(my_lst)
#
# my_lst[2] = 'asdfghk'
#
#
# # my_lst[20] = 'asdfghk'
#
# print(my_lst)
#
# my_lst.insert(3, False)
#
# print(my_lst)
#
# print(my_lst.pop(3), '<-----')
#
# print(my_lst)
#
# my_lst.remove('2')
#
# print(my_lst)
#
# # my_lst.remove('2')
#
# print(my_lst.count(4.4))
#
# print(my_lst.index(4.4))
#
# print('123' in my_lst)
#
#
# my_lst = [1, '2', True, 4.4, None, 2, 3, '123', [1, [1, 2, 3], 3]]
#
# print(my_lst[-1][1])
#
# my_lst[-1][1].append(100)
#
# print(my_lst)

# my_lst1 = [0, 2, 3]
# my_lst2 = [1, 2.0, 3]
#
# print(my_lst1 >= my_lst2)
#
# my_lst = [1, '2', True, 4.4, None, 2, 3, '123', [1, [1, 2, 3], 3]]
#
# print(str(my_lst))
# print(list('12345678'))
#
#
# my_str = 'abc*abc*ndn*kwe*wefrvl'
#
# res = my_str.split('*')
# print(res)
#
# my_str = 'abc abc ndnkwe wefrvl'
#
# res = my_str.split(' ')
# print(res)
#
# res = my_str.split()
# print(res)
#
# my_lst = []
#
# print(bool(my_lst))


# loop


# counter = 0
#
# while counter < 10:
#     print('inside while loop')
#     print(f'counter is {counter}')
#     counter += 1
#
#
# print('outside loop ')

# counter = 0
#
# while counter < 10:
#     print('inside while loop')
#     print(f'counter is {counter}')
#     if counter % 2 == 0:
#         print('counter % 2 == 0')
#     else:
#         print('counter % 2 != 0')
#
#     counter += 1
#
# print('outside loop ')

#
# counter = 0
#
# while True:
#     print('inside while loop')
#     print(f'counter is {counter}')
#     counter += 1
#
#     if counter > 10:
#         print('BREAK!')
#
#         break
#
# print('outside loop ')



# counter = 0
#
#
# while True:
#     counter += 1
#
#     if counter % 3 == 0:
#         print('inside while loop')
#         print(f'counter is {counter}')
#         continue
#
#     print('inside loop')
#     if counter > 10:
#         print('BREAK!')
#
#         break
#
# print('outside loop ')


# counter = 0
#
#
# while True:
#     counter += 1
#     if counter == 5:
#         inner_counter = 0
#         while True:
#             # print('inside inner loop')
#             inner_counter += 1
#             if inner_counter % 2 == 0:
#                 continue
#             print('inside inner loop', inner_counter)
#             if inner_counter > 3:
#                 break
#     print('inside loop', counter)
#     if counter > 10:
#         print('BREAK!')
#         break
#
# print('outside loop ')


# KISS
# DRY
# YAGNI

#
# my_lst = [1, '2', True, 4.4, None, 2, 3, '123', [1, [1, 2, 3], 3]]
#
# idx = 0
#
# limit = len(my_lst) - 1
#
# while True:
#     i = my_lst[idx]
#     print('----->', my_lst[idx])
#     print('----->', i)
#     idx += 1
#     if idx > limit:
#         break


# loop FOR

# iterable - str, list

# my_lst = [1, '2', True, 4.4, None, 2, 3, '123', [1, [1, 2, 3], 3]]
#
# print(my_lst[::3])
#
# for elem in my_lst:
#     print('----->', elem)
#
#
# students_names_list = ['Bill', 'Bob', 'Tom']
#
# for name in students_names_list:
#     print('----->', name)
#
# for char in 'students_names_list':
#     print('----->', char)


# students_names_list = ['Bill', 'Bob', 'Tom', 'Joe']
#
# for name in students_names_list:
#     if name.startswith('B'):
#         print('----->', name)
#
#


# students_names_list = ['Bill', 'Bob', 'Tom', 'Joe']
#
# for name in students_names_list:
#
#     if name.startswith('T'):
#         break
#
#     print('----->', name)


# numbers = [1, 2, 3, 4, 5, 1, 2, 4, 5, 6]
#
# for number in numbers:
#
#     if number % 2 == 0:
#         continue
#
#     print('----->', number)
#
#
# numbers = [1, 2, 3, 4, 5, 1, 2, 4, 5, 6]
#
# lst_copy = numbers.copy()
# lst_copy = numbers[:]
#
# for number in lst_copy:
#
#     print('----->', number)
#     numbers.append(number)
