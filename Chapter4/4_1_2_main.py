'''
This module addressed problem 4.1.2.
'''

def main():

    f = '/Users/michaelbarile/Desktop/MyTable.csv'
    vr = f.split('/')[-1]
    print(f'This is the original string (for Mac): {f}\n')
    print(f'This is the filename with the extension from the path: {vr}\n')
    vr2 = f.split('.')[-1]
    print(f'This is the extension: {vr2}\n')
    l = f.split('/')
    l.insert(4, 'NewFolder')
    f = '/'.join(l)
    print(f'This is the path with the new folder added: {f}')



if __name__ == '__main__':
    main()