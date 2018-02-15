#!/usr/bin/env python3

__author__ = "Stephen J. Burke"
__email__ = "steburke71@hotmail.com"
__date__ = "2/15/18"
__license__ = "GPL"


even = list(range(0, 10, 2))
odd = list(range(1, 10, 2))

print(even)
print(odd)

print(list(range(0, 1000, 2)))

aList = list(range(10))
print(aList)

even = list(range(0, 10000000, 2))
odd = list(range(1, 10000000, 2))
both = even + odd
print(even + odd)
print(both)
print(sorted(both))

