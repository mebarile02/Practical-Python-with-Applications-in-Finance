'''
This module creates a list of 1000 numbers, converts it to an iterator and iterates through it
'''

def main():

    lst = [i for i in range(1000)]

    print('verifying list type: ' + str(type(lst)))
    li = iter(lst)
    print('verifying list_iterator type: ' + str(type(li)))

    for i in range(1000):
        print(next(li))

if __name__=='__main__':
    main()