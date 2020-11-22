'''
This module opens the files created in 4.3.4 and prints to screen, per problem 4.3.5.
'''

def main():

    with open('/Users/michaelbarile/Desktop/testFile.txt') as tf:
        for line in tf:
            print(line)

if __name__ == '__main__':
    main()