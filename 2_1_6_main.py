'''
This module was originally used to test the Asset class functionality and
the currentVal method described in 2.1.6d.  After the modification required in
exercise 2.2.6, this will produce a NotImplementedError, as a warning to the
user that we are not meant to instantiate Assets directly.  We "abstract" the Asset
class, as described in the homework.
'''


from classFiles.asset import Asset


def main():

    # We validate the currentVal method of the Asset class here.

    a = Asset(100000, .20)

    # After the modifications made in exercise 2.2.6, this will now throw
    # a Not Implemented Error.
    print('Validation of currentVal method: ')
    for i in range(13):
        print(a.currentVal(i))


if __name__ == '__main__':
    main()