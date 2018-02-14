#!/usr/bin/env python3

__author__ = "Stephen J. Burke"
__email__ = "steburke71@hotmail.com"
__date__ = "2/13/18"
__license__ = "GPL"

compass = ['north', 'northwest', 'northeast', 'south', 'southwest', 'southeast', 'east', 'west']
move = ''

while move not in compass:
    if move == 'quit':
        print('You quit!')
        break
    x = str(compass)[1:-1]
    print('Options are: ' + x + ' or \'quit\' to exit')
    move = input('choose a compass direction: ')
else:
    print('you moved {0}'.format(move))
