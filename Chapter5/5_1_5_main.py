'''
This module creates a date differential program, per problem 5.1.5.
'''

import datetime
import math

def main():

    # The user enter input in specified format.
    dtime = input('Please enter a datetime in the following format: YYYY-mm-dd hh:mm:ss:ffffff ')
    dtime1 = input('Please enter another datetime in the following format: YYYY-mm-dd hh:mm:ss:ffffff ')

    d = datetime.datetime.strptime(dtime, '%Y-%m-%d %H:%M:%S:%f')
    d1 = datetime.datetime.strptime(dtime1, '%Y-%m-%d %H:%M:%S:%f')

    # The date difference is calculated.
    df = d - d1

    # The date difference is converted to microseconds, and then total days, hours, etc are calculated.
    tmicro = abs(df.days * 86400000000 + df.seconds * 1000000 + df.microseconds)
    tdays = tmicro/86400000000
    thours = tmicro/3600000000
    tmins = tmicro/60000000
    tsecs = tmicro/1000000

    # The total time is displayed in different units.
    print(f'\nTotal time difference in days: {tdays}\n')
    print(f'Total time difference in hours: {thours}\n')
    print(f'Total time difference in minutes: {tmins}\n')
    print(f'Total time difference in seconds: {tsecs}\n')
    print(f'Total time difference in microseconds: {tmicro}\n')

    # Frac/whole manipulation is used to get the result into a displayable form.
    fracd, wholed = math.modf(tdays)
    wholeDays = wholed
    hours = 24 * fracd
    frach, wholeh = math.modf(hours)
    wholeHours = wholeh
    minutes = 60 * frach
    fracm, wholem = math.modf(minutes)
    wholeMinutes = wholem
    seconds = 60 * fracm
    fracs, wholes = math.modf(seconds)
    wholeSeconds = wholes
    microseconds = 1000000 * fracs

    lst = [(int(wholeDays),'days'), (int(wholeHours),'hours'), (int(wholeMinutes),'minutes'),
           (int(wholeSeconds),'seconds'), (round(microseconds,2), 'microseconds')]

    lst2 = []
    for val in lst:
        if val[0] != 0:
            lst2.append(f'{val[0]} {val[1]}')
        else:
            pass

    # A loop is used to handle punctuation and the possibility of some units having 0 value.
    if len(lst2) == 1:
        print(f'The difference is {lst2[0]}.')
    else:
        for i in range(len(lst2)):
            if i == 0:
                print(f'The difference is {lst2[0]}, ',end='')
            elif 0 < i < len(lst2) - 1:
                print(f'{lst2[i]}, ', end='')
            else:
                print(f'and {lst2[i]}.', end='')


if __name__ == '__main__':
    main()