from math import sqrt

def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

primes_found = 0
n = 1
while primes_found != 10001:
    n += 1
    if is_prime(n):
        primes_found += 1
    
print(n)
