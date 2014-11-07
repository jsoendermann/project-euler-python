from math import sqrt
from functools import reduce
from operator import mul

two_million = 2*1000*1000
sieve = [True] * two_million

n = 2
while n < sqrt(two_million):
    while sieve[n] != True:
        n += 1
    m = 2
    while n * m < two_million:
        sieve[n * m] = False
        m += 1
    n += 1

print(sum([n for n in range(2, two_million) if sieve[n]]))
