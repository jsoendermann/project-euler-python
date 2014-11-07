from itertools import groupby
from utils import triangle_numbers, factorize

def number_of_factors(n):
    prime_factors = factorize(n) 
    grouped_factors = [list(g) for k, g in groupby(prime_factors)]
    count = 1
    for factor_group in grouped_factors:
        count *= len(factor_group) + 1
    return count

for t in triangle_numbers():
    n = number_of_factors(t)
    if n > 500:
        print(t)
        break
