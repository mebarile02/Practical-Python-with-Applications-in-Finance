'''
This module addresses the problem in 6.1.1.  The Excel file with the exported data is in the 6.1.1 subfolder.
'''


import random
import csv

def main():
    random.seed(1)

    # The random numbers from given distributions are created.
    fields = ['Uniform', 'Normal', 'Lognormal']
    rvar = []
    for i in range(200000):
        lst = []
        lst.append(random.uniform(1, 20))
        lst.append(random.normalvariate(10, 7))
        lst.append(random.lognormvariate(1, 0.5))
        rvar.append(lst)

    # Here, the data is exported to a csv file with three columns and 200000 rows.
    with open('/Users/michaelbarile/Desktop/test.csv', 'w') as fp:
        write = csv.writer(fp)
        write.writerow(fields)
        write.writerows(rvar)


if __name__ == '__main__':
    main()
