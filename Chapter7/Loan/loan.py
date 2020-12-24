'''
This module contains the basic Loan class.
'''

import logging
from Assets.asset import Asset


class Loan(object):

    #logging.getLogger().setLevel(logging.DEBUG)

    _id = 0

    def __init__(self, term, rate, face, asset):
        if isinstance(asset, Asset):
            self._term = term
            self._rate = rate
            self._face = face
            self._asset = asset
            self._id = Loan._id + 1
            self._default = 1
            self._timeperiod = 0
            Loan._id += 1
        else:
            logging.error(' You have not entered a valid asset.')
            raise TypeError('Please enter a valid asset.')

    def getId(self):
        return self._id

    def toString(self):
        logging.error(' This produces a NotImplemented Error.')
        raise NotImplementedError('Not Implemented Error.')

    def printLoan(self):
        print(self.toString())

    # Here I add the getter property methods.
    @property
    def timeperiod(self):
        return self._timeperiod

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

    @property
    def default(self):
        return self._default

    # Here I add the setter property methods.
    @default.setter
    def timeperiod(self,itimeperiod):
        self._timeperiod = itimeperiod


    @default.setter
    def default(self,idefault):
        self._default = idefault

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
        if period > self._term:
            return 0
        elif period == 0:
            return 0
        else:
            return self.calcMonthlyPmt(self._term, self._rate, self._face)

    # @classmethod
    # def calcMonthlyPmt(cls, term, rate, face):
    #     return ((rate / 12) * face * (1 + rate / 12) ** term) / \
    #            ((1 + rate / 12) ** term - 1)

    @classmethod
    def calcMonthlyPmt(cls, term, rate, face):
        logging.debug(f' Monthly Payment: {Loan.monthlyRate(rate)} * {face} * (1 + {Loan.monthlyRate(rate)}) '
                      f'^ {term} / ((1 + {Loan.monthlyRate(rate)}) ^ {term}) - 1)')
        return (Loan.monthlyRate(rate) * face * (1 + Loan.monthlyRate(rate)) ** term) / \
               ((1 + Loan.monthlyRate(rate)) ** term - 1)

    def totalPayments(self, period=None):
        logging.debug(f' Total Payments: {self._term} * {self.monthlyPayment()}')
        return self._term * self.monthlyPayment()

    def totalInterest(self, period=None):
        logging.debug(f' Total Interest: {self.totalPayments()} - {self._face}')
        return self.totalPayments() - self._face

    # def interestDue(self, period):
    #     if period == 0 or period > self._term:
    #         return 'Enter a valid period!'
    #     else:
    #         return (self._rate / 12) * self.balance(period - 1)

    def interestDue(self, period):
        if period <= 0 or period > self._term:
            return 0
        else:
            logging.debug(f' Interest Due: {Loan.monthlyRate(self._rate)} * {self.balance(period - 1)}')
            return (Loan.monthlyRate(self._rate)) * self.balance(period - 1)

    def interestDueR(self, period):
        logging.warning(' It is recommended to use the non-recursive version of this function.')
        if period == 0 or period > self._term:
            logging.info(' An invalid period has been entered.')
            return 'Enter a valid period!'
        else:
            bal = self._face
            for i in range(period):
                interest = (Loan.monthlyRate(self._rate)) * bal
                bal = bal - self.monthlyPayment() + interest
                logging.debug(f' Calculation {i + 1}:\n'
                              f'Interest = {interest}\n'
                              f'Balance = {bal}')
            return interest

    def principalDue(self, period):
        if period <= 0 or period > self._term:
            return 0
        else:
            logging.debug(f' Principal Due: {self.monthlyPayment()} - {self.interestDue(period)}')
            return self.monthlyPayment() - self.interestDue(period)

    def principalDueR(self, period):
        logging.warning(' It is recommended to use the non-recursive version of this function.\n')
        if period == 0 or period > self._term:
            logging.info(' An invalid period has been entered.')
            return 'Enter a valid period!'
        else:
            bal = self._face
            for i in range(period):
                interest = (Loan.monthlyRate(self._rate)) * bal
                principal = self.monthlyPayment() - interest
                bal = bal - self.monthlyPayment() + interest
                logging.debug(f' Calculation {i + 1}:\n'
                              f'Interest = {interest}\n'
                              f'Principal = {principal}\n'
                              f'Balance = {bal}')
            return principal

    # def balance(self, period):
    #     if period > self._term or period < 0:
    #         return 'Enter a valid period!'
    #     else:
    #         return self._face * (1 + self._rate / 12) ** period - self.monthlyPayment() * \
    #             ((1 + self._rate/12) ** period - 1)/(self._rate / 12)

    def balance(self, period):
        if self._default == 0:
            return 0
        else:
            return self.calcBalance(self._term, self._rate, self._face, period)

    # This class-level method invokes the calcMonthlyPmt class-level method.

    @classmethod
    def calcBalance(cls, term, rate, face, period):
        if period < 0 or period > term:
            logging.info(' An invalid period has been entered.')
            return 0
        else:
            logging.debug(f' Balance: {face} * (1 + {Loan.monthlyRate(rate)}) ** {period} - '
                          f'{cls.calcMonthlyPmt(term, rate, face)} * ((1 + {Loan.monthlyRate(rate)}) ** '
                          f'{period} - 1) / {(Loan.monthlyRate(rate))})')
            return face * (1 + Loan.monthlyRate(rate)) ** period - cls.calcMonthlyPmt(term, rate, face) * \
                   ((1 + Loan.monthlyRate(rate)) ** period - 1) / (Loan.monthlyRate(rate))


    def balanceR(self, period):
        logging.warning(' It is recommended to use the non-recursive version of this function.\n')
        if period > self._term or period < 0:
            logging.info(' An invalid period has been entered.')
            return 'Enter a valid period!'
        else:
            bal = self._face
            for i in range(period):
                interest = (Loan.monthlyRate(self._rate)) * bal
                bal = bal - self.monthlyPayment() + interest
                logging.debug(f' Calculation {i + 1}:\n'
                              f'Interest = {interest}\n'
                              f'Balance = {bal}\n')
            return bal


    def recoveryValue(self, period):
        logging.debug(f' Recovery Value: {self._asset.currentVal(period)} * .6 ')
        return self._asset.currentVal(period) * .6

    def equity(self, period):
        logging.debug(f' Equity: {self._asset.currentVal(period)} - {self.balance(period)}')
        return self._asset.currentVal(period) - self.balance(period)

    # If the value passed to this method is 0, it sets the default attribute to 0, which in
    # turn sets the loan balance to 0.  It also returns that current value of the asset upon
    # default.
    def checkDefault(self,val):
        if val == 0:
            self.default = 0
            return self.asset.currentVal(self.timeperiod)
        else:
            pass

    @staticmethod
    def monthlyRate(rate):
        return rate/12

    @staticmethod
    def annualRate(rate):
        return 12*rate










