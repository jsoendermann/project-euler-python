def is_palindrome_number(n):
    s = str(n)
    return s == s[::-1]

maximum = 0
for i in range(999, 0, -1):
    for j in range(999, 0, -1):
        if is_palindrome_number(i*j):
            if i*j > maximum:
                maximum = i*j
print(maximum)
