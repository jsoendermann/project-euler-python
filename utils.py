from math import sqrt

def sum_of_digits(n):
    str_ = str(n)
    list_ = list(str_)
    int_list = map(int, list_)
    sum_ = sum(int_list)
    return sum_

known_factors = {}
def factorize(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            factors = [i] + factorize(n // i)
            known_factors[n] = factors
            return factors
        i += 1
    known_factors[n] = [n]
    return [n]

def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def next_prime(n):
    n += 1
    while not is_prime(n):
        n += 1
    return n

def primes():
    p = 2
    while True:
        yield p
        p = next_prime(p)

def triangle_numbers():
    i = 1
    n = 0
    while True:
        n += i
        i += 1
        yield n

def fibonacci_numbers():
    i = 1
    j = 1
    while True:
        yield i
        n = i + j
        i = j
        j = n
