'''
This module tests the reconcileLists function.
'''

from functions.reconcilelists import reconcileLists

def main():

    lst1 = [1, 2, 900, 12, 201, 90, 812, 345, 723, 1001]
    lst2 = [90, 2, 123, 12, 201, 90, 813, 345, 724, 1000]

    print(reconcileLists(lst1, lst2))


if __name__=='__main__':
    main()