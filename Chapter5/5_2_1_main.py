"""
This module modifies the Timer to work as a decorator and validates.
"""

import time
from functools import wraps

def Timer(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        s = time.time()
        result = f(*args, **kwargs)
        e = time.time()
        print('Function {0}: {1} seconds'.format(f, e-s))
        return result

    return wrapped

# The Timer decorator is used on this function.
@Timer
def squareList(n):
    print([i ** 2 for i in range(n)])

# Here, we see the output expected from the Timer decorator.
def main():
    squareList(100)


if __name__ == '__main__':
    main()