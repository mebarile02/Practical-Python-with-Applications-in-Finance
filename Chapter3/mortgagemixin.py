'''
This module contains the MortgageMixin class, and the VariableMortgage and FixedMortgage
classes.
'''

from classFiles.Assets.housebase import HouseBase
from classFiles.Loan.fixedrateloan import FixedRateLoan
from classFiles.Loan.variablerateloan import VariableRateLoan


class MortgageMixin(object):
    def __init__(self, term, rate, face, home):
        if isinstance(home, HouseBase):
            self._home = home
            super(MortgageMixin, self).__init__(term, rate, face, home)
        else:
            print('Enter a valid asset!\n')

    def PMI(self, period):
        if self.calcBalance(self._term, self._rate, self._face, period) >= .8 * self._home.ival:
            return .000075 * self._face
        else:
            return 0

    def monthlyPayment(self, period):
        pmi = self.PMI(period)
        return self.calcMonthlyPmt(self._term, self._rate, self._face) + pmi

    def principalDue(self, period):
        if period == 0 or period > self._term:
            return 'Enter a valid period!'
        else:
            return self.monthlyPayment(period) - self.interestDue(period) - self.PMI(period)


class VariableMortgage(MortgageMixin, VariableRateLoan):
    pass


class FixedMortgage(MortgageMixin, FixedRateLoan):
    pass

