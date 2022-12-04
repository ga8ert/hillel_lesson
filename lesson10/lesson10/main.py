from typing import Any, Union
import functools
import time
import copy


def is_string(value: Any, /, *, param: bool = False) -> bool:
    """
    checks if the given value is string
    """
    if param:
        return True

    is_value_string = type(value) == str
    return is_value_string


def multiply_to_two(value: Union[int, float, list]) -> Union[int, float, list]:

    result = value * 2
    return result


@functools.cache  # lru_cache
def foo(value: int):
    print('I work >>> ', value)
    time.sleep(2)
    return {value - 1}


f = {
    5: {4},
}


# print(foo(5))
# print(foo(5))
# print(vars())
# print(foo(50))
# print(foo(5))
# print(foo(5))


person = {
    'name': 'Alex',
    'age': 5
}


def foo2(data: dict = None):
    # data = data[:] list
    data = copy.copy(data)
    # data = copy.deepcopy(data)
    data['name'] = 'kljghdfihbifdh'
    return data


print(person)
print(foo2(person))
print(person)
