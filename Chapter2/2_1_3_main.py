'''
This module tests functionality for methods created in section 2.1.3 of the homework.
Observe that this had to be slightly modified to account for changes as exercises
progressed.
'''

from classFiles.loan import Loan
from classFiles.timer import Timer
from classFiles.car import Civic


def main():

    civ = Civic(25000)
    l = Loan(60, .06, 20000, civ)
    t = Timer()

    # Interest Due, Principal Due and Balance functions are run for both formula
    # and recursive methods.  It is clear that the recursive method is significantly less
    # efficient, and this become more noticeable as the term length increases.

    print('Interest Due results: ')
    t.start()
    for i in range(1, l.term + 1):
        l.interestDue(i)
    t.end()
    t.start()
    for i in range(1, l.term + 1):
        l.interestDueR(i)
    t.end()

    print('\nPrincipal Due results: ')
    t.start()
    for i in range(1, l.term + 1):
        l.principalDue(i)
    t.end()
    t.start()
    for i in range(1, l.term + 1):
        l.principalDueR(i)
    t.end()

    print('\nBalance results: ')
    t.start()
    for i in range(l.term + 1):
        l.balance(i)
    t.end()
    t.start()
    for i in range(l.term + 1):
        l.balanceR(i)
    t.end()


if __name__ == '__main__':
    main()
