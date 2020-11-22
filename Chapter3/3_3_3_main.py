'''
This module contains a factorial function and provides exception handling for invalid input.
'''


def fact(n):

    if not isinstance(n, int) or n < 0:
        raise ValueError('Please enter a nonnegative integer. ')
    else:
        i = 1
        for j in range(1, n + 1):
            i *= j
        return i


def main():

    try:
        print(fact('name'))
    except ValueError as ex:
        print(ex)
    except Exception as ex:
        print(ex)

    try:
        print(fact(test))
    except ValueError as ex:
        print(ex)
    except Exception as ex:
        print(ex)

    try:
        print(fact(-1000))
    except ValueError as ex:
        print(ex)
    except Exception as ex:
        print(ex)

    try:
        print(fact(1.78))
    except ValueError as ex:
        print(ex)
    except Exception as ex:
        print(ex)

    try:
        print(fact(6))
    except ValueError as ex:
        print(ex)
    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    main()