from Loan.loan import Loan


class FixedRateLoan(Loan):

    @property
    def rate(self, period=None):
        # This overrides the Loan base class.
        return self._rate


    def toString(self):

        # This overrides the Loan base class.

        return 'FixedRateLoan'
