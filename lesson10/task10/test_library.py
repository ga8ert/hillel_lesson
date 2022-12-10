from library import exponent_mult
import pytest


def test1_type_exp_mult():
    assert type(exponent_mult(3, 2, exp=4)) == int, 'not int'


def test2_value_exp_mult():
    assert exponent_mult(-2, 2, exp=2) == 16, 'not expected result'


def test3_arg_type_exp_mult():
    with pytest.raises(TypeError):
        exponent_mult('2', 2, exp=2)
