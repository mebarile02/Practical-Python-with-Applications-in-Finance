'''
This module addresses the problem in 6.1.2, printing a histogram to screen for the
three distribution types.
'''

import random
from collections import Counter

# Here, I have created a normalize functions that takes moxold, minold and freq as parameters.  Output is
# rounded to nearest integer, so this will produce integers between 1 and 100.
def normalize(maxold, minold, freq):
    return round(((100 - 1)/(maxold - minold)) * (freq - maxold) + 100)

def main():
    random.seed(1)


    uni = []
    for i in range(200000):
        uni.append(random.uniform(1,20))

    # Here, we round the results of above.
    unirnd = [round(i) for i in uni]
    # We then use Counter and dictionary to get key:value pairs, where the key is an element
    # from unirnd and value is the element's frequency in unirnd.
    freq = Counter(unirnd)
    freq = dict(freq)
    maxold = max(list(freq.values()))
    minold = min(list(freq.values()))
    # Here, we apply the normalize function to each value in the key value pair, to scale frequencies
    # to 1-100.
    newdict = {key:normalize(maxold,minold,value) for (key,value) in freq.items()}
    lstTuple = list(newdict.items())
    # We then sort a list of tuples for final output.
    sortlstTuple = sorted(lstTuple, key=lambda tup: tup[0])

    print('******************************** Uniform ******************************')
    for i in range(len(sortlstTuple)):
        print(str(sortlstTuple[i][0]) + sortlstTuple[i][1] * '-')

    # The remaining two distributions follow the same logic ad above.
    norm = []
    for i in range(200000):
        norm.append(random.normalvariate(10, 7))

    nrmrnd = [round(i) for i in norm]
    freq = Counter(nrmrnd)
    freq = dict(freq)
    maxold = max(list(freq.values()))
    minold = min(list(freq.values()))
    newdict = {key:normalize(maxold,minold,value) for (key,value) in freq.items()}
    lstTuple = list(newdict.items())
    sortlstTuple = sorted(lstTuple, key=lambda tup: tup[0])

    print('******************************** Normal ******************************')
    for i in range(len(sortlstTuple)):
        print(str(sortlstTuple[i][0]) + sortlstTuple[i][1] * '-')


    lognorm = []
    for i in range(2000000):
        lognorm.append(random.lognormvariate(1, 0.5))

    logrnd = [round(i) for i in lognorm]
    freq = Counter(logrnd)
    freq = dict(freq)
    maxold = max(list(freq.values()))
    minold = min(list(freq.values()))
    newdict = {key:normalize(maxold,minold,value) for (key,value) in freq.items()}
    lstTuple = list(newdict.items())
    sortlstTuple = sorted(lstTuple, key=lambda tup: tup[0])

    print('******************************** Lognormal ******************************')
    for i in range(len(sortlstTuple)):
        print(str(sortlstTuple[i][0]) + sortlstTuple[i][1] * '-')


if __name__ == '__main__':
    main()