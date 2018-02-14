#!/usr/bin/env python3

__author__ = "Stephen J. Burke"
__email__ = "steburke71@hotmail.com"
__date__ = "2/13/18"
__license__ = "GPL"

import random

answer = random.randint(1, 10)
guess = ''

try:
    while guess != answer:
        guess = int(input('enter a number between 1 and 10: '))
        if not 1 <= guess <= 10:
            print('only numbers between 1-10 excepted')
            print('exiting...')
            break
    else:
        print('you got it!')
except:
    print('only numbers between 1-10 excepted')
    print('exiting...')


