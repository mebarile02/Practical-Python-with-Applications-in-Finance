'''
This module addresses problems from 5.1.2.
'''

import datetime

def main():

    # The user is prompted to enter date and time with specific format.
    ui = input('Enter a datetime with the following format: YYYY-mm-dd  hh:mm:ss:ffffff  ')

    # Here, user info is output to screen.
    d = datetime.datetime.strptime(ui, '%Y-%m-%d %H:%M:%S:%f')
    print(d)


if __name__ == '__main__':
    main()