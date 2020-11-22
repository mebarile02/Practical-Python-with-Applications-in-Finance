'''
This module contains the LoanPool class.  The loanList parameter is a list of
loans objects.
'''

from functions.weightedaverage import war, wam

class LoanPool(object):

    def __init__(self, loanList):
        self._loanList = loanList

    def __iter__(self):
        for loan in self._loanList:
            yield loan

    @property
    def loanList(self):
        return self._loanList

    @loanList.setter
    def loanList(self, iloanList):
        self._loanList = iloanList

    # The getList method returns a list of tuples with loan details for easier viewing.
    def getList(self):
        initList = []
        for i in range(len(self._loanList)):
            initList.append((self._loanList[i].term, self._loanList[i].rate,self._loanList[i].face,
                             self._loanList[i].asset))
        return initList

    def getTotalPrincipal(self):
        totPrincipal = 0
        for i in range(len(self._loanList)):
            totPrincipal = totPrincipal + self._loanList[i].face
        return totPrincipal

    def getTotalBalance(self, period):
        totBalance = 0
        for i in range(len(self._loanList)):
            totBalance = totBalance + self._loanList[i].balance(period)
        return totBalance

    def getPrincipalDue(self, period):
        totPrincipalDue = 0
        for i in range(len(self._loanList)):
            totPrincipalDue = totPrincipalDue + self._loanList[i].principalDue(period)
        return totPrincipalDue

    def getInterestDue(self, period):
        totInterestDue = 0
        for i in range(len(self._loanList)):
            totInterestDue = totInterestDue + self._loanList[i].interestDue(period)
        return totInterestDue

    def getPaymentDue(self, period):
        totPaymentDue = 0
        for i in range(len(self._loanList)):
            totPaymentDue = totPaymentDue + self._loanList[i].monthlyPayment(period)
        return totPaymentDue

    def isActive(self, period):
        active = 0
        for i in range(len(self._loanList)):
            if self._loanList[i].term < period:
                pass
            else:
                active += 1
        return active

    def warPool(self):
        initList = []
        for i in range(len(self._loanList)):
            initList.append((self._loanList[i].term, self._loanList[i].rate,self._loanList[i].face))
        return war(initList)

    def wamPool(self):
        initList = []
        for i in range(len(self._loanList)):
            initList.append((self._loanList[i].term, self._loanList[i].rate,self._loanList[i].face))
        return wam(initList)



