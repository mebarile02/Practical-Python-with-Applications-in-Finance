'''
This module creates three generator expressions, chains them together using itertools, and prints
the result as a list.
'''

import itertools

def main():

    genx1 = (x ** 2 for x in range(3))
    genx2 = (i for i in range(21) if i % 2 == 0)
    genx3 = (i for i in range(20) if i % 2 != 0)

    allGen = itertools.chain(genx1, genx2, genx3)

    print(list(allGen))


if __name__ == '__main__':
    main()


