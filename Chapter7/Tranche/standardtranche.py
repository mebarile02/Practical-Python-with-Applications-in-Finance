'''
This is the standard tranche subclass of the tranche class.
'''

from Tranche.tranche import Tranche
from Loan.loan import Loan
from Loan.loanpool import LoanPool

class StandardTranche(Tranche):

    # This class has several attributes.  The dictionaries are for the purpose of storing
    # historical calculations for use in subsequent steps of the makePayments method
    # in the structured securities class.  The makePayments method essentially recreates the
    # steps seen in the Excel spread provided in the course download, for both sequential
    # and pro rata modes.

    def __init__(self, notional, rate, subordination):
        self._notional = notional
        self._rate = rate
        self._subordination = subordination
        self._timeperiod = 0
        self._principaldict = {}
        self._interestdict = {}
        self._interestshortfall = {0:0}
        self._principalshortfall = {0:0}
        self._interestdue = {}
        self._balance = {}
        self._cashflows = []

        super(StandardTranche, self).__init__(notional, rate, subordination)

    @property
    def notional(self):
        return self._notional

    @property
    def rate(self):
        return self._rate

    @property
    def subordination(self):
        return self._subordination

    @property
    def timeperiod(self):
        return self._timeperiod

    @property
    def principaldict(self):
        return self._principaldict

    @property
    def interestdict(self):
        return self._interestdict

    @property
    def interestshortfall(self):
        return self._interestshortfall

    @property
    def principalshortfall(self):
        return self._principalshortfall

    @property
    def interestdue(self):
        return self._interestdue

    @property
    def cashflows(self):
        return self._cashflows

    @notional.setter
    def notional(self, inotional):
        self._notional = inotional

    @rate.setter
    def rate(self, irate):
        self._rate = irate

    @subordination.setter
    def subordination(self, isubordination):
        self._subordination = isubordination

    @timeperiod.setter
    def timeperiod(self,itimeperiod):
        self._timeperiod = itimeperiod

    def toString(self):
        return 'StandardTranche'

    def increaseTimePeriod(self):
        self._timeperiod += 1

    #These methods are called by the makePayments method in the structured securities class.
    #They both store key:value pairs of period:principal (or nterest) payment.

    def makePrincipalPayment(self, amt):
        if self._timeperiod in self._principaldict.keys():
            raise ValueError('makePrincipalPayment has already been called for this time period.')
        elif self.notionalBalance() == 0:
            self._principaldict[self._timeperiod] = 0
            return 0
            #raise ValueError('Notional balance is zero.')
        else:
            #self._principalshortfall[self._timeperiod] = self.notionalBalance(1)-amt
            self._principaldict[self._timeperiod] = amt

    def makeInterestPayment(self, amt):
        if self._timeperiod in self._interestdict.keys():
            raise ValueError('makeInterestPayment has already been called for this time period.')
        elif self.interestDue() == 0:
            self._interestshortfall[self._timeperiod] = 0
            self._interestdict[self._timeperiod] = 0
            return 0
        else:
            self._interestshortfall[self._timeperiod] = self.interestDue()-amt
            self._interestdict[self._timeperiod] = amt

    # This gives the balance, as defined in the last column of the Excel spread, initial
    # notional minus sum of principal payments to date.
    def notionalBalance(self,offset=0):
        principalpaymentstodate = sum(list(self._principaldict.values())[:(self._timeperiod-offset)])
        #interestshortfalltodate = sum(list(self._interestshortfall.values())[:(self._timeperiod-offset)])
        return self._notional - principalpaymentstodate #+ interestshortfalltodate

    def notionalBalanceInt(self, period):
        principalpaymentstodate = sum(list(self._principaldict.values())[:period])
        #interestshortfalltodate = sum(list(self._interestshortfall.values())[:period])
        interestshortfall = self._interestshortfall[period]
        return self._notional - principalpaymentstodate + interestshortfall

    # This defines interest due as the balance of the previous period times the monthly rate,
    # plus the interestshortfall.

    def interestDue(self):
        if self._timeperiod == 0:
            return 0
        else:
            interestshortfall = self._interestshortfall[self._timeperiod - 1]
            return self.notionalBalance(1) * StandardTranche.monthlyRate(self._rate) + interestshortfall

    def reset(self):
        self._timeperiod = 0

    @staticmethod
    def monthlyRate(rate):
        return rate/12

