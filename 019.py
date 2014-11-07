from datetime import datetime, timedelta

FROM = datetime(1901, 1, 1)
TO = datetime(2001, 1, 1)

def days_between(from_, to):
    while from_ < to:
        yield from_
        from_ += timedelta(days=1)

counter = 0

for day in days_between(FROM, TO):
    if day.day == 1 and day.weekday() == 6:
        counter += 1

print(counter)
