'''
This module creates a list of 10 names and prints them in the desired format by using enumerate.
'''


def main():

    lnames = ['Mike', 'Bob', 'Ted', 'Sam', 'Sarah', 'Billy', 'Jill', 'Gloria', 'Tom', 'Karen']

    for i, name in enumerate(lnames, 1):
        print('Name ' + str(i) + ': ' + str(name))


if __name__ == '__main__':
    main()