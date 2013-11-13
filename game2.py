# coding=utf-8
"""A simple guessing game."""
from random import random


class InvalidChoiceError(Exception):
    """An error instance for bad choices."""
    pass


class Game():
    """A Game Class."""
    def __init__(self):
        self.difficulty = 50

    def set_difficulty(self):
        """Set the difficulty level for the game.
        """
        self.difficulty = int(raw_input(
            'Enter the highest number allowed for the secret: '))

    @staticmethod
    def ask_to_replay():
        """See if the user wants to play again.
        """
        play_again = int(raw_input('Play again?: '))
        if play_again is not 'y':
            return False
        else:
            return True

    def play(self):
        """Play a guessing game."""
        print 'Playing the GAME!'
        self.set_difficulty()
        allowed_range = self.difficulty
        secret = int(random() * allowed_range)
        result = -1
        retry = True
        while retry:
            while result != secret:
                try:
                    result = int(raw_input(
                        'Enter your guess between 0 and %i: ' % allowed_range))
                except ValueError, ex:
                    error_type = ex.__class__.__name__
                    message = 'You entered invalid data - %s' % error_type
                    error = InvalidChoiceError()
                    error.message = message
                    raise error
                if result < secret:
                    print 'Too low, try again'
                elif result > secret:
                    print 'Too high, try again'
            print 'Perfect!'
            retry = self.ask_to_replay()
            result = -1
        print 'Thanks for playing!'


if __name__ == '__main__':
    game = Game()
    try:
        game.play()
    except InvalidChoiceError, e:
        print e.message
