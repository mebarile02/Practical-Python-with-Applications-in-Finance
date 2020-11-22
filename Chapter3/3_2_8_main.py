'''
This module creates three generator expressions and uses itertools.product to get every combination
of values.
'''


import itertools


def main():

    genx1 = (x ** 2 for x in range(3))
    genx2 = (i for i in range(21) if i % 2 == 0)
    genx3 = (i for i in range(20) if i % 2 != 0)

    # This prints out all combination of values of the three generator expressions as a list of tuples.
    print(list(itertools.product(genx1, genx2, genx3)))


if __name__ == '__main__':
    main()