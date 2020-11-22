'''
This module tests the Timer class for functionality.
'''

from classFiles.timer import Timer


def main():

    # Here, I initialize a timer object and call the start method, run a loop, call the
    # call the end method, and then call the lastTime method.

    t = Timer()
    t.start()
    var = 0
    for i in range(101):
        var += 1
    print(i)
    t.end()
    t.lastTime()
    t.end()

    # Here, I verify that you will receive a message if calling start while timer is
    # already running.
    t.start()
    t.start()
    t.end()

    # Here, I verify that you will receive a message if the calling end when the timer
    # is not running.
    t.end()

    # Here, I verify that the timer will produce results when the unit is changed
    # to minutes, as opposed to the default, second.

    t = Timer('m')
    t.start()
    var = 0
    for i in range(100001):
        var += 1
    print(i)
    t.end()
    t.lastTime()


if __name__ == '__main__':
    main()
