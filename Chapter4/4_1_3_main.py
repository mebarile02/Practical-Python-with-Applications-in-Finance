'''
This module addresses problem 4.1.3
'''


def main():
    lst = ['C:', 'Users', 'Me', 'Desktop', 'MyTable.csv']
    fp = '/'.join(lst)
    print(f'This is the original path: {fp}')
    lst.insert(4, 'NewFolder')
    fp = '/'.join(lst)
    print(f'This is the new path: {fp}')


if __name__ == '__main__':
    main()