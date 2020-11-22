'''
This module modifies the WAM and WAR functions to use reduce.  I include the original functions and compare
output.
'''

from functools import reduce

# This is the original WAR function.
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

# This is the modified WAR function using a lambda function and reduce.
def warMod(param):
    totamt = reduce(lambda total, face: total + face[2], param, 0)
    wavrt = reduce(lambda total, face_rate: total + (face_rate[1]*face_rate[2])/totamt, param, 0)
    return wavrt

# This is the original WAM function.
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

# This function adds two numbers.
def addNum(x, y):
    return x + y

# This is the modified WAM function using the addNum function, reduce and list comprehensions.
def wamMod(param):
    totamt = reduce(addNum, [tup[2] for tup in param])
    wavma = reduce(addNum, [tup[0]/12 * tup[2]/totamt for tup in param])
    return wavma

# Here, I test results.


def main():
    list = [(360, .09, 500000), (300, .07, 400000), (180, .01, 100000), (60, .0625, 150000)]

    print('Original WAR function: ' + str(war(list)))
    print('Modified WAR function: ' + str(warMod(list)))
    print('Original WAM function: ' + str(wam(list)))
    print('Modified WAM function: ' + str(wamMod(list)))


if __name__=='__main__':
    main()