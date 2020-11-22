'''
This module tests various aspects of the LoanPool class.
'''

from classFiles.loan import Loan
from classFiles.loanpool import LoanPool
from classFiles.asset import Asset

def main():

    a = Asset(6000000, .08)
    l1 = Loan(360, .10, 500000, a)
    l2 = Loan(300, .08, 400000, a)
    l3 = Loan(180, .10, 100000, a)
    lp = LoanPool([l1, l2, l3])
    print('loanList: ' + str(lp.loanList) + '\n')
    print('getList method: ' + str(lp.getList()) + '\n')
    l4 = Loan(180, .05, 200000, a)
    lp2 = LoanPool([l1, l2, l3, l4])
    lp = lp2
    print('loanList: ' + str(lp.loanList) + '\n')
    print('getList method: ' + str(lp.getList()) + '\n')
    print('getTotalPrincipal: ' + str(lp.getTotalPrincipal()) + '\n')
    print('getTotalBalance: ' + str(lp.getTotalBalance(0)) + '\n')
    print('getPrincipalDue: ' + str(lp.getPrincipalDue(9)) + '\n')
    print('getInterestDue: ' + str(lp.getInterestDue(9)) + '\n')
    print('getPaymentDue: ' + str(lp.getPaymentDue(9)) + '\n')
    print('warPool: ' + str(lp.warPool()) + '\n')
    print('wamPool: ' + str(lp.wamPool()) + '\n')
    print('isActive: ' + str(lp.isActive(200)))

if __name__ == '__main__':
    main()
