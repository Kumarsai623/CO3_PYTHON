import random
import time

# Generate rainfall readings for 365 days
readings = [round(random.uniform(0, 30), 2) for _ in range(365)]

# Weekly rainfall totals
weekly_totals = []

for i in range(0, len(readings), 7):
    week = readings[i:i + 7]
    weekly_totals.append(round(sum(week), 2))

# Wettest and driest weeks
wettest_week = weekly_totals.index(max(weekly_totals)) + 1
driest_week = weekly_totals.index(min(weekly_totals)) + 1

# Naive moving average
def naive_average(data):
    averages = []

    for i in range(len(data) - 6):
        total = sum(data[i:i + 7])
        averages.append(total / 7)

    return averages

# Running-sum moving average
def running_average(data):
    averages = []

    if len(data) < 7:
        return averages

    total = sum(data[:7])
    averages.append(total / 7)

    for i in range(7, len(data)):
        total = total - data[i - 7] + data[i]
        averages.append(total / 7)

    return averages

# Dry days
dry_days = [i + 1 for i, value in enumerate(readings) if value == 0]

print("Total readings:", len(readings))
print("Number of weeks:", len(weekly_totals))
print("Wettest week:", wettest_week)
print("Driest week:", driest_week)
print("First 5 weekly totals:", weekly_totals[:5])
print("Number of moving averages:", len(running_average(readings)))
print("Dry days:", dry_days)

# Experimental investigation
for size in [365, 36500, 365000]:
    data = [random.uniform(0, 30) for _ in range(size)]

    start = time.perf_counter()
    naive_average(data)
    naive_time = time.perf_counter() - start

    start = time.perf_counter()
    running_average(data)
    running_time = time.perf_counter() - start

    print("\nReadings:", size)
    print("Naive time:", naive_time)
    print("Running-sum time:", running_time)

# Edge cases
print("\nEmpty list:", running_average([]))
print("Short list:", running_average([2, 3, 4]))
