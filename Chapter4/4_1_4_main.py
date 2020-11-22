'''
This module defines and tests 8 functions for exercise 4.1.4.  Overall, f-Strings are cleanest.
'''

# This function uses format flags and integer input for age.
def sform1Int():
    name = input('Please enter your name: ')
    age = input('Please enter your age: ')
    country = input('Please enter your country: ')

    try:
        int(age)
    except:
        raise ValueError('Please enter age as an integer.\n')

    print('%s is %i years old and lives in %s.\n' % (name, int(age), country))

# This function uses format flags and float or integer input for age.
def sform1Flt():
    name = input('Please enter your name: ')
    age = input('Please enter your age: ')
    country = input('Please enter your country: ')

    try:
        float(age)
    except:
        raise ValueError('Please enter age as an integer or float.')

    print('%s is %.1f years old and lives in %s.\n' % (name, float(age), country))


# This function uses the format function, numeric placeholders, and integer input for age.
def sform2Int():

    name = input('Please enter your name: ')
    age = input('Please enter your age: ')
    country = input('Please enter your country: ')

    try:
        int(age)
    except:
        raise ValueError('Please enter age as an integer.\n')

    print('{0} is {1} years old and lives in {2}.\n'.format(name, age, country))

# This function uses the format function, numeric placeholders, and float or integer input for age.
def sform2Flt():
    name = input('Please enter your name: ')
    age = input('Please enter your age: ')
    country = input('Please enter your country: ')

    try:
        float(age)
    except:
        raise ValueError('Please enter age as an integer or float.\n')

    age = float(age)
    print('{0} is {1:.1f} years old and lives in {2}.\n'.format(name, age, country))

# This function uses the format function, keyword placeholders, and integer input for age.
def sform3Int():

    name = input('Please enter your name: ')
    age = input('Please enter your age: ')
    country = input('Please enter your country: ')

    try:
        int(age)
    except:
        raise ValueError('Please enter age as an integer.\n')

    print('{n} is {a} years old and lives in {c}.\n'.format(n=name,a=age,c=country))

# This function uses the format function, keyword placeholders, and float or integer input for age.
def sform3Flt():
    name = input('Please enter your name: ')
    age = input('Please enter your age: ')
    country = input('Please enter your country: ')

    try:
        float(age)
    except:
        raise ValueError('Please enter age as an integer or float.\n')

    age = float(age)
    print('{n} is {a:.1f} years old and lives in {c}.\n'.format(n=name, a=age, c=country))

# This function uses f-Strings and integer input for age.
def sform4Int():
    name = input('Please enter your name: ')
    age = input('Please enter your age: ')
    country = input('Please enter your country: ')

    try:
        int(age)
    except:
        raise ValueError('Please enter age as an integer.\n')

    print(f'{name} is {age} years old and lives in {country}.\n')

# This function uses f-Strings and float or integer input for age.
def sform4Flt():
    name = input('Please enter your name: ')
    age = input('Please enter your age: ')
    country = input('Please enter your country: ')

    try:
        float(age)
    except:
        raise ValueError('Please enter age as an integer or float.\n')

    age = float(age)
    print(f'{name} is {age:.1f} years old and lives in {country}.\n')


def main():

    # Here, we test each function in the order that they were defined above.

    try:
        sform1Int()
    except ValueError as ex:
        print(ex)

    try:
        sform1Flt()
    except ValueError as ex:
        print(ex)

    try:
        sform2Int()
    except ValueError as ex:
        print(ex)

    try:
        sform2Flt()
    except ValueError as ex:
        print(ex)

    try:
        sform3Int()
    except ValueError as ex:
        print(ex)

    try:
        sform3Flt()
    except ValueError as ex:
        print(ex)

    try:
        sform4Int()
    except ValueError as ex:
        print(ex)

    try:
        sform4Flt()
    except ValueError as ex:
        print(ex)


if __name__ == '__main__':
    main()