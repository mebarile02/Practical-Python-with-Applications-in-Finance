from classFiles.loan import Loan
from classFiles.asset import Asset
from classFiles.car import Lamborghini
from classFiles.mortgagemixin import FixedMortgage
from classFiles.housebase import PrimaryHome
from classFiles.autoloanmixin import FixedAutoLoan

def main():

    # Here I initialize an asset and loan with this asset.
    a = Asset(100000, .05)
    l = Loan(360, .05, 500000, a)
    print('Returns depreciation rate of asset: ' + str(l.asset.rate) + '\n')

    # Here I test whether I can set a new asset in the loan.

    l.asset = Asset(500000, .02)
    print('Returns new depreciation rate of asset: ' + str(l.asset.rate) + '\n')

    # Here, I put an int for asset to verify that I receive an error message since
    # this object is not in the Asset class, or classes derived from the Asset class.
    l2 = Loan(60, .09, 80000, 2)

    # Here, I test for functionality on subclasses of the Asset and Loan classes.
    ph = PrimaryHome(1000000)
    fm = FixedMortgage(360, .06, 900000, ph)

    # And again, I test for the error message when entering an object that is not an
    # Asset or derived from the Asset class.

    fm2 = FixedMortgage(300, .07, 500000, 'test')
    print('PMI test for FixedMortgage: ' + str(fm.PMI(70)) + '\n')

    # Here, I create a Lamborghini object, derived from the Car class, which was itself
    # derived from the Asset class.  I then test some of the functions from the Loan base
    # class using a FixedAutoLoan.
    lamb = Lamborghini(200000)
    fal = FixedAutoLoan(60, .06, 180000, lamb)
    print('PMI test for FixedAutoLoan: ' + str(fal.PMI(4)) + '\n')
    print('balance test for FixedAutoLoan: ' + str(fal.balance(9)) + '\n')
    print('currentVal test for Lamborghini: ' + str(lamb.currentVal(9)) + '\n')
    print('recoveryValue test for FixedAutoLoan: ' + str(fal.recoveryValue(9)) + '\n')
    print('equity test for FixedAutoLoan: ' + str(fal.equity(9)))





if __name__ == '__main__':
    main()