'''
This module tests functionality of methods created in exercise 2.1.4.
'''

from classFiles.loan import Loan
from classFiles.housebase import PrimaryHome


def main():

    ph = PrimaryHome(1000000)
    l = Loan(360, .07, 500000, ph)

    # This is a validation of the object-level method for monthlyPayment,
    # where we delegate to class-level method calcMonthlyPmt.
    print('Validation of monthlyPayment object-level method: ' + str(l.monthlyPayment()) + '\n')

    # This is a validation of the class-level method for calcMonthlyPmt.
    print('Validation of calcMonthlyPmt class-level method: '
          + str(Loan.calcMonthlyPmt(360, .07, 500000)) + '\n')

    # This is a validation of the object-level method for balance, where we
    # delegate to class-level method calcBalance.
    print('Validation of balance object-level method:')
    for i in range(5):
        print(l.balance(i))

    # This is a validation of the class-level method for calcBalance.
    print('\nValidation of calcBalance class-level method:')
    for i in range(5):
        print(Loan.calcBalance(360, .07, 500000, i))


if __name__ == '__main__':
    main()
