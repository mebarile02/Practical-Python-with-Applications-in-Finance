'''
This module tests LoanPool class to verify that it is an iterable.
'''

from classFiles.Loan.loan import Loan
from classFiles.Loan.loanpool import LoanPool
from classFiles.Assets.car import Lamborghini

def main():

    a1 = Lamborghini(100000, .05)
    a2 = Lamborghini(200000, .09)
    a3 = Lamborghini(150000, .10)

    l1 = Loan(60,.10, 75000, a1)
    l2 = Loan(72, .07, 125000, a2)
    l3 = Loan(48, .10, 130000, a3)

    lpool = LoanPool([l1, l2, l3])

    for loan in lpool:
        print('Term: ' + str(loan.term))

    for loan in lpool:
        print('Rate: ' + str(loan.rate))

    for loan in lpool:
        print('Face: ' + str(loan.face))

    for loan in lpool:
        print('Current value of asset: ' + str(loan.asset.currentVal(0)))

if __name__ == '__main__':
    main()