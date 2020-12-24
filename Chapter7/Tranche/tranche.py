'''
This is the Tranche base class.  Some of the attributes did not end up getting used,
but were added for possible code revisions in the future, specifically to address the
length of time it takes for sequential mode to run.
'''

import numpy as np

class Tranche(object):

    def __init__(self, notional, rate, subordination):
        self._notional = notional
        self._rate = rate
        self._subordination = subordination
        self._cashflows = []
        self._principaldict = {}

    def toString(self):
        raise NotImplementedError('Not Implemented Error.')

    @property
    def notional(self):
        return self._notional

    @property
    def rate(self):
        return self._rate

    @property
    def subordination(self):
        return self._subordination


    @notional.setter
    def notional(self, inotional):
        self._notional = inotional

    @rate.setter
    def rate(self,irate):
        self._rate = irate

    @subordination.setter
    def subordination(self,isubordination):
        self._subordination = isubordination

    # IRR, DIRR and AL functions are defined here for use the with the standard tranche
    # subclass.  The IRR function delegates to the numpy irr function, as described
    # in case study description.
    def IRR(self):
        return 100*12*np.irr(self._cashflows)

    def DIRR(self):
        return 100*self._rate - self.IRR()

    # Here, I use a loop to calculate the AL, although the reduce function may be preferred.
    def AL(self):
        AL = 0
        for i in range(1,len(self._principaldict)+1):
            AL += i * self._principaldict[i]
        AL = AL/self._notional
        totalpaid = sum(self._principaldict.values())
        if abs(totalpaid-self._notional) > .50:
            return None
        else:
            return AL
