'''
This module contains the AutoLoanMixin and FixedAutoLoan classes.
'''

from classFiles.fixedrateloan import FixedRateLoan
from classFiles.car import Car


class AutoLoanMixin(object):
    def __init__(self, term, rate, face, car):
        if isinstance(car, Car):
            self._car = car
            super(AutoLoanMixin, self).__init__(term, rate, face, car)
        else:
            print('Enter a valid asset!\n')

    def PMI(self, period):
        if self.calcBalance(self._term, self._rate, self._face, period) >= .8 * self._car.ival:
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


class FixedAutoLoan(AutoLoanMixin, FixedRateLoan):
    pass