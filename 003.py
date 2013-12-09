def is_prime(n):
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def next_prime(n):
    n += 1
    while not is_prime(n):
        n += 1
    return n

def factorize(n):
    factors = []
    i = 2
    while True:
        while n % i == 0:
            factors.append(i)
            n = n/i
            if n == 1:
                return factors

        i = next_prime(i)


print(factorize(600851475143)[-1])
