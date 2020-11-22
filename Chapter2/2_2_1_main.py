'''
This module tests functionality for exercise 2.2.1. Again, this needed to be modified
slightly after changes to the Loan base class.
'''

from classFiles.fixedrateloan import FixedRateLoan
from classFiles.variablerateloan import VariableRateLoan
from classFiles.housebase import PrimaryHome, VacationHome


def main():

    # Here, I test the derived FixedRateLoan and VariableRateLoan classes.

    ph = PrimaryHome(700000)
    vh = VacationHome(1000000)
    frl1 = FixedRateLoan(360, .08, 500000, ph)
    frl2 = FixedRateLoan(300, .06, 400000, vh)
    print('Testing loan ID functionality: ' + str(frl1.getId()))
    print('Testing loan ID functionality: ' + str(frl2.getId()))

    vrl1 = VariableRateLoan(5, {1: .10, 2: .08, 3: .06, 4: .04, 5: .09}, 100000, ph)

    print('Returns face value of loan: ' + str(vrl1.face))
    print('Tests the rate function to retrieve rate for a given period '
          'in a Variable Rate Loan: ' + str(vrl1.rate(4)))
    print('Tests toString for FRL: ' + str(frl1.toString()))
    print('Tests toString for VRL: ' + str(vrl1.toString()))


if __name__ == '__main__':
    main()
