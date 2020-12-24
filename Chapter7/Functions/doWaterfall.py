'''
This module contains the doWaterfall standalone function, as well as the ABSRating function.
'''

from Loan.loanpool import LoanPool
from StructuredSecurities.structuredsecurities import StructuredSecurities

# This function accepts a tranche and a (converted) DIRR to print the ABSRating to screen.

def ABSRating(tr, d):
    print(f'ABS Rating for Tranche {tr}:', end =" ")
    if d <= .06:
        print('Aaa')
    elif d <= 0.67:
        print('Aa1')
    elif d <= 1.3:
        print('Aa2')
    elif d <= 2.7:
        print('Aa3')
    elif d <= 5.2:
        print('A1')
    elif d <= 8.9:
        print('A2')
    elif d <= 13:
        print('A3')
    elif d <= 19:
        print('Baa1')
    elif d <= 27:
        print('Baa2')
    elif d <= 46:
        print('Baa3')
    elif d <= 72:
        print('Ba1')
    elif d <= 106:
        print('Ba2')
    elif d <= 143:
        print('Ba3')
    elif d <= 183:
        print('B1')
    elif d <= 231:
        print('B2')
    elif d <= 311:
        print('B3')
    elif d <= 2500:
        print('Caa')
    else:
        print('Ca')

# This is the doWaterfall function.  It accepts a loan pool and structured securities object.

def doWaterfall(lp, ss):
    if isinstance(lp, LoanPool) and isinstance(ss, StructuredSecurities):
        if ss.trancheList == []:
            raise ValueError('Please add tranches to the Structured Securities Object.')
        else:
            a = []
            b = []
            i = 1
            #k = 0
            err = .01
            # This while loop keeps running until the tranche balances are lower than .50, to account
            # for rounding.  This calls makePayments throughout the loop and uses getWaterfall
            # to store data to lists.  It then formats for output to screen in the main function, calling
            # IRR, DIRR and AL methods.
            while ss.trancheList[0][0].notionalBalance() + ss.trancheList[1][0].notionalBalance() > err:
                ss.makePayments(lp.getPaymentDue(i))
                if i == 1:
                    a.append(ss.getWaterfall(i-1))
                    b.append(0)
                    a.append(ss.getWaterfall(i))
                    b.append(ss.reserveaccount)
                else:
                    a.append(ss.getWaterfall(i))
                    b.append(ss.reserveaccount)
                i += 1
            lst = []
            for j in range(len(a)):
                lst.append(a[j][0]+a[j][1][1:]+[b[j]])
            for i in range(len(lst)):
                if i == 0:
                    # This step is to associate cashflows with each tranche for use
                    # with the IRR, DIRR and AL functions.
                    ss.trancheList[0][0].cashflows.append((-1) * lst[i][6])
                    ss.trancheList[1][0].cashflows.append((-1) * lst[i][12])
                else:
                    ss.trancheList[0][0].cashflows.append(lst[i][3] + lst[i][5])
                    ss.trancheList[1][0].cashflows.append(lst[i][9] + lst[i][11])
            # Here, methods are called and printed to screen.
            print(f'Tranche A IRR: {ss.trancheList[0][0].IRR()}')
            print(f'Tranche A DIRR: {ss.trancheList[0][0].DIRR()}')
            print(f'Tranche A Average Life: {ss.trancheList[0][0].AL()}')
            dirrAbasis = ss.trancheList[0][0].DIRR()*100
            ABSRating('A',dirrAbasis)
            print(f'Tranche B IRR: {ss.trancheList[1][0].IRR()}')
            print(f'Tranche B DIRR: {ss.trancheList[1][0].DIRR()}')
            print(f'Tranche B Average Life: {ss.trancheList[1][0].AL()}')
            dirrBbasis = ss.trancheList[1][0].DIRR()*100
            ABSRating('B',dirrBbasis)
            return lst

    else:
        raise TypeError('Please enter a valid loan pool and Structured Securities Object.')
