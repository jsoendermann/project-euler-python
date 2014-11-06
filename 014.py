def collatz_squence(n):
    yield n
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        yield n

max_number = 0
max_length = 0
for n in range(1, 1000000):
    length_of_sequence = len(list(collatz_squence(n)))
    if length_of_sequence > max_length:
        max_number = n
        max_length = length_of_sequence
        
print(max_number)
