'''
This program tests the modified Timer class to ensure that it works as a Context Manager.
'''

from classFiles.Timer.timer import Timer


def main():

    with Timer('First Test Timer') as timer:
        print('This is the first test.  No configuration will produce time in seconds.')

    with Timer('Seconds Timer') as timer:
        timer.configureTimerDisplay('s')
        print('\nThis is a test for configuring display in seconds.')

    with Timer('Minutes Timer') as timer:
        timer.configureTimerDisplay('m')
        print('\nThis is a test for timer display in minutes.')

    with Timer('Hour Timer') as timer:
        timer.configureTimerDisplay('h')
        print('\nThis is a test for timer display in hours.')

    print('\nThis is a test to retrieve last timer result:')
    timer.lastTime()

if __name__ == '__main__':
    main()