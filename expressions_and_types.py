# coding=utf-8
"""Using expressions and types in python."""


def add(a, b):
    """Add two numbers.

    :param a: First number.
    :type a: float, int

    :param b: First number.
    :type b: float, int

    :returns: The sum of a and b.
    :rtype: float, int
    """
    return a + b


def calculate():
    """Do some calcs."""
    x = 5
    y = 5.5
    print add(x, y)
    z = x * 5 / 2 + y
    print type(z)
    z = 5
    print type(z)


def function_as_object(function):
    """Demo of function as object.
    :param function: A function handle.
    :type function: Any function.
    """
    function()


if __name__ == '__main__':
    c = calculate
    function_as_object(c)
