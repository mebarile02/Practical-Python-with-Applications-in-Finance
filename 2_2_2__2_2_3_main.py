'''
This module tests functionality from modifications made in exercises 2.2-2.3, specifically
PMI, monthlyPayment and principalDue.
'''

from classFiles.mortgagemixin import VariableMortgage, FixedMortgage
from classFiles.loan import Loan
from classFiles.housebase import VacationHome


def main():

    vh1 = VacationHome(1000000)
    vh2 = VacationHome(900000)
    vm = VariableMortgage(360,{0: .08, 1: .10}, 500000, vh1)
    fm = FixedMortgage(360, .07, 900000, vh2)


    # Here I validate that the VariableMortgage and FixedMortgage
    # classes are functioning as intended.

    print('VariableMortgage rate function: ' + str(vm.rate(0)) + '\n')
    print('VariableMortgage rate function: ' + str(vm.rate(1)) + '\n')
    print('FixedMortgage rate function: ' + str(fm.rate(0)) + '\n')
    print('Type of VariableMortgage: ' + str(type(vm)) + '\n')
    print('Type of FixedMortgage: ' + str(type(fm)) + '\n')
    print(fm.toString() + '\n')
    print(vm.toString() + '\n')

    # Outstanding principal drops to less than 80% of the asset value at period 153 for this
    # fixed mortgage.  Here we see the fm.PMI(152) produces a non-zero result,
    # and fm.monthlyPayment(152) includes the PMI, while fm.PMI(153) = 0,
    # and fm.monthlyPayment(153) reflects the change in monthly payment accordingly.

    print('PMI test period 152: ' + str(fm.PMI(152)))
    print('monthlyPayment period 152: ' + str(fm.monthlyPayment(152)))
    print('PMI test period 153: ' + str(fm.PMI(153)))
    print('monthlyPayment period 153: ' + str(fm.monthlyPayment(153)))


    # Here, I create a loan object with the same term, rate, face and asset as the
    # fm Fixed Mortgage object above.  I test monthlyPayment and principalDue and compare.
    # I expect to see a difference in the monthly payment of the loan when PMI is a
    # factor in the FixedMortage, since the Loan object does not have PMI defined.
    # After period 152, I expect monthlyPayment to return the same value for both fm and l,
    # since there is no more PMI.  Additionally, I expect principalDue to be the same for both
    # for all periods.

    l = Loan(360, .07, 900000, vh2)

    print('\n' + 'Monthly payment on Loan object:  '
          + str(l.monthlyPayment(152)))
    print('Principal due on Loan object: '
          + str(l.principalDue(152)))
    print('Monthly payment on Fixed Mortgage object, where LTV below threshhold: '
          + str(fm.monthlyPayment(152)))
    print('Principal due on Fixed Mortgage object, where LTV below threshhold: '
          + str(fm.principalDue(152)))
    print('Monthly payment on Loan object: '
          + str(l.monthlyPayment(153)))
    print('Principal due on Loan object: '
          + str(l.principalDue(153)))
    print('Monthly payment on Fixed Mortgage object, where LTV above threshhold: '
          + str(fm.monthlyPayment(153)))
    print('Principal due on Fixed Mortgage object, where LTV above threshhold: '
          + str(fm.principalDue(153)))


if __name__ == '__main__':
    main()
