from functools import wraps
from Timer.timerdec import Timer

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