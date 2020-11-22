'''
This module creates a division function which provides an Exception message for division by zero.
'''

def divFunc(num, den):
    if den != 0:
        return float(num / den)
    else:
        raise ZeroDivisionError('Please enter a non-zero denominator.')

def main():

    try:
        print(divFunc(1, 0))
    except ZeroDivisionError as ex:
        print('Zero Division Error: ' + str(ex))
    except Exception as ex:
        print('Exception: ' + str(ex))

    try:
        print(divFunc(l, 3))
    except ZeroDivisionError as ex:
        print(ex)
    except Exception as ex:
        print('Exception: ' + str(ex))


if __name__ == '__main__':
    main()
