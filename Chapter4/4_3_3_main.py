'''
This module searches my computer for all pdf files with 'gr,' 'GR', 'gR' or 'Gr' in the name,
per problem 4.3.3.
'''

import os


def main():

    # You can see here that .find() is used to filter out pdf files without the relevant substring in
    # the name.
    for root, dirs, files in os.walk('/Users/michaelbarile/Desktop'):
        for file in files:
            if file.endswith('.pdf'):
                if file.lower().find('gr') != -1:
                    print(file)


if __name__ == '__main__':
    main()