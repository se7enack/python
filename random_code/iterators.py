#!/usr/bin/env python3

__author__ = "Stephen J. Burke"
__email__ = "steburke71@hotmail.com"
__date__ = "2/14/18"
__license__ = "GPL"

numbers = "0123456789"

iter1 = iter(numbers)


#print(iter1)
print(next(iter1))
print(next(iter1))
next(iter1)
print(next(iter1))

# both of these are the same:
for char in numbers:
    print(char)
for char in iter(numbers):
    print(char)