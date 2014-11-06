def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n - 1)


def n_over_k(n, k):
    return fac(n)/(fac(n - k) * fac(k))

print(n_over_k(40, 20))
