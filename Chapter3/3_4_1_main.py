'''
This program opens a file, writes to it, and verifies that it is closed once the with statement exits.
'''


def main():
    with open("contextManager.txt", 'w') as f:
        f.write('This is a test.')

    print(f.closed)


if __name__=='__main__':
    main()