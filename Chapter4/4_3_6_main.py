'''
This module appends to the file created in 4.3.5 and then prints the results to screen, per problem
4.3.6.
'''


def main():

    with open('/Users/michaelbarile/Desktop/testFile.txt', 'a') as tf:
        tf.write('\n4,140000,.02,200')

    with open('/Users/michaelbarile/Desktop/testFile.txt') as tf:
        for line in tf:
            print(line)


if __name__ == '__main__':
    main()