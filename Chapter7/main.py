'''
This is the main function for testing the case study.  A structured securities object is created
with the total notional as the sum of all loan values in the spreadsheet.  Two tranche objects
are created and added to the structured security object. The loan csv is imported as a loan
pool attached to the structured security object.  You will observe the Loans_edit.csv file,
which is included here in the Root Folder, is the same as the file provided in the course
download, but reformatted for easier importing based on how I initially set it up.  This
is set up to run pro rata, which takes about 16 seconds to go through all the loans/period
to pay down to zero using doWaterfall.  When set at sequential, it takes around 10 minutes.
Tranche IRR, DIRR Average Life and ABS Ratings are printed to screen, and the output of
doWaterfall is exported to csv.
'''

from Tranche.standardtranche import StandardTranche
from StructuredSecurities.structuredsecurities import StructuredSecurities
from Loan.loanpool import LoanPool
from Loan.autoloanmixin import FixedAutoLoan
from Assets.car import Lamborghini, Lexus, Civic
from Functions.doWaterfall import doWaterfall
from Functions.importLoans import importLoans
import csv
import time

def main():

    totalnotional = 28354374.3178204
    ss = StructuredSecurities(totalnotional)
    t1 = StandardTranche(totalnotional*.7,.05,'a')
    t2 = StandardTranche(totalnotional*.3,.08,'b')
    ss.addTranche(t1)
    ss.addTranche(t2)
    lp = importLoans('/Users/michaelbarile/Desktop/Loans_edit.csv')
    ss.addLoanPool(lp)
    # This is set to pro rata, but can also be set to sequential.  Sequential takes
    # considerably longer, and probably needs to be optimized for more efficiency.
    ss.setMode('pro rata')

    s = time.time()
    output = doWaterfall(lp,ss)
    e = time.time()
    print(f'Runtime: {e - s}')

    with open('/Users/michaelbarile/Desktop/doWFoutput.csv', 'w', newline="") as fp:
        writer = csv.writer(fp)
        writer.writerow(['Period','Tranche','Interest Due','Interest Paid','Interest Shortfall'
                            ,'Principal Paid','Balance','Tranche','Interest Due','Interest Paid',
                         'Interest Shortfall','Principal Paid','Balance','Cash Reserve'])
        writer.writerows(output)

if __name__ == '__main__':
    main()
