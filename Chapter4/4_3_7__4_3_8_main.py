'''
This module contains the program described in 4.3.7 and 4.3.8.  The user can add a loan,
or multiple loans.  They can then write the collection of loans to a csv file.  They can then open
a csv file, where the results are printed to the screen and each loan is stored as a loan subclass
object.  The list of loans is then used as input to a loan pool object.  If the loan pool contains no
variable rate loans, the user is presented with the choice of calculating WAR and WAM on the loan
pool before exiting the program.  This is because the WAR and WAM functions are defined only for fixed
rate loan types, per lecture requirements.  If they need to be modified going forward to accept
variable rate loans, I will look into that.
'''

from classFiles.Loan.loan import Loan
from classFiles.Loan.autoloanmixin import FixedAutoLoan
from classFiles.Loan.mortgagemixin import VariableMortgage, FixedMortgage
from classFiles.Assets.asset import Asset
from classFiles.Assets.car import Car, Lamborghini, Lexus, Civic
from classFiles.Assets.housebase import PrimaryHome, VacationHome
from functions.weightedaverage import warRed, wamRed
from classFiles.Loan.loanpool import LoanPool
import ast


def main():

    # Here, I initiate an empty list for loan details.
    lnList = []

    # Here, the user can add a loan, write a file and exit, or read a file.  Any other choice
    # prompts the same option.
    choice = input('Select 1 to add a loan\n2 to write a file and exit\n3 to read a file: \n')

    # Here, I initiate i = 0 for use with the While loop.
    i = 0

    while i == 0:
        while choice != '1' and choice != '2' and choice != '3':
            choice = input('Select 1 to add a loan\n2 to write a file and exit\n3 to read a file: \n')
        else:
            # The user has chosen to enter a loan, so they must select the loan type, home loan or car loan.
            if choice == '1':
                loanType = input('Enter 1 for Home Loan or 2 for Car Loan: ')
                if loanType == '1':
                    # If the user chooses home loan, they can select variable or fixed mortgage.
                    mortType = input('Enter 1 for Variable Rate Mortgage or 2 for Fixed Rate Mortgage: ')

                    while mortType != '1' and mortType != '2':
                        mortType = input('Enter 1 for Variable Rate Mortgage or 2 for Fixed Rate Mortgage: ')
                    else:
                        pass
                    # Here, if the user has selected home loan, they select home asset type.
                    assetType = input('Enter 1 for Primary Home or 2 for Vacation Home: ')

                    while assetType != '1' and assetType != '2':
                        assetType = input('Enter 1 for Primary Home or 2 for Vacation Home: ')
                    else:
                        pass
                    # Here, the user inputs the asset value and we make sure it is convertible to float.
                    assetVal = input('Enter initial asset value: ')

                    j = 0

                    while j == 0:
                        try:
                            float(assetVal)
                            j = 1
                        except:
                            assetVal = input('Enter initial asset value: ')
                    # Similarly, we validate input for face value of the loan.
                    faceVal = input('Enter face value of loan: ')

                    j = 0

                    while j == 0:
                        try:
                            float(faceVal)
                            j = 1
                        except:
                            faceVal = input('Enter face value of loan: ')
                    # Is the user chooses variable rate loan, they must enter a rate for the
                    # first period.
                    if mortType == '1':

                        r0 = input('Enter the rate for the first period of the loan: ')
                        j = 0

                        while j == 0:
                            try:
                                float(r0)
                                j += 1
                            except:
                                r0 = input('Enter the rate for the first period of the loan: ')

                        rate = {1: float(r0)}
                        print(rate)

                        j = 0
                        # They are then prompted to add an additional period and rate.
                        while j == 0:

                            k = input('Enter loan period key for rate dictionary: ')
                            h = 0

                            while h == 0:
                                try:
                                    int(k)
                                    h += 1
                                except:
                                    k = input('Enter loan period key for rate dictionary: ')

                            v = input('Enter loan rate value for rate dictionary: ')
                            h = 0

                            while h == 0:
                                try:
                                    float(v)
                                    h += 1
                                except:
                                    v = input('Enter loan rate value for rate dictionary: ')

                            rate[int(k)] = float(v)
                            print(rate)
                            # Here, the user can choose to continue entering period and rates for the
                            # variable rate loan, or move on.
                            cont = input('Enter 1 to continue entering key:value pairs, or 2 if you are done '
                                         'entering loan dictionary:  ')

                            while cont != '1' and cont != '2':
                                cont = input('Enter 1 to continue entering key:value pairs, or 2 if you are done '
                                             'entering loan dictionary:  ')
                            else:
                                pass

                            if cont == '2':
                                j += 1
                            else:
                                pass
                    else:
                        # If the loan is fixed, the user enters the rate.
                        rate = input('Enter rate: ')

                        k = 0

                        while k == 0:
                            try:
                                float(rate)
                                k += 1
                            except:
                                rate = input('Enter rate: ')

                    term = input('Enter the term of the loan, in months: ')
                    k = 0

                    while k == 0:
                        try:
                            int(term)
                            k += 1
                        except:
                            term = input('Enter the term of the loan, in months: ')
                    # Here, the asset type that was selected in used, along with other inputs,
                    # to create the asset.
                    if assetType == '1':
                        ast = PrimaryHome(float(assetVal))
                    elif assetType == '2':
                        ast = VacationHome(float(assetVal))
                    # Here, the loan subclass object is created, where rate is a dictionary for variable
                    # rate loans, or is converted to a float for fixed rate loans.
                    if mortType == '1':
                        ln = VariableMortgage(int(term), rate, float(faceVal), ast)
                    else:
                        ln = FixedMortgage(int(term), float(rate), float(faceVal), ast)
                    # The loan is added to the list, and the user is prompted with a choice.
                    lnList.append(ln)

                    choice = input('Select 1 to add a loan\n2 to write a file and exit\n3 to read a file: \n')

                # The car loan section is similar to the home loan section, but the user does not
                # have a choice for a variable rate loan.  They can choose one of three car types.
                elif loanType == '2':

                    assetType = input('Enter 1 for Lamborghini or 2 for Lexus or 3 for Civic: ')

                    while assetType != '1' and assetType != '2' and assetType != '3':
                        assetType = input('Enter 1 for Lamborghini or 2 for Lexus or 3 for Civic: ')

                    assetVal = input('Enter initial asset value: ')
                    k = 0

                    while k == 0:
                        try:
                            float(assetVal)
                            k += 1
                        except:
                            assetVal = input('Enter initial asset value: ')

                    faceVal = input('Enter face value of loan: ')
                    k = 0

                    while k == 0:
                        try:
                            float(faceVal)
                            k += 1
                        except:
                            faceVal = input('Enter face value of loan: ')

                    rate = input('Enter rate: ')
                    k = 0

                    while k == 0:
                        try:
                            float(rate)
                            k += 1
                        except:
                            rate = input('Enter rate: ')

                    term = input('Enter the term of the loan, in months: ')
                    k = 0

                    while k == 0:
                        try:
                            int(term)
                            k += 1
                        except:
                            rate = input('Enter term: ')

                    if assetType == '1':
                        ast = Lamborghini(float(assetVal))
                    elif assetType == '2':
                        ast = Lexus(float(assetVal))
                    else:
                        ast = Civic(float(assetVal))

                    ln = FixedAutoLoan(int(term),float(rate),float(faceVal),ast)
                    lnList.append(ln)

                    choice = input('Select 1 to add a loan\n2 to write a file and exit\n3 to read a file: \n')
                else:
                    print('Select a Valid Loan Type')
                    choice = input('Select 1 to add a loan\n2 to write a file and exit\n3 to read a file: \n')
            elif choice == '2':
                lnPool = LoanPool(lnList)
                # Once the user enters 2, they are prompted to enter a path to create a csv of
                # the individual loans. loan.rate is put in double quotes to handle the comma
                # that separates key:value pairs in the variable rate dictionary.  Otherwise,
                # the .csv file delimits between these commas as well.
                uifp = input('Please enter the file path to write the .csv file: ')

                with open(uifp, 'w') as fp:
                    for loan in lnPool:
                        fp.write(f'{loan.toString()},{loan.asset.toString()},{loan.asset.ival},'
                            f'{loan.face},"{loan.rate}",{loan.term}\n')
                i += 1
            else:
                # Here, when the user enters 3, they can specify a file path for a csv.
                # The loans details are printed to screen, and after some restructuring desribed below,
                # the loans are stored in loan subclass objects.  The list of loans is then passed
                # to a LoanPool object.
                ui = input('Please enter the file path of the loan .csv file:\n')

                # This is an initial empty list.
                lnList = []
                # .csv info is appended to the list, and each line of the .csv is printed to screen.
                with open(ui) as fp:
                    for line in fp:
                        print(line)
                        lnList.append(line)

                # This is an initial empty list for splitting at commas.
                lnListSp = []

                for j in range(len(lnList)):
                    lnListSp.append(lnList[j].split('"'))

                # This converts the rate dictionary in string form to a dict object, and/or converts
                # the rate for a fixed rate loans to a float, and then reassigns the new rate dict and/or
                # rate object to the appropriate index.
                for j in range(len(lnListSp)):
                    r = eval(lnListSp[j][1])
                    lnListSp[j][1] = r

                # This is additional cleanup to use the imported information to create loan objects.
                for j in range(len(lnListSp)):
                    lnListSp[j][0] = lnListSp[j][0].split(',')
                    lnListSp[j][2] = lnListSp[j][2].replace('\n','')
                    lnListSp[j][2] = lnListSp[j][2].replace(',','')
                    lnListSp[j][2] = int(lnListSp[j][2])

                # The imported .csv info is now manageable for creating loan objects, as below.
                finLoanList = []

                for j in range(len(lnListSp)):
                    if lnListSp[j][0][0] == 'Variable Rate Mortgage' and lnListSp[j][0][1] == 'Vacation Home':
                        ast = VacationHome(float(lnListSp[j][0][2]))
                        ln = VariableMortgage(lnListSp[j][2],lnListSp[j][1],float(lnListSp[j][0][3]),ast)
                        finLoanList.append(ln)
                    elif lnListSp[j][0][0] == 'Variable Rate Mortgage' and lnListSp[j][0][1] == 'Primary Home':
                        ast = PrimaryHome(float(lnListSp[j][0][2]))
                        ln = VariableMortgage(lnListSp[j][2],lnListSp[j][1],float(lnListSp[j][0][3]),ast)
                        finLoanList.append(ln)
                    elif lnListSp[j][0][0] == 'Fixed Rate Mortgage' and lnListSp[j][0][1] == 'Vacation Home':
                        ast = VacationHome(float(lnListSp[j][0][2]))
                        ln = FixedMortgage(lnListSp[j][2],lnListSp[j][1],float(lnListSp[j][0][3]),ast)
                        finLoanList.append(ln)
                    elif lnListSp[j][0][0] == 'Fixed Rate Mortgage' and lnListSp[j][0][1] == 'Primary Home':
                        ast = PrimaryHome(float(lnListSp[j][0][2]))
                        ln = FixedMortgage(lnListSp[j][2],lnListSp[j][1],float(lnListSp[j][0][3]),ast)
                        finLoanList.append(ln)
                    elif lnListSp[j][0][0] == 'Fixed Rate Auto Loan' and lnListSp[j][0][1] == 'Lamborghini':
                        ast = Lamborghini(float(lnListSp[j][0][2]))
                        ln = FixedAutoLoan(lnListSp[j][2], lnListSp[j][1], float(lnListSp[j][0][3]), ast)
                        finLoanList.append(ln)
                    elif lnListSp[j][0][0] == 'Fixed Rate Auto Loan' and lnListSp[j][0][1] == 'Lexus':
                        ast = Lexus(float(lnListSp[j][0][2]))
                        ln = FixedAutoLoan(lnListSp[j][2], lnListSp[j][1], float(lnListSp[j][0][3]), ast)
                        finLoanList.append(ln)
                    elif lnListSp[j][0][0] == 'Fixed Rate Auto Loan' and lnListSp[j][0][1] == 'Civic':
                        ast = Civic(float(lnListSp[j][0][2]))
                        ln = FixedAutoLoan(lnListSp[j][2], lnListSp[j][1], float(lnListSp[j][0][3]), ast)
                        finLoanList.append(ln)
                    else:
                        pass

                # A Loan Pool object is created.
                lp = LoanPool(finLoanList)

                h = 0
                # Here, if there is a variable rate mortgage in the list, the user will not be prompted
                # to calculate WAR and WAM.
                for loan in lp:
                    if loan.toString() == 'Variable Rate Mortgage':
                        h += 1
                    else:
                        pass

                if h == 0:
                    # Here, the user can calculate WAR and WAM if all loan types are fixed rate.
                    fCall = input('Enter 1 to calculate WAM and WAR of this loan pool, enter 2 to exit: ')

                    while fCall != '1' and fCall != '2':
                        fCall = input('Enter 1 to calculate WAM and WAR of this loan pool, enter 2 to exit: ')


                    if fCall == '1':
                        print(f'WAM: {lp.wamPool()}\n')
                        print(f'WAR: {lp.warPool()}\n')
                    else:
                        pass
                else:
                    pass

                i += 1

    else:
        pass


if __name__ == '__main__':
    main()