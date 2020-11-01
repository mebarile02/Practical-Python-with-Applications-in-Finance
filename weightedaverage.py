'''
This module defines the war and wam functions.  These accept lists of tuples
of the form (term, rate, face)
'''

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

