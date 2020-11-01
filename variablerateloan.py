from classFiles.loan import Loan


class VariableRateLoan(Loan):

    def __init__(self, term, rateDict, face, asset):
        self._rateDict = rateDict
        super(VariableRateLoan, self).__init__(term, None, face, asset)

    def rate(self, period):

        # This overrides the Loan class rate function.

        # print('In the VariableRateLoan rate function.')
        return self._rateDict[period]

    def toString(self):

        # This overrides the Loan class.

        return 'VariableRateLoan(' + str(self._term) + ',' + str(self._rateDict) + ',' \
               + str(self._face) + ',' + str(self._asset) + ')'
