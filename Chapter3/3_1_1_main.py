'''
This module creates a lambda function to calculate the hypotenuse of a right triangle.
'''


hypotenuse = lambda base, height:  (base ** 2 + height ** 2) ** (1/2)

def main():

    print('This is the length of the hypotenuse of a right triangle with base 4 and height 8: '
          + str(hypotenuse(4, 8)) + '\n')

    print('This is the length of the hypotenuse of a right triangle with base 3 and height 6: '
          + str(hypotenuse(3, 6)))

if __name__=='__main__':
    main()