# coding=utf-8
"""Implementation for telescope."""


class Telescope():
    """Representatio of a telescope."""
    def __init__(self):
        """Constructor."""
        self.track_result = False
        self.aliens_killed = 0

    def track(self):
        """Track a satellite."""
        self.track_result = True

    def fire(self):
        """Fire a beam at a ufo."""
        print 'Kablaaaam!'
        self.aliens_killed = 10
