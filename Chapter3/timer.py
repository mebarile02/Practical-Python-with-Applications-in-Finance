'''
This module contains the Timer class, modified to work as a context manager.
'''


from time import time


class Timer(object):

    _display = 's'

    def __init__(self, msg):
        self._msg = msg

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, type, value, traceback):
        # print(type)
        # print(value)
        # print(traceback)
        self.end(self._display)

    def start(self):
        self._t1 = time()

    def end(self, display):
        tdiff = time() - self._t1
        self._lasttime = tdiff
        if self._display == 'm':
            print(str(self._msg) + ': ' + str(tdiff/60) + ' min(s)')
        elif self._display == 'h':
            print(str(self._msg) + ': ' + str(tdiff/3600) + ' hr(s)')
        else:
            print(str(self._msg) + ': ' + str(tdiff) + ' sec(s)')

    def lastTime(self):
        if self._display == 'm':
            print('The last timer result: ' + str(self._lasttime/60) + ' min(s)')
        elif self._display == 'h':
            print('The last timer result: ' + str(self._lasttime/3600) + ' hr(s)')
        else:
            print('The last timer result: ' + str(self._lasttime) + ' sec(s)')

    def configureTimerDisplay(self, display):
        self._display = display
        return self._display







