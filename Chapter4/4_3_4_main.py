'''
This module writes a file to my desktop, per problem 4.3.4.
'''

def main():

    with open('/Users/michaelbarile/Desktop/testFile.txt','w') as tf:
        tf.write('1,10000,.02,180\n2,20000,.07,360\n3,150000,.04,300')

if __name__ == '__main__':
    main()