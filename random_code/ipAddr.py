#!/usr/bin/env python3

__author__ = "Stephen J. Burke"
__email__ = "steburke71@hotmail.com"
__date__ = "2/13/18"
__license__ = "GPL"

seg = 1
segLen = 0
char = ''

ipAddr = input('enter an ip: ')


for char in ipAddr:
    if char == '.':
        print('segment {0} contains {1} characters'.format(seg, segLen))
        seg += 1
        segLen = 0
    else:
        segLen += 1
if char != '.':
    print('segment {0} contains {1} characters'.format(seg, segLen))



