from datetime import datetime, timedelta

counter = 0
d = datetime(1901, 1, 1)

while d <= datetime(2000, 12, 31):
    if d.day == 1 and d.weekday() == 6:
        counter += 1
    d = d + timedelta(days=1)

print(counter)
