#!/usr/bin/env python3

__author__ = "Stephen J. Burke"
__email__ = "steburke71@hotmail.com"
__date__ = "2/13/18"
__license__ = "GPL"

import random

high = 100000
answer = random.randint(1, high)
guess = 0

try:
    while guess != answer:
        guess = int(input('enter a number between 1 and {0}: '.format(high)))
        if guess > answer:
            print('too high')
        if guess < answer:
            print('too low')
        if not 1 <= guess <= high:
            print('only numbers between 1-{0} excepted'.format(high))
            print('exiting...')
            break
    else:
        print('you got it!')
except:
    print('only numbers between 1-{0} excepted'.format(high))
    print('exiting...')


