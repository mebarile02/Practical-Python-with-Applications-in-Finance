'''
This module tests Loan classes for exception/error handling of an invalid asset.
'''
from classFiles.Loan.loan import Loan
from classFiles.Assets.car import Lamborghini
from classFiles.Loan.fixedrateloan import FixedRateLoan
from classFiles.Loan.variablerateloan import VariableRateLoan

def main():

    lambo = Lamborghini(100000)

    try:
        l = Loan(60, .04, 80000, 10)
    except Exception as ex:
        print(ex)

    try:
        frl = FixedRateLoan(60, .04, 80000, 10)
    except Exception as ex:
        print(ex)

    try:
        frl = VariableRateLoan(60, {1: .05, 2: .07}, 80000, 10)
    except Exception as ex:
        print(ex)

    try:
        frl = VariableRateLoan(60, {1: .05, 2: .07}, 80000, lambo)
    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    main()