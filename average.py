#!/bin/env python3
x = 1  # Start point (number is ignored, just needs to be more than 0)
counter = 0  # Used to calculate the average
total = 0  # Needs to be zero to start the adding of future values

print()

try:
    while x > 0:
        x = int(input(str(counter + 1) + ') Enter a number. (enter 0 or leave blank if done):\t'))
        counter += 1
        total = x + total
        if counter > 1 and x > 0:
            print('average so far: ' + str(total / counter) + '\n')
        elif x == 0:
            counter -= 1
except ValueError:
    pass

try:
    print('\n\ntotal average:\t' + str(total / counter))
    print("counter:\t" + str(counter))
except ZeroDivisionError:
    pass
