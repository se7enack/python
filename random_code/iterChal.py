#!/usr/bin/env python3

__author__ = "Stephen J. Burke"
__email__ = "steburke71@hotmail.com"
__date__ = "2/15/18"
__license__ = "GPL"

aList = ['Stephen', 'Michelle', 'Nathan', 'Logan', 'Bryson']
iter1 = iter(aList)
n = len(aList)

for x in range(0, n):
    print(next(iter1))
