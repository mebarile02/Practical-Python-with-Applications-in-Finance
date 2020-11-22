'''
This module contains the basic Loan class.
'''

from classFiles.Assets.asset import Asset


class Loan(object):
    _id = 0

    def __init__(self, term, rate, face, asset):
        if isinstance(asset, Asset):
            self._term = term
            self._rate = rate
            self._face = face
            self._asset = asset
            self._id = Loan._id + 1
            Loan._id += 1
        else:
            raise TypeError('Please enter a valid asset.')

    def getId(self):
        return self._id

    def toString(self):
        raise NotImplementedError()

    def printLoan(self):
        print(self.toString())

    # Here I add the getter property methods.
    @property
    def term(self):
        return self._term

    @property
    def rate(self):
        return self._rate

    @property
    def face(self):
        return self._face

    @property
    def asset(self):
        return self._asset

    # Here I add the setter property methods.
    @term.setter
    def term(self, iterm):
        self._term = iterm

    @rate.setter
    def rate(self, irate):
        self._rate = irate

    @face.setter
    def face(self, iface):
        self._face = iface

    @asset.setter
    def asset(self, iasset):
        self._asset = iasset


    # def monthlyPayment(self, period=None):
    #     return ((self._rate / 12) * self._face * (1 + self._rate / 12) ** self._term) /\
    #            ((1 + (self._rate / 12)) ** self._term - 1)

    def monthlyPayment(self, period=None):
        return self.calcMonthlyPmt(self._term, self._rate, self._face)

    # @classmethod
    # def calcMonthlyPmt(cls, term, rate, face):
    #     return ((rate / 12) * face * (1 + rate / 12) ** term) / \
    #            ((1 + rate / 12) ** term - 1)

    @classmethod
    def calcMonthlyPmt(cls, term, rate, face):
        return (Loan.monthlyRate(rate) * face * (1 + Loan.monthlyRate(rate)) ** term) / \
               ((1 + Loan.monthlyRate(rate)) ** term - 1)

    def totalPayments(self, period=None):
        return self._term * self.monthlyPayment()

    def totalInterest(self, period=None):
        return self.totalPayments() - self._face

    # def interestDue(self, period):
    #     if period == 0 or period > self._term:
    #         return 'Enter a valid period!'
    #     else:
    #         return (self._rate / 12) * self.balance(period - 1)

    def interestDue(self, period):
        if period == 0 or period > self._term:
            return 'Enter a valid period!'
        else:
            return (Loan.monthlyRate(self._rate)) * self.balance(period - 1)

    def interestDueR(self, period):
        if period == 0 or period > self._term:
            return 'Enter a valid period!'
        else:
            bal = self._face
            for i in range(period):
                interest = (Loan.monthlyRate(self._rate)) * bal
                bal = bal - self.monthlyPayment() + interest
            return interest

    def principalDue(self, period):
        if period == 0 or period > self._term:
            return 'Enter a valid period!'
        else:
            return self.monthlyPayment() - self.interestDue(period)

    def principalDueR(self, period):
        if period == 0 or period > self._term:
            return 'Enter a valid period!'
        else:
            bal = self._face
            for i in range(period):
                interest = (Loan.monthlyRate(self._rate)) * bal
                principal = self.monthlyPayment() - interest
                bal = bal - self.monthlyPayment() + interest
            return principal

    # def balance(self, period):
    #     if period > self._term or period < 0:
    #         return 'Enter a valid period!'
    #     else:
    #         return self._face * (1 + self._rate / 12) ** period - self.monthlyPayment() * \
    #             ((1 + self._rate/12) ** period - 1)/(self._rate / 12)

    def balance(self, period):
        return self.calcBalance(self._term, self._rate, self._face, period)

    # Thie class-level method invokes the calcMonthlyPmt class-level method.

    @classmethod
    def calcBalance(cls, term, rate, face, period):
        if period > term or period < 0:
            return 'Enter a valid period!'
        else:
            return face * (1 + Loan.monthlyRate(rate)) ** period - cls.calcMonthlyPmt(term, rate, face) * \
                   ((1 + Loan.monthlyRate(rate)) ** period - 1) / (Loan.monthlyRate(rate))


    def balanceR(self, period):
        if period > self._term or period < 0:
            return 'Enter a valid period!'
        else:
            bal = self._face
            for i in range(period):
                interest = (Loan.monthlyRate(self._rate)) * bal
                bal = bal - self.monthlyPayment() + interest
            return bal


    def recoveryValue(self, period):
        return self._asset.currentVal(period) * .6

    def equity(self, period):
        return self._asset.currentVal(period) - self.balance(period)

    @staticmethod
    def monthlyRate(rate):
        return rate/12

    @staticmethod
    def annualRate(rate):
        return 12*rate







