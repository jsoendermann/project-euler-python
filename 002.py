sum = 0
fib_last = 1
fib_current = 1
while fib_current <= 4000000:
    if fib_current % 2 == 0:
            sum += fib_current
    t = fib_current
    fib_current = fib_current + fib_last
    fib_last = t

print(sum)
