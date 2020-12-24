'''
This module contains the StructuredSecurities class.  It initiates with an empty
trancheList attribute.  There is a method defined that adds tranches and relevant
tranche details to this list.  There is a mode attribute, which defaults to None and needs
to be specified at runtime.  The reserve account is also stored as part of the ss object.
'''

from Tranche.tranche import Tranche
from Tranche.standardtranche import StandardTranche
from operator import itemgetter
from Loan.loanpool import LoanPool

class StructuredSecurities(object):

    def __init__(self, tnotional):
        self._tnotional = tnotional
        self._tranchelist = []
        self._mode = None
        self._reserveaccount = 0
        self._loanpool = None
        self._timeperiod = 0

    @property
    def reserveaccount(self):
        return self._reserveaccount

    @property
    def tnotional(self):
        return self._tnotional

    @property
    def trancheList(self):
        return self._tranchelist

    @property
    def mode(self):
        return self._mode

    @property
    def loanpool(self):
        return self._loanpool

    @property
    def timeperiod(self):
        return self._timeperiod

    @tnotional.setter
    def tnotional(self,itnotional):
        self._tnotional = itnotional

    def reset(self):
        self._timeperiod = 0
        for i in range(len(self._tranchelist)):
            self._tranchelist[i][0].reset()

    # This adds tranches to the ss tranche list with relevant details of tranche.
    def addTranche(self,tranche):
        if isinstance(tranche, Tranche):
            trancheclass = tranche.toString()
            percentnotional = tranche.notional/self._tnotional
            rate = tranche.rate
            subordinationlevel = tranche.subordination
            self._tranchelist.append([tranche, trancheclass, percentnotional, rate, subordinationlevel])
        else:
            raise TypeError('Please specify a Tranche object.')

    # This sets the mode as sequential or pro rata.
    def setMode(self, mode):
        if mode.lower() != 'sequential' and mode.lower() != 'pro rata':
            raise ValueError('Please enter Sequential or Pro Rata for mode.')
        else:
            self._mode = mode.lower()

    # This adds the loanpool to the ss object.
    def addLoanPool(self,loanpool):
        if isinstance(loanpool,LoanPool):
            self._loanpool = loanpool
        else:
            raise TypeError('Enter a LoanPool object.')

    def increaseTimePeriod(self):
        self._timeperiod += 1
        for i in range(len(self._tranchelist)):
            self._tranchelist[i][0].increaseTimePeriod()

    # The makePayments method starts with a cash amount and recreates the calculations of the
    # Excel spreadsheet example depending on pro rata or sequential mode selection.
    def makePayments(self,cash_amount):
        # upon calling, the time period is increased on both the ss and loanpool objects.
        self.increaseTimePeriod()
        self.loanpool.increaseTimePeriod()
        # Ultimately, this is where I want to call checkDefaults and pass the results to the
        # checkDefault function for each loan in the loan pool so that balances can
        # be set to zero for defaulted loans before running through interest and loan payments.
        ordertranchlist = list(sorted(self._tranchelist,key=itemgetter(4)))
        totalcash = cash_amount + self._reserveaccount
        # First, the interest is calculates and paid.
        for i in range(len(ordertranchlist)):
            interestdue = ordertranchlist[i][0].interestDue()
            ordertranchlist[i][0].interestdue[self._timeperiod] = interestdue
            ordertranchlist[i][0].makeInterestPayment(min(interestdue,totalcash))
            totalcash = totalcash - min(interestdue,totalcash)
        # Next, depending on mode, principal payments are made.  The sequential code
        # likely needs to be optimized, since it takes a long time to complete.  I think
        # the main problem with run time for sequential mode is that when it gets to the else
        # section, it calculates cumulative principal collection and cumulative principal
        # collection of the previous period by calling getRunningTotalPrincipal on the loanpool
        # object.  This is inefficient, because getRunningTotalPrincipal loops through all
        # loans in the loanpool objects to calculate the running total principal, and this is
        # compounded by the issue that it is called twice, once for the current period and once
        # for the previous.
        if self._mode == 'sequential':
            for i in range(len(ordertranchlist)):
                totalprincipal = self._loanpool.getPrincipalDue(self._timeperiod)
                if i == 0:
                    principaldue = min(ordertranchlist[i][0].notionalBalance(1),totalprincipal  \
                                    + ordertranchlist[i][0].principalshortfall[self._timeperiod - 1])
                    ordertranchlist[i][0].makePrincipalPayment(min(principaldue,totalcash))
                    ordertranchlist[i][0].principalshortfall[self._timeperiod] = \
                        principaldue - min(principaldue,totalcash)
                    totalcash = totalcash - min(principaldue,totalcash)
                else:
                    cumulativeprincipalcollection = self._loanpool.getRunningTotalPrincipal(self._timeperiod)
                    cumulativeprincipalcollectionprev = self._loanpool.getRunningTotalPrincipal(self._timeperiod - 1)
                    principaldue= min(ordertranchlist[i][0].notionalBalance(1),max(0,cumulativeprincipalcollection
                        -max(ordertranchlist[0][0].notional,cumulativeprincipalcollectionprev))) \
                                    + ordertranchlist[i][0].principalshortfall[self._timeperiod - 1]
                    ordertranchlist[i][0].makePrincipalPayment(min(totalcash,principaldue))
                    ordertranchlist[i][0].principalshortfall[self._timeperiod] = \
                        principaldue - min(principaldue,totalcash)
                    self._reserveaccount = totalcash - min(principaldue,totalcash)
        else:
            for i in range(len(ordertranchlist)):
                principaldue = min(ordertranchlist[i][0].notionalBalance(1),
                                    (ordertranchlist[i][0].notional/self._tnotional) *
                                    self._loanpool.getPrincipalDue(self._timeperiod) +
                                    ordertranchlist[i][0].principalshortfall[self._timeperiod - 1])
                ordertranchlist[i][0].makePrincipalPayment(min(totalcash, principaldue))
                ordertranchlist[i][0].principalshortfall[self._timeperiod] = principaldue - min(principaldue, totalcash)
                totalcash = totalcash - min(principaldue, totalcash)
                if i != len(ordertranchlist) - 1:
                    pass
                else:
                    self._reserveaccount = totalcash


    # The getWaterfall method is used in the doWaterfall standalone function as
    # described in the case document.

    def getWaterfall(self, period):
        lst = []
        ordertranchlist = list(sorted(self._tranchelist,key=itemgetter(4)))
        try:
            for tr in ordertranchlist:
                if period == 0:
                    lst.append([0,tr[0].subordination.upper(),
                                0, 0, 0, 0,tr[0].notional])
                else:
                    lst.append([period, tr[0].subordination.upper(),
                                    tr[0].interestdue[period],
                                tr[0].interestdict[period],
                                   tr[0].interestshortfall[period],
                                tr[0].principaldict[period],
                                   tr[0].notionalBalance()])
            return lst
        except KeyError:
            return 'There is no information for that period.'


def main():
    pass

if __name__ == '__main__':
    main()


