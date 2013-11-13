# coding=utf-8
"""A simple game."""
from random import random

secret = 0
while secret is 0:
    secret = int(random() * 10)
print secret

answer = -1

while answer != secret:
    if answer != -1:
        print 'Sorry try another guess'
    answer = int(raw_input('Guess my number! '))
    if answer < secret:
        print 'Your guess was too low!'
    elif answer > secret:
        print 'Your guess was too high!'

print 'Well done it is %s' % secret

