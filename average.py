#!/bin/env python3
x = 1
y = 0
counter = 0
total = 0

try:
    while x > 0:
        x = int(input('pick a number:\t'))
        counter += 1
        total = x + y
        y = total
        if counter > 1 and x > 0:
            print(total / counter)
        elif x == 0:
            counter -= 1
except ValueError:
    pass

try:
    print('\n\ntotal average:\t' + str(total / counter))
    print("counter:\t" + str(counter))
except ZeroDivisionError:
    pass
