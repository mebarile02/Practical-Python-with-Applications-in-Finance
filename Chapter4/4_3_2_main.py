'''
This file searches my computer for all files with extension py, per problem 4.3.2.
'''

import os


def main():

    for root, dirs, files in os.walk('/Users/michaelbarile/Desktop'):
        for file in files:
            if file.endswith('.py'):
                print(file)


if __name__ == '__main__':
    main()
