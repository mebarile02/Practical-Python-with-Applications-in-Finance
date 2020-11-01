'''
This module tests some of the methods of the basic Loan class that are created in exercise
2.1.2.  This had to be modified from the original testing to account for changes made as
the exercises progressed.
'''

from classFiles.loan import Loan
from classFiles.asset import Asset

def main():

    a = Asset(600000, .04)
    l = Loan(360, .05, 500000, a)

    print('Testing monthlyPayment method: ' + str(l.monthlyPayment()))
    print('Testing totalPayments method: ' + str(l.totalPayments()))
    print('Testing totalInterest method: ' + str(l.totalInterest()))



if __name__ == '__main__':
    main()