import functools


@functools.cache
def exponent_mult(num1: int | float,
                  num2: int | float, 
                  exp: int | float) -> int | float:
    mult = num1 * num2
    result = mult ** exp
    return result
