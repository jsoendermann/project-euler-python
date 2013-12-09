def square(n):
    return n*n

sum_squares = sum([x*x for x in range(1,101)])
square_sum = square(sum([x for x in range(1,101)]))

print(square_sum - sum_squares)
