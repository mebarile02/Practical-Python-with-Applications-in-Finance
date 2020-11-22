from classFiles.Timer.timer import Timer

def main():

    # Below, we compare time using a list comprehension versus a generator expression.  We can see that
    # the generator expression takes less time.  This uses the modified Timer class as a context manager.
    # Per the lecture, the generator expression saves memory as well.

    with Timer('List Comprehension Timer'):
        lst1 = sum([x ** 2 for x in range(5000001)])

    with Timer('Generator Timer'):
        lst2 = sum(x ** 2 for x in range(5000001))


if __name__ == '__main__':
    main()
