print('lib.py', __name__)


def foo():
    print('function from lib')


var1 = 10
var2 = [1, 2, 3, 4]


__all__ = [
    'var1',
    'var2',
]


if __name__ == '__main__':

    foo()

    print('in file lib.py')
