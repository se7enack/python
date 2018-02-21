#!/usr/bin/env python3

__author__ = "Stephen J. Burke"
__email__ = "steburke71@hotmail.com"
__date__ = "2/14/18"
__license__ = "GPL"

even = [0, 2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
print(numbers)
numbersSorted = sorted(numbers)
print(numbersSorted)

if numbersSorted == sorted(numbers):
    print("they are the same when sorted")
