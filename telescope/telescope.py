# coding=utf-8
"""Implementation for telescope."""


class Telescope():
    """Representation of a telescope."""
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

    def friendly_message(self):
        """Send a friendly message to a ufo."""
        print 'Greetings alien, take me to your leader!'
        self.friendly_message = 'Greetings alien, take me to your leader!'
