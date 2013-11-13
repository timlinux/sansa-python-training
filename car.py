# coding=utf-8
"""Simple car class."""


class Door():
    """A super door class."""
    count = 0

    def __init__(self):
        """Constructor."""
        self.state = 'open'
        Door.count += 1

    def close(self):
        """Close the door."""
        self.state = 'closed'

    def open(self):
        """Open the door."""
        self.state = 'open'


class Car(object):
    """A super car class."""

    def __init__(self):
        """Constructor."""
        self.doors = [Door(), Door(), Door(), Door()]
        self._secret_engine_hack = None

    def open_doors(self):
        """Open all doors."""
        for door in self.doors:
            door.open()

    def close_driver_door(self):
        """Close the driver door."""
        self.doors[0].close()

    def show_state(self):
        """Show the state of the car."""
        for door in self.doors:
            print door.state
