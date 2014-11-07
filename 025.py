from utils import fibonacci_numbers

for i, f in enumerate(fibonacci_numbers()):
    if len(str(f)) >= 1000:
        print(i + 1)
        break
