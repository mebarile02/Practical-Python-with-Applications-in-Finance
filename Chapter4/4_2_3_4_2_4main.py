'''
This tests the logging modifications added to the Loan class.  Even though we would not typically
instantiate a loan object (versus a subclass of loan), I tested on a loan object to verify.
'''

from classFiles.Loan.loan import Loan
from classFiles.Assets.car import Lamborghini
import logging


def main():

    logging.getLogger().setLevel(logging.DEBUG)

    # Here, we handle the exception due to an invalid asset being passed to the loan, or toString()
    # being called on the loan.  These produce Errors with messages, as well as printing a custom
    # message to the user.

    try:
        ln = Loan(360,.10,50000,7)
    except Exception as ex:
        print(ex)

    lambo = Lamborghini(100000)
    ln = Loan(360, .10, 50000, lambo)

    try:
        ln.toString()
    except Exception as ex:
        print(ex)

    # Here, a loan is instantiated correctly.  The logger will display results from DEBUG and up.
    # I have commented out most of these, as it is best to go through them one by one.  Then, the
    # logging level is set to INFO and up, so you will no longer see DEBUG logs, and will only see
    # the WARNING logs due to using recursive functions.

    # As an example of the issue I emailed you about, observe the Total Interest statement below.
    # This calls ln.totalInterest.  I want to display the calculations for Total Interest in the DEBUG log.
    # The totalInterest() method calls totalPayments(). which in turn call monthlyPayment(), both of
    # which have their own DEBUG logs for calculations.  I can not find a clean way to suppress the DEBUG
    # logs for totalPayments() and monthlyPayment() when calling totalInterest().  Furthermore, logs
    # for totalPayments() and monthlyPayment() are displayed multiple times, since they are used in
    # the return value calculation of totalInterest(), as well as in the f-String for the DEBUG log
    # itself.  I suppose it may be useful, for debugging purposes, to show the calculations for
    # totalPayments() and monthlyPayment(), since they are used to calculate totalInterest(), but is
    # there a way to clean this up by at least removing the duplicate logs?

    ln1 = Loan(180, .06, 70000, lambo)
    #print(f'Monthly payment: {ln.monthlyPayment()}\n')
    #print(f'Total Payment: {ln.totalPayments()}\n')

    # This is referred to in notes above.
    print(f'Total Interest: {ln.totalInterest()}\n')

    #print(f'Interest Due: {ln.interestDue(10)}\n')
    #print(f'Interest Due Recursive: {ln.interestDueR(10)}\n')
    #print(f'Principal Due: {ln.principalDue(10)}\n')
    #print(f'Principal Due Recursive: {ln.principalDueR(10)}\n')
    #print(f'Loan Balance: {ln.balance(10)}\n')
    #print(f'Loan Balance Recursive: {ln.balanceR(10)}\n')
    #print(f'Recovery Value: {ln.recoveryValue(10)}\n')
    #print(f'Current Value: {lambo.currentVal(10)}\n')
    #print(f'Equity: {ln.equity(10)}\n')

    # Here, we set the logging level to INFO, so we no longer see DEBUG logs as above.
    # Here, we will see WARNING logs for using the recursive versions of Interest Due,
    # Principal Due and Loan Balance.

    logging.getLogger().setLevel(logging.INFO)

    print(f'Monthly payment: {ln.monthlyPayment()}\n')
    print(f'Total Payment: {ln.totalPayments()}\n')
    print(f'Total Interest: {ln.totalInterest()}\n')
    print(f'Interest Due: {ln.interestDue(10)}\n')
    print(f'Interest Due Recursive: {ln.interestDueR(10)}\n')
    print(f'Principal Due: {ln.principalDue(10)}\n')
    print(f'Principal Due Recursive: {ln.principalDueR(10)}\n')
    print(f'Loan Balance: {ln.balance(10)}\n')
    print(f'Loan Balance Recursive: {ln.balanceR(10)}\n')
    print(f'Recovery Value: {ln.recoveryValue(10)}\n')
    print(f'Current Value: {lambo.currentVal(10)}\n')
    print(f'Equity: {ln.equity(10)}\n')

    logging.getLogger().setLevel(logging.INFO)



if __name__ == '__main__':
    main()