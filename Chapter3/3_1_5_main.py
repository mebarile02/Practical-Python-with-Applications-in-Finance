'''
This module uses the partial function as described in exercise 3.1.5.
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

    reconcileListsBreakAbsolute = partial(reconcileListsMod, breakFn=partial(breakAbsolute, epsilon=.5))
    print('reconcileListsBreakAbsolute:' + '\n' + str(reconcileListsBreakAbsolute(l1, l2)) + '\n')

    reconcileListsBreakRelative = partial(reconcileListsMod, breakFn=partial(breakRelative, percent=10))
    print('reconcileListsBreakRelative:' + '\n' + str(reconcileListsBreakRelative(l1, l2)) + '\n')

    reconcileListsBreakAbsRelative = partial(reconcileListsMod, breakFn=partial(breakAbsRelative, percent=10))
    print('reconcileListsBreakAbsRelative:' + '\n' + str(reconcileListsBreakAbsRelative(l1, l2)))


if __name__ == '__main__':
    main()