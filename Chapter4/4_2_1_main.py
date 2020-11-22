'''
This module tests the modified Timer class, which uses an info level logging statement, instead of
a print statement.
'''


from classFiles.Timer.timer import Timer


def main():

    with Timer('testTimer') as timer:
        lst = [i ** 2 for i in range(100)]
        print(lst)


if __name__ == '__main__':
    main()