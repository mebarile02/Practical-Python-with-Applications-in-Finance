'''
This module creates three generator expressions, zips them, and prints out the result as a list.
'''


def main():

    genx1 = (x ** 2 for x in range(3))
    genx2 = (i for i in range(21) if i % 2 == 0)
    genx3 = (i for i in range(20) if i % 2 != 0)
    genex = zip(genx1, genx2, genx3)
    # When printing the zipped generators to a list, returns three tuples.  (0, 0, 1) corresponds to
    # first value of each generator expression, (1, 2, 3) to the second value of each generator expression,
    # and (4, 4, 5) to the third value of each generator.  I think that since genx1 is exhausted of values,
    # nothing more is displayed.

    print(list(genex))


if __name__ == '__main__':
    main()