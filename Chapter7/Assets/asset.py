'''
This module contains the Asset class.
'''


class Asset(object):

    def __init__(self, ival, rate):
        self._ival = ival
        self._rate = rate

    # Getter and setter methods are created at the Asset level and passed on to
    # HouseBase and Car classes, which then pass on to their derived classes.

    @property
    def ival(self):
        return self._ival

    @ival.setter
    def ival(self, ivaln):
        self._ival = ivaln

    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, nrate):
        self._rate = nrate


    # These methods were created here, but annualDepRate raises a NotImplemented Error,
    # per assignment instructions.  This method is overridden in the inherited classes,
    # but monthlyDepRate and currentVal are still invoked by inherited classes.

    def annualDepRate(self):
        raise NotImplementedError()

    def monthlyDepRate(self):
        return self.annualDepRate()/12

    def currentVal(self, period):
        return self._ival * (1 - self.monthlyDepRate()) ** period
