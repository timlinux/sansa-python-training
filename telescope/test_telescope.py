# coding=utf-8
"""Unit tests for our telescope class."""

import unittest
from telescope import Telescope


class TestTelescope(unittest.TestCase):
    """Telescope tests."""
    #noinspection PyPep8Naming
    def setUp(self):
        """Runs runs before each test."""
        self.telescope = Telescope()

    #noinspection PyPep8Naming
    def tearDown(self):
        """Runs after each test."""
        self.telescope = None

    def test_track(self):
        """Test we can track a satellite."""
        self.telescope.track()
        self.assertTrue(self.telescope.track_result)

    def test_laser_beam_ufo(self):
        """Test firing a beam works."""
        self.telescope.fire()
        self.assertEqual(10, self.telescope.aliens_killed)

if __name__ == '__main__':
    unittest.main()
