'''
This module creates a division function which provides an Exception message for division by zero or input
that is not float or int type.
'''


def divFunc(num, den):
    if not isinstance(num, (float, int)):
        raise ValueError('Please enter a number')
    elif not isinstance(den, (float, int)):
        raise ValueError('Please enter a number')
    elif den != 0:
        return float(num / den)
    else:
        raise ZeroDivisionError('Please enter a non-zero denominator.')


def main():

    # The following produces an Exception message for invalid input.

    try:
        print(divFunc('string', 1))
    except ValueError as ex:
        print(ex)
    except ZeroDivisionError as ex:
        print(ex)
    except Exception as ex:
        print(ex)

    try:
        print(divFunc(3, 0))
    except ValueError as ex:
        print(ex)
    except ZeroDivisionError as ex:
        print(ex)
    except Exception as ex:
        print(ex)

    try:
        print(divFunc(3, l))
    except ValueError as ex:
        print(ex)
    except ZeroDivisionError as ex:
        print(ex)
    except Exception as ex:
        print(ex)

    try:
        print(divFunc(3, 10))
    except ValueError as ex:
        print(ex)
    except ZeroDivisionError as ex:
        print(ex)
    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    main()