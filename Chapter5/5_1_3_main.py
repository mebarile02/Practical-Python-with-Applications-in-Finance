'''
This module addresses problems for 5.1.3.
'''

import datetime

def main():

    # The user is prompted to enter datetime with a given format.
    ui = input('Enter a datetime with the following format: YYYY month dd  hh:mm:ss:ffffff AM/PM ')

    d = datetime.datetime.strptime(ui, '%Y %B %d %I:%M:%S:%f %p')

    # This will produce the final intended format.
    dd = d.strftime('%Y %B %d %I:%M:%S:%f %p')

    print(dd)


if __name__ == '__main__':
    main()