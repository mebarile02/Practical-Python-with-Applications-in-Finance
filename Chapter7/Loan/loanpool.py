'''
This module contains the LoanPool class.  The loanList parameter is a list of
loans objects.
'''

from Functions.weightedaverage import war, wam
import random

class LoanPool(object):

    def __init__(self, loanList):
        self._loanList = loanList
        self._runningTotPrin = 0
        self._timeperiod = 0

    def __iter__(self):
        for loan in self._loanList:
            yield loan

    @property
    def loanList(self):
        return self._loanList

    @property
    def timeperiod(self):
        return self._timeperiod

    @loanList.setter
    def loanList(self, iloanList):
        self._loanList = iloanList

    @timeperiod.setter
    def timeperiod(self,itimeperiod):
        self._timeperiod = itimeperiod

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

    def getRunningTotalPrincipal(self,period):
        totPrincipal = 0
        for i in range(len(self._loanList)):
            j = 0
            while j <= period:
                #print(self._loanList[i].principalDue(j))
                totPrincipal = totPrincipal + self._loanList[i].principalDue(j)
                j += 1
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

    # This function generates a list of uniformly distributed random integers, based of
    # default probabilities in case study description.  This gets called in the makePayments
    # function, which is, in turn called by the doWaterfall function.

    def checkDefaults(self):
        lst = []
        for i in range(len(self.loanList)):
            if 1 <= self.timeperiod <= 10:
                lst.append(random.randint(0,2000))
            elif 11 <= self.timeperiod <= 59:
                lst.append(random.randint(0,1000))
            elif 60 <= self.timeperiod <= 119:
                lst.append(random.randint(0,500))
            elif 120 <= self.timeperiod <= 179:
                lst.append(random.randint(0,250))
            elif 180 <= self.timeperiod <= 209:
                lst.append(random.randint(0,500))
            elif self.timeperiod >= 210:
                lst.append(random.randint(0,1000))
        return lst


    def increaseTimePeriod(self):
        for i in range(len(self.loanList)):
            self.loanList[i].timeperiod += 1
        self.timeperiod += 1

