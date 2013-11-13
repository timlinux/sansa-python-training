# coding=utf-8
"""Examples with tuples."""

f = (1, 2, 3)  # tuple
h = [1, 2, 3]  # list
i = {'a': 1, 'b': 2, 'c': 3}  # dic


for item in f:
    print item

for item in h:
    print item

for item, value in i.items():
    print item, value

h[1] = 5
#f[1] = 5


def get_things():
    """Demonstration of returning a tuple."""
    return 1, 2, 3

print 'Getting things'
a, b, c = get_things()
print a, b, c

foo = get_things()
print foo
print 'Printing things'
for item in foo:
    print item

nest = {'a': {'z': 2, 'x': 4},
        'b': {'z': 2, 'x': 4}}


print nest['a']['z']
for value in nest.itervalues():
    print value.values()

x = [value for value in range(1, 101)]

print x


def half(x):
    """Divide a number in half.

    :param x: Any number.
    :type x: int, float

    :returns: The number halved.
    :rtype: float
    """
    return float(x) / 2.0


y = map(half, x)


print y

