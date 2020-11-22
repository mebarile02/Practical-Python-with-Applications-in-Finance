from classFiles.loan import Loan


class FixedRateLoan(Loan):
    def rate(self, period):

        # This overrides the Loan base class.

        return self._rate


    def toString(self):

        # This overrides the Loan base class.

        return 'FixedRateLoan(' + str(self._term) + ',' + str(self._rate) + ',' \
               + str(self._face) + ',' + str(self._asset) + ')'
