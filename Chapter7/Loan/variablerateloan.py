from Loan.loan import Loan


class VariableRateLoan(Loan):

    def __init__(self, term, rateDict, face, asset):
        self._rateDict = rateDict
        super(VariableRateLoan, self).__init__(term, None, face, asset)

    @property
    def rate(self, period=None):

        # This overrides the Loan class rate function.

        # print('In the VariableRateLoan rate function.')
        return self._rateDict


    def toString(self):

        # This overrides the Loan class.

        return 'VariableRateLoan'
