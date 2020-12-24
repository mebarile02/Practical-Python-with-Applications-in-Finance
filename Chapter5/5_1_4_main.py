'''
This module creates the "dat calculator" program described in problem 5.1.4.
'''

import datetime

def main():

    # The user enters a datetime with the specified format.
    ui = input('Enter a datetime with the following format: YYYY-mm-dd  hh:mm:ss:ffffff  ')

    # The user enters a time delta with a specified format, per problem description.
    uidelt = input('Enter delta in the format: hh:mm:ss:ffffff  ')

    d = datetime.datetime.strptime(ui, '%Y-%m-%d %H:%M:%S:%f')

    # This piece takes care of the leading minus sign, depending on how delta is intended.
    if uidelt[0] == '-':
        uidelt = uidelt[1:]
        sgn = -1
    else:
        sgn = 1

    # The user entered delta is split at :"
    dlist = uidelt.split(':')

    # This will produce the new datetime.
    d1 = d + (sgn) * datetime.timedelta(hours=float(dlist[0]),minutes=float(dlist[1]),seconds=float(dlist[2]),
                                        microseconds=float(dlist[3]))

    print(f'\nThe original datetime: {d}\n')
    print(f'The new datetime: {d1}\n')



if __name__ == '__main__':
    main()

