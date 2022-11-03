# Try/Except

# a = 10
# b = 30
#
# # c = a / b
#
# c = 0
#
# try:
#     c = a / 0
# except:
#     print('Exception')
#
# print('--->', c)

# a = 10
# b = 30
#
# c = 0
#
# try:
#     c = a / int(input('Enter the number: '))
# except Exception as e:
#     # print('Exception', e)
#     # print('Exception', type(e))
#     print('Exception', e.args)
#
# print('--->', c)


# a = 10
# b = 30
#
# c = 0
#
# try:
#     c = a / int(input('Enter the number: '))
# except ZeroDivisionError as e:
#     print('Invalid value "0" !')
# except ValueError as e:
#     print('Should be a number !')
#
# print('--->', c)

# a = 10
# b = 30
#
# c = 0
#
# try:
#     c = a / int(input('Enter the number: '))
#     'asdfgh'[1000]
# except ZeroDivisionError as e:
#     print('Invalid value "0" !')
# except ValueError as e:
#     print('Should be a number !')
# except Exception:
#     print('Exception')
#
# print('--->', c)


# a = 10
# b = 30
#
# c = 0
#
# try:
#     c = a / int(input('Enter the number: '))
# except Exception:
#     print('Exception')
# else:
#     print('No exception')
#
#
# print('--->', c)

#
# a = 10
# b = 30
#
# c = 0
#
# try:
#     c = a / int(input('Enter the number: '))
# except Exception:
#     print('Exception')
# else:
#     print('No exception')
# finally:
#     print('Exception or No exception')
#
# print('--->', c)


# Mutable objects issue


# lst1 = [1, 2, 3, 4]
#
# lst2 = lst1
#
# print(lst1)
# print(lst2)
#
# lst2.append('5')
#
# print(lst1)
# print(lst2)


# a = 10
#
# print(id(a))
#
# a += 1
#
# print(id(a))


# lst1 = [1, 2, 3, 4]
#
# # lst2 = lst1
# lst2 = lst1.copy()
#
# print(id(lst1))
# print(id(lst2))
#
#
# print(lst1)
# print(lst2)
#
# lst2.append('5')
#
# print(lst1)
# print(lst2)
#
# print(id(lst1))
# print(id(lst2))


# lst1 = [1, 2, 3, ['a', 'b', 'c']]
#
# lst2 = lst1.copy()
#
# print(id(lst1))
# print(id(lst2))
#
# lst2.append('5')
# lst2[3].append('d')
#
# print(lst1)
# print(lst2)
#
# print(id(lst1))
# print(id(lst2))


# import copy
# lst1 = [1, 2, 3, ['a', 'b', 'c']]
#
# lst2 = copy.deepcopy(lst1)
#
# lst2.append('5')
# lst2[3].append('d')
#
# print(id(lst1))
# print(id(lst2))
#
# print(lst1)
# print(lst2)


# Data types:
# Tuple

# # tuple  # immutable
#
# my_tuple = (1, 2.3, '3', 4, 5, [1, 3, 5])
#
# print(my_tuple)
# print(my_tuple[1])
# print(my_tuple[1: 4])
#
# print(bool(my_tuple))
# print(bool(tuple()))
#
# print('3' in my_tuple)
#
# print(my_tuple[-1])
#
# my_tuple[-1].append('12345')
#
# print(my_tuple)
#
# # my_tuple[0] = 3.4
#
# print(list(my_tuple))
#
#
# my_tuple = tuple('1234567890-')
#
# print(my_tuple)
# for i in my_tuple:
#     print(f'----> {i}')


# # Set, FrozenSet
#
# my_set = {1, 2, 3, 3, 4, 5, 6}
#
# print(my_set)
#
# my_set.add(False)
# my_set.add('True')
# my_set.add(1)
#
# print(my_set)
#
# for i in my_set:
#     print(i)
#
# print(10 in my_set)
#
# # my_set.remove(10)
# my_set.discard(10)
# print(my_set)
#
#
# fr = frozenset([1, 2, 3])
# print(fr)


# Dict

# my_dict = {
#     1: 12345,
#     2.3: 'sdfgh',
#     False: [1, 3, 4],
#     '123456': True,
#     None: None,
#     (1, 2, 3): (1, 2, 3),
#     frozenset('abc'): {1, 3, 4}
# }
#
# print(my_dict)
# print(my_dict[2.3].startswith('a'))
# print(my_dict[False])
#
# lst = ['login', 'pwd', 'address']
#
# my_dict = {
#     'login': 'qwer',
#     'pwd': 'sdfg',
#     'address': 'ERTH',
#     (1, 2): [1234]
# }
#
# print(my_dict['login'])
# # print(my_dict['abcde'])
# print(my_dict)
# my_dict['abcde'] = 1234567
#
# print(my_dict)
#
# my_dict['login'] = None
#
# print(my_dict)
#
# my_dict.pop('login')
#
# print(my_dict)
# print(my_dict[(1, 2)])
#
# print(1 in my_dict)  # keys
# print('pwd' in my_dict)  # keys
#
# # print(my_dict['login'])
# # my_dict['login'] = 'abc@abc.abc'
# print(my_dict.get('login', '123456'))  # None
# print(my_dict['login'] if 'login' in my_dict else '123456')  # None
#
# dict2 = {1: 2, 3: 4}
#
# my_dict.update(dict2)
#
# print(my_dict)
#
# my_dict |= {'a': 'b'}
#
# print(my_dict)


# my_dict = {
#     1: 12345,
#     2.3: 'sdfgh',
#     False: [1, 3, 4],
#     '123456': True,
#     None: None,
#     (1, 2, 3): (1, 2, 3),
#     frozenset('abc'): {1, 3, 4}
# }

# for i in my_dict:
#     print(i)

# for key in my_dict.keys():
#     print(key)
#     print(my_dict[key])

# for value in my_dict.values():
#     print(value)

# for item in my_dict.items():
#     print(item)

# for key, value in my_dict.items():
#     print(key, value)


my_dict = {
    1: 12345,
    2.3: 'sdfgh',
}

print(bool(my_dict))

print(bool({}))
print(my_dict)
my_dict[0] = 0
print(my_dict)

