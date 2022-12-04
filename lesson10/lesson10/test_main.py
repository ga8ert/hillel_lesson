from main import multiply_to_two
import pytest


def test_multiply_to_two():
    assert type(multiply_to_two(5)) == int, 'not int'


@pytest.mark.parametrize('value,expected', [(5, 10), ([1], [1, 1])])
def test_second(value, expected):
    assert multiply_to_two(value) == expected, 'not expected result'
