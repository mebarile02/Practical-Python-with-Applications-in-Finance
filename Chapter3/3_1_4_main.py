'''
This module tests the ReconcileListsMod function with different lambda functions passed in.
'''


from functions.reconcilelists import reconcileListsMod, breakAbsolute, breakAbsRelative, breakRelative
from functools import partial
from random import uniform


def main():

    l1 = []
    l2 = []
    for i in range(100):
        l1.append(uniform(0, 1))
        l2.append(uniform(0, 1))
    print('List 1 of uniformly distributed random numbers:\n ' + str(l1) + '\n')
    print('List 2 of uniformly distributed random numbers: \n' + str(l2) + '\n')
    print('reconcileListsMod with breakAbsolute: '
          + str(reconcileListsMod(l1, l2, partial(breakAbsolute, epsilon=.5))) + '\n')
    print('reconcileListsMod with breakRelative: '
          + str(reconcileListsMod(l1, l2, partial(breakRelative, percent=10))) + '\n')
    print('reconcileListsMod with breakAbsRelative: '
          + str(reconcileListsMod(l1, l2, partial(breakAbsRelative, percent=10))) + '\n')


if __name__=='__main__':
    main()