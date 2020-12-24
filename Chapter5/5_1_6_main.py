'''
This module validates some of the changes made to the Loan class to ensure that startdate and
enddate parameters for the loan work correctly (as opposed to term).
'''

from classFiles.Loan.loan import Loan
from classFiles.Assets.asset import Asset

def main():

    a = Asset(1000000, .02)
    l = Loan('2000-01-01','2029-12-31', .09, 500000, a)
    print(f'Loan term, in months: {l.term()}')
    print(f'Loan start date: {l.stdate}')
    l.stdate = '2010-01-01'
    print(f'New loan start date: {l.stdate}')
    print(f'Loan monthly payments, which uses term() method: {l.monthlyPayment()}')
    print(f'Loan total payments, which uses term() method: {l.totalPayments()}')


if __name__ == '__main__':
    main()