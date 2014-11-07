from itertools import islice
from utils import primes

# https://docs.python.org/2/library/itertools.html#recipes
def nth(iterable, n, default=None):
    "Returns the nth item or a default value"
    return next(islice(iterable, n, None), default)

n = nth(primes(), 10000)

print(n)
