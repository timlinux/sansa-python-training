# coding=utf-8
"""A module illustrating the use of imports."""

import hello_function
from hello_function import hello_world, blow_up_world


def goodbye():
    """A simple goodbye function."""
    print 'Goodbye'

if __name__ == '__main__':
    # Call a function via the module
    hello_function.hello_world()
    # Call a function directly
    hello_world()
    blow_up_world()
    goodbye()
