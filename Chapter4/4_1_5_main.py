'''
This module tests the Timer class after it was modified to use the format function for print statements.
'''

from classFiles.Timer.timer import Timer


def main():

    # Here, display is configured for minutes.
    with Timer('testTimer') as timer:
        timer.configureTimerDisplay('m')
        print('This is a test')

    timer.lastTime()

    # Here, display is configured for seconds.
    with Timer('testTimer2') as timer:
        timer.configureTimerDisplay('s')
        print('This is another test.')

    timer.lastTime()


if __name__ == '__main__':
    main()