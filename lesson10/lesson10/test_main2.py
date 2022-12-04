from main import multiply_to_two
import pytest


def test_multiply_to_two():
    assert type(multiply_to_two(5)) == int, 'not int'


def test_second():
    assert multiply_to_two(5) == 10, 'not expected result'


def test_foo():
    with pytest.raises(TypeError):
        multiply_to_two({5})
