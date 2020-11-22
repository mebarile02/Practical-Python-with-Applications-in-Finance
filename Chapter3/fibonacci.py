'''
This module modifies the fibonacci function to be a generator function.
'''


def fibonacci():

    values = [0, 1]

    i = 0

    while i < 2:
        yield values[i]
        i += 1

    while True:
        values.append(values[i - 2] + values[i - 1])
        yield values[-1]
        i += 1












