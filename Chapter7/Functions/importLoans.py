'''
This module contains the importLoans function, which is used in main to import Loans_edit.csv.
'''

from Loan.loan import Loan
from Loan.autoloanmixin import FixedAutoLoan
from Loan.mortgagemixin import VariableMortgage, FixedMortgage
from Assets.asset import Asset
from Assets.car import Car, Lamborghini, Lexus, Civic
from Assets.housebase import PrimaryHome, VacationHome
from Functions.weightedaverage import warRed, wamRed
from Loan.loanpool import LoanPool
import ast
import random


def importLoans(csvpath):

    # This is an initial empty list.
    lnList = []
    with open(csvpath) as fp:
        for line in fp:
            lnList.append(line)

    # This is some manipulation to get the imported data into a loan object.
    for i in range(len(lnList)):
        lnList[i] = lnList[i][:-5].split(',')

    lnObjects = []

    for i in range(len(lnList)):
        lex = Lexus(float(lnList[i][3]))
        l = FixedAutoLoan(int(lnList[i][5]),float(lnList[i][4]),float(lnList[i][2]),lex)
        lnObjects.append(l)

    lp = LoanPool(lnObjects)
    return lp



