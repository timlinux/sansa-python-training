# coding=utf-8
"""Examples of class inheritance."""


class Athlete():
    """An athlete."""
    def __init__(self):
        """Constructor."""
        print 'New athlete is made'

    def run(self):
        """Run dude run!."""
        print 'Running man running'


class GrandParent():
    """Our grandparent class."""
    def __init__(self, foo):
        print 'Grandparent made'
        print 'Grandparent: %s' % foo

    def walk_with_cane(self):
        """Walk with a cane."""
        print 'Hobble hobble'


class Parent(GrandParent, Athlete):
    """Our parent class."""
    def __init__(self, foo):
        print 'Parent made: %s' % foo
        GrandParent.__init__(self, foo)
        Athlete.__init__(self)

if __name__ == '__main__':
    parent = Parent('Silly me')
    parent.walk_with_cane()
    parent.run()
