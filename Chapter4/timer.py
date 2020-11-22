'''
This module contains the Timer class, modified to work as a context manager.
'''

import logging
from time import time


class Timer(object):
    logging.getLogger().setLevel(logging.INFO)

    _display = 's'
    _warnThreshold = 60

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
        if tdiff > self._warnThreshold:
            if self._display == 'm':
                logging.warning('{0}: {1} min(s)'.format(self._msg, tdiff/60))
            elif self._display == 'h':
                logging.warning('{0}: {1} hr(s)'.format(self._msg, tdiff/3600))
            else:
                logging.warning('{0}: {1} sec(s)'.format(self._msg, tdiff))
        else:
            if self._display == 'm':
                logging.info('{0}: {1} min(s)'.format(self._msg, tdiff/60))
            elif self._display == 'h':
                logging.info('{0}: {1} hr(s)'.format(self._msg, tdiff/3600))
            else:
                logging.info('{0}: {1} sec(s)'.format(self._msg, tdiff))


    def lastTime(self):
        if self._display == 'm':
            logging.info('The last timer result: {0} min(s)'.format(self._lasttime/60))
        elif self._display == 'h':
            logging.info('The last timer result: {0} hr(s)'.format(self._lasttime/3600))
        else:
            logging.info('The last timer result: {0} sec(s)'.format(self._lasttime))

    def configureTimerDisplay(self, display):
        self._display = display
        return self._display







