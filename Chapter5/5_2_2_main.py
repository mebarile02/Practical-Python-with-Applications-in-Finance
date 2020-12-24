'''
This module creates a decorator that memoizes the result o function and the tests.
'''

from functools import wraps
from classFiles.Timer.timerdec import Timer
import time

# Here, I use a dictionary with a string for the keys of str(args) + str(kwargs).
def memoize(f):
    cache = {}

    @wraps(f)
    def wrapped(*args,**kwargs):
        try:
            key = str(args) + str(kwargs)
            return cache[key]
        except KeyError:
            result = f(*args,**kwargs)
            cache[str(args) + str(kwargs)] = result
            return result

    return wrapped

@memoize
def fibonacci(n):
    if n < 2: return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci2(n):
    if n < 2: return n
    return fibonacci2(n - 1) + fibonacci2(n - 2)


def main():

    # Using the Timer decorator results in a timer output every time the function is called
    # in the recursive function, as opposed to the overall time it takes to run from start to finish,
    # so I just use the basic approach to measure performance difference.  It is clear that the
    # memoized function take significantly less time.

    t1 = time.time()
    fibonacci(25)
    t2 = time.time()
    print(f'Function time with memoization: {t2 - t1}')
    t3 = time.time()
    fibonacci2(25)
    t4 = time.time()
    print(f'Function time without memoization: {t4 - t3}')

if __name__ == '__main__':
    main()