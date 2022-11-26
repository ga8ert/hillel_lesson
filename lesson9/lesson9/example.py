#  decorator


# def foo(a, b=0, *args, **kwargs):
#
#     return a
#
#
# res = foo(1, 2)
# res = foo(3, 2)


# def foo(a, b=0, *args, **kwargs):
#
#     print('inside function', id(a))
#
#     return a
#
#
# # print(id(foo))
#
# var = 1000
#
# print('outside function', id(var))
#
# res = foo(var)
#
# print('outside function', id(res))


# def foo():
#
#     def bar():
#         print('i\'m function')
#
#     return bar
#
#
# res = foo()
#
# print(type(res))
#
# res()


# def function_to_decorate(*args, **kwargs):
#     print(f'I\'m a function with {args} and {kwargs}')
#     return 1
#
#
# def my_decorator(function):
#
#     def wrapper(*args, **kwargs):
#         print('Some code before')
#         result = function(*args, **kwargs)
#         print('Some code after')
#         return result
#
#     return wrapper
#
#
# # decorated_function = my_decorator(function_to_decorate)
# #
# # # function_to_decorate(1, 2, 3, a=10, b=20)
# #
# # decorated_function(1, 2, 3, a=10, b=20)
#
# function_to_decorate = my_decorator(function_to_decorate)
#
# function_to_decorate(1, 2, 3, a=10, b=20)

#
# def my_decorator(function):
#
#     def wrapper(*args, **kwargs):
#         print('Some code before')
#         result = function(*args, **kwargs)
#         print('Some code after')
#         return result
#
#     return wrapper
#
#
# @my_decorator  # function_to_decorate = my_decorator(function_to_decorate)
# def function_to_decorate(a, b):
#     print(f'I\'m a function with {a} and {b}')
#     return 1
#
#
# function_to_decorate(1, 2)
#

#
# def decorator_my(function):
#
#     def wrapper(*args, **kwargs):
#         print('Begin decorator_my')
#         result = function(*args, **kwargs)
#         print('End decorator_my')
#         return result
#
#     return wrapper
#
#
# def decorator_only_int_float(function):
#
#     def wrapper(*args, **kwargs):
#         print('Begin decorator_only_int_float')
#         for arg in args:
#             if not isinstance(arg, (int, float)):
#                 raise TypeError
#
#         for key, value in kwargs.items():
#             if not isinstance(value, (int, float)):
#                 raise TypeError
#
#         result = function(*args, **kwargs)
#         print('End decorator_only_int_float')
#
#         return result
#
#     return wrapper
#
#
# @decorator_my
# @decorator_only_int_float  # mult_a_b = decorator_my(decorator_only_int_float(mult_a_b))
# def mult_a_b(a, b):
#
#     print(f'I\'m a function with {a} and {b}')
#     return a * b
#
#
# # print(mult_a_b(a=1, b=3))

# def decorator_arg_type_check(*types):
#     print(f'decorator_arg_type_check with {types}')
#
#     def decorator(function):
#
#         def wrapper(*args, **kwargs):
#             print('Begin decorator_arg_type_check')
#             print(f'Begin {args} {kwargs}')
#             for arg in args:
#                 if type(arg) not in types:
#                     raise TypeError
#
#             for key, value in kwargs.items():
#                 if not isinstance(value, types):
#                     raise TypeError
#
#             result = function(*args, **kwargs)
#             print('End decorator_arg_type_check')
#
#             return result
#
#         return wrapper
#
#     return decorator
#
#
# # mult_a_b = decorator_arg_type_check(int, float)(mult_a_b)
# @decorator_arg_type_check(int, float)
# def mult_a_b(a, b):
#
#     print(f'I\'m a function with {a} and {b}')
#
#     return a * b
#
#
# mult_a_b(1, 2)


def decorator_save_data_to_file(file_name):
    print(f'decorator_save_data_to_file with {file_name}')

    def decorator(function):

        def wrapper(*args, **kwargs):
            print('Decorator begin')

            result = function(*args, **kwargs)  # all args and all kwargs

            with open(file_name, 'a') as file:
                file.write(f'Args: {args}, kwargs: {kwargs}, result {result}\n')

            print('End decorator')

            return result

        return wrapper

    return decorator


@decorator_save_data_to_file('function_foo_call_results.txt')
def foo(a, b):
    return a + b


@decorator_save_data_to_file('function_bar_call_results.txt')
def bar(a, b, c):
    return a + b * c


print(foo(1, 2, 4))
# print(foo(3, 2))
# print(foo(1, 5))
# print(foo(a=4, b=2))
# print(foo(a=6, b=2))
# print(bar(a=6, b=2, c=0))
# print(bar(a=6, b=2, c=3))
# print(bar(a=7, b=2, c=4))

# lst = range(3)
#
# # bar(1, 2, 3)
# bar(*lst)  # bar(1, 2, 3)
#
# dct = {
#     'a': 10,
#     'b': 13,
#     'c': 16,
#     'd': 55,
# }
#
# bar(a=10, b=13, c=16)
# bar(**dct)  # bar(a=10, b=13, c=16, d=55)


