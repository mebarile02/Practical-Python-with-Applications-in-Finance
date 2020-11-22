'''
This module includes the reconcileLists functions and related lambda functions.  It includes both the original
reconcileLists function, as well as the modified reconcileListsMod function, which accepts the breakFn parameter.
'''

import math
from functools import partial
import random

breakAbsolute = lambda x, y, epsilon: True if abs(x-y) > epsilon else False
breakRelative = lambda x, y, percent: True if 100 * (x-y) / ((x + y) / 2) > percent else False
breakAbsRelative = lambda x, y, percent: True if 100 * abs(x - y) / ((x + y) / 2) > percent else False

def reconcileLists(l1, l2):
    if len(l1) != len(l2):
        print('Please enter lists of the same length! ')
    else:
        bvals = []

        for i in range(len(l1)):
            bvals.append(l1[i] == l2[i])

        return bvals


def reconcileListsMod(l1, l2, breakFn):
    if len(l1) != len(l2):
        print('Please enter lists of the same length! ')
    else:
        bvals = []

        for i in range(len(l1)):
            bvals.append(breakFn(l1[i], l2[i]))

        return bvals





