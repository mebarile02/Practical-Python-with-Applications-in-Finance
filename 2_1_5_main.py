'''
This module validates methods created as part of exercise 2.1.5.
'''

from classFiles.loan import Loan
from classFiles.car import Lexus

def main():

    # This is for validation of the static methods monthlyRate and annualRate.
    print('Annual rate converted to monthly rate for simple interest: '
          + str(Loan.monthlyRate(.10)) + '\n')
    print('Monthly rate converted to annual rate for simple interest: '
          + str(Loan.annualRate(Loan.monthlyRate(.10))) + '\n')

    # This is for validation of methods that relied on rate where static method is now
    # being used.
    print('calcMonthlyPmt using static method for rate: ' +
          str(Loan.calcMonthlyPmt(360, .07, 500000)) + '\n')

    lex = Lexus(80000)
    l = Loan(360, .07, 500000, lex)

    print('interestDue using static method for rate: ' + str(l.interestDue(10)) + '\n')
    print('interestDueR using static method for rate: ' + str(l.interestDueR(10)) + '\n')
    print('principalDueR using static method for rate: ' + str(l.principalDueR(10)) + '\n')
    print('calcBalance using static method for rate: ' + str(Loan.calcBalance(360, .07, 500000, 200)) + '\n')
    print('balance using static method for rate: ' + str(l.balanceR(200)))


if __name__ == '__main__':
    main()