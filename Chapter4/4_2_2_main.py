'''
This module tests the modified Timer class, which uses an info level logging statement, instead of
a print statement, and includes a class level warnThreshold variable.  If the timer exceeds 60 seconds, a
warn level log statement is produced instead of an info level log statement.
'''


from classFiles.Timer.timer import Timer


def main():

    # This example is pretty contrived, but it takes over 60 seconds to complete and is
    # good for verifying the threshold warning message.
    with Timer('testTimer') as timer:
        lst = [i ** 2 for i in range(100000000)]
        print(lst)
        print(lst)


if __name__ == '__main__':
    main()