'''
This module defines the war and wam functions.  These accept lists of tuples
of the form (term, rate, face)
'''

from functools import reduce

def war(param):
    amt = []
    for i in range(len(param)):
        amt.append(param[i][2])
    totamt = sum(amt)
    weights = []
    for i in range(len(param)):
        weights.append((param[i][2] / totamt, param[i][1]))
    wavrt = 0
    for i in range(len(weights)):
        wavrt = wavrt + weights[i][1] * weights[i][0]
    return wavrt


def wam(param):
    amt = []
    for i in range(len(param)):
        amt.append(param[i][2])
    totamt = sum(amt)
    weights = []
    for i in range(len(param)):
        weights.append((param[i][2] / totamt, param[i][0] / 12))
    wavma = 0
    for i in range(len(weights)):
        wavma = wavma + weights[i][1] * weights[i][0]
    return wavma

# This is the modified WAR function using a lambda function and reduce.
def warRed(param):
    totamt = reduce(lambda total, face: total + face[2], param, 0)
    wavrt = reduce(lambda total, face_rate: total + (face_rate[1]*face_rate[2])/totamt, param, 0)
    return wavrt

# This function adds two numbers.
def addNum(x, y):
    return x + y

# This is the modified WAM function using the addNum function, reduce and list comprehensions.
def wamRed(param):
    totamt = reduce(addNum, [tup[2] for tup in param])
    wavma = reduce(addNum, [tup[0]/12 * tup[2]/totamt for tup in param])
    return wavma
