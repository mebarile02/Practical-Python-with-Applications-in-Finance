'''
This module contains the Timer class.
'''


from time import time


class Timer(object):

    _display = 's'
    _lasttime = None
    _lastunit = 's'

    def __init__(self, display=None):
        self._t1 = None
        self._display = display if display is not None else Timer._display

    def start(self):
        if self._t1 is not None:
            print('Timer is already running!')
        else:
            self._t1 = time()

    def end(self):
        if self._t1 is None:
            print('The Timer is not running!')
        else :
            tdiff = time() - self._t1
            self._t1 = None
            Timer._lasttime = tdiff
            self._lastunit = self._display
            if self._display == 'm':
                print('The elapsed time: ' + str(tdiff/60) + ' min(s)')
            elif self._display == 'h':
                print('The elapsed time: ' + str(tdiff/3600) + ' hr(s)')
            else:
                print('The elapsed time: ' + str(tdiff) + ' sec(s)')

    def lastTime(self):
        if self._lasttime is not None:
            if self._lastunit == 'm':
                print('The last timer result: ' + str(Timer._lasttime/60) + ' min(s)')
            elif self._display == 'h':
                print('The last timer result: ' + str(Timer._lasttime/3600) + ' hr(s)')
            else:
                print('The last timer result: ' + str(Timer._lasttime) + ' sec(s)')
        else:
            print('The timer has not been run yet.')







