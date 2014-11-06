from math import sqrt
from itertools import groupby

prime_factors_cache = {}
def factorise(n):
    if n in prime_factors_cache:
        return prime_factors_cache[n]

    divisor = 2
    rest = n
    factors = []

    while divisor <= int(sqrt(n)):
        if rest % divisor == 0:
            factors.append(divisor)
            rest /= divisor
            if rest in prime_factors_cache:
                factors.extend(prime_factors_cache[rest])
                prime_factors_cache[n] = factors
                return factors
            divisor = 2
        else:
            divisor += 1
    if rest > 1:
        factors.append(int(rest))
    prime_factors_cache[n] = factors
    return factors

def number_of_factors(n):
    prime_factors = factorise(n) 
    grouped_factors = [list(g) for k, g in groupby(prime_factors)]
    count = 1
    for factor_group in grouped_factors:
        count *= len(factor_group) + 1
    return count

def triangle_numbers():
    i = 1
    n = 0
    while True:
        n += i
        i += 1
        yield n

for t in triangle_numbers():
    n = number_of_factors(t)
    if n > 500:
        print(t)
        break
