# types

# int, float

# bool

# str
#
# my_str = 'qwertyu'
#
#
# my_str += '6234765'

# print(my_str)

# string formatting
#
# name = 'Artem'
# age = 39
#
# # Hello! My name is Artem, I'm 39 year old
#
# my_str = 'Hello! My name is ' + name + ', I\'m ' + str(age) + ' year old'
# print(my_str)
#
# my_str = 'Hello! My name is %s, I\'m %s year old' % (name, age)
# print(my_str)
#
# tpl = 'Hello! My name is {}, I\'m {} year old'
# my_str = tpl.format(name, age)
# print(my_str)
#
# tpl = 'Hello! My name is {name_var}, I\'m {age_var} year old'
# my_str = tpl.format(age_var=age, name_var=name)
# print(my_str)
#
#
# # f-string
# my_str = f'Hello! My name is {name}, I\'m {age} year old'
# print(my_str)
#
#
# print('abcd' in my_str)
# print('He' in my_str)
#
# print(ord('A'))
#
#
# # string methods
#
# my_str = 'Hello! My name is Artem, I\'m 39 year old'
#
#
# my_str = my_str.replace('am', '++')
#
# print(my_str)
#
#
# my_str = '__abcd 123___'
# print(my_str)
# my_str = my_str.strip('_')
#
# print(my_str)
#
# my_str = '__abcd 123___'
# print(my_str)
# my_str = my_str.lstrip('_')
#
# print(my_str)
#
# my_str = '__abcd 123___'
# print(my_str)
# my_str = my_str.rstrip('_')
#
# print(my_str)
#
# my_str = 'Hello! My name is Artem, I\'m 39 year old'
# my_str = my_str.upper()
# print(my_str)
#
# my_str = 'Hello! My name is Artem, I\'m 39 year old'
# my_str = my_str.lower()
# print(my_str)
#
# my_str = 'abcd abcd'
# my_str = my_str.title()
# print(my_str)
#
# my_str = 'abcd abdsfDDKJBHIBcd'
# my_str = my_str.capitalize()
# print(my_str)
#
# my_str = 'abcd abdsfDDKJBHIBabcd'
# res = my_str.count('ab')
# print(res)
#
# my_str = 'Abcd abdsfDDKJBHIBabcd'
# res = my_str.startswith('ab')
# print(res)
#
# my_str = 'Abcd abdsfDDKJBHIBabcd'
# res = my_str.endswith('abwcd')
# print(res)
#
# my_str = '0123456789'
# res = my_str.isdigit()
# print(res)
#
# my_str = 'asdfghjAkl'
# res = my_str.isalpha()
# print(res)
#
# my_str = 'asdfghjAkl 123'
# res = my_str.isalnum()
# print(res)

#
# my_str = 'abcdefghijkl'
# res = my_str.find('sde')
# print(res)
#
# res = my_str.index('de')
# print(res)
#
# res = my_str.find('de', 5, 8)
# print(res)
#
#
# # idx
# print(my_str[2])
#
# print(len('0123456789'))
#
# print('0123456789'[2])
# # print('0123456789'[20])
#
# print('0123456789'[-1])
# print('0123456789'[-2])
#
# # slices
# print('0123456789'[2:6])  # 2345
# print('0123456789'[2:])  # 2->
# print('0123456789'[:5])  # <-5
#
# idx = -2
# print('0123456789'[-4:])  # -4->
# print('0123456789'[-4:-2])
# print('0123456789'[idx:-6])
#
# print('0123456789'[1:8:2])
# print('0123456789'[8:1:-1])
#
# print('0123456789'[::-1])
# print('0123456789'[-3::-1])
#
# my_str = '0123456789'
# print(my_str[len(my_str) // 2:])
#
#
# condition = True
#
# if condition:
#     print('1 Inside IF block')
#     print('2 Inside IF block')
#     print('3 Inside IF block')
# else:
#     print('1 Inside ELSE block')
#     print('2 Inside ELSE block')
#     print('3 Inside ELSE block')
#
# print('Outside')


# a = 310
# b = 20
#
# if a > b:
#     print('a > b')
# else:
#     print('a <= b')


# a = 10
# b = 20
#
# if a > b:
#     print('a > b')
#
#
# print('outside')


# a = 0
# b = 0
#
# if a > b:
#     print('a > b')
# elif a == b:
#     print('a == b')
# elif a == 0:
#     print('a == 0')
#
# print('outside')


# a = 10
# b = 20
#
# if a > b:
#     print('a > b')
# elif a == b:
#     print('a == b')
# elif a == 0:
#     print('a == 0')
# else:
#     print('else')
#
# print('outside')


# a = 'abc'
# b = 'cba'
#
# if a == b:
#     print('a == b')
# elif a.isalpha():
#     print('isalpha')
# else:
#     print('else')
#
# print('outside')


# a = 'abc'
# a = 0
#
#
# if a:  # bool(a) ->
#     print('a is True')
# else:
#     print('else')
#
# print('outside')


# a = 0
#
#
# if a != 0:  # if a:
#     print('a is True')
# else:
#     print('else')
#
# print('outside')


# a = 0

# not

# my_bool = True
# print(not my_bool)


# if a == 0:  # if a:
#     print('a is True')
# else:
#     print('else')
#
# print('outside')
#
#
# if not a:
#     print('a is True')
# else:
#     print('else')
#
# print('outside')
