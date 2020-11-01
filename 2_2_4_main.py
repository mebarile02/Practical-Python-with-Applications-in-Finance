'''
Please refer to autoloanmixin in classFiles folder.  The FixedAutoLoan class
derives from autoloanmixin, which is essentially the same as mortgagemixin, but was created
in the event that different functionality needs to be added to mortgage-type loans versus
auto-type loans.
'''

from classFiles.autoloanmixin import FixedAutoLoan
from classFiles.car import Lamborghini

def main():

    lam = Lamborghini(110000)
    fal = FixedAutoLoan(60, .075, 109000, lam)

    print('Test for PMI: ' + str(fal.PMI(12)) + '\n')
    print('Test for monthlyPayment: ' + str(fal.monthlyPayment(12)) + '\n')
    print('Test for principalDue: ' + str(fal.principalDue(12)))




if __name__ == '__main__':
    main()