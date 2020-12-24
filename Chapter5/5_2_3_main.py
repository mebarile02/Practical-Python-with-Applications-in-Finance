'''
The intention of this module was to test memoization of recursive loan functions, but I created these
using loops, so there were not really any noticeable benefits when comparing performance.  I may need to
redefine these recursive functions if they are not defined as intended in the homework.
'''

from classFiles.Loan.loan import Loan
from classFiles.Assets.car import Civic
import time

def main():
    a = Civic(100000)
    l = Loan('2000-01-01', '2020-12-31', .08, 200000, a )

    print(f'Recursive Interest: {l.interestDueR(200)}')
    print(f'Principal Due: {l.principalDueR(200)}')
    print(f'Recursive Balance: {l.balanceR(200)}')


if __name__ == '__main__':
    main()