'''
This module spot-checks some of the classes derived from the Asset class for functionality
(Civic class derived from Car class derived from Asset class, and VacationHome class and
PrimaryHome class derived from HouseBase class derived from Asset class).
'''

from classFiles.car import Lamborghini, Civic, Lexus
from classFiles.housebase import VacationHome, PrimaryHome


def main():

    #  Here, I create some objects from classes derived from the Asset Class and test.

    civ = Civic(25000)
    print('The default depreciation rate for the Civic: ' + str(civ.rate) + '\n')
    civ.rate = .17
    print('Setting a new depreciation rate for the Civic: ' + str(civ.rate) + '\n')
    print('Monthly depreciation rate for the Civic: ' + str(civ.monthlyDepRate()) + '\n')
    print('Testing the currentVal method inherited from the Car Class: ' +
          str(civ.currentVal(60)) + '\n')

    vh = VacationHome(1000000)
    ph = PrimaryHome(500000)
    print('Initialized value of vacation home: ' + str(vh.ival) + '\n')
    vh.ival = 1200000
    print('Value of vacation home after changing: ' + str(vh.ival) + '\n')
    print('Testing the currentVal method inherited from the Car Class: ' +
          str(ph.currentVal(12)) + '\n')


if __name__ == '__main__':
    main()