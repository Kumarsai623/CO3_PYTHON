import random
import time
import sys

readings = [3, 5, 9, 55, -60, 7, 1, 6, 52, 4]

# Method 1: For loop with append
valid_celsius = []
valid_fahrenheit = []

for c in readings:
    if -50 <= c <= 50:
        valid_celsius.append(c)
        valid_fahrenheit.append((c * 9 / 5) + 32)

# Method 2: List comprehension
clean_celsius = [c for c in readings if -50 <= c <= 50]

clean_fahrenheit = [
    (c * 9 / 5) + 32
    for c in readings if -50 <= c <= 50
]

# Method 3: map() and filter()
filtered = list(filter(lambda c: -50 <= c <= 50, readings))

mapped = list(map(
    lambda c: (c * 9 / 5) + 32,
    filtered
))

# Alarm minutes: temperature outside 2°C to 8°C
alarm_minutes = [
    minute for minute, temp in enumerate(readings, start=1)
    if -50 <= temp <= 50 and not (2 <= temp <= 8)
]

print("Valid Celsius:", valid_celsius)
print("Valid Fahrenheit:", valid_fahrenheit)
print("List comprehension:", clean_celsius)
print("Map and filter:", filtered)
print("Fahrenheit using map:", mapped)
print("Alarm minutes:", alarm_minutes)

# Dictionary comprehension
temperature_dict = {
    minute: temp for minute, temp in enumerate(readings, start=1)
    if -50 <= temp <= 50
}

# Set comprehension
temperature_set = {
    temp for temp in readings if -50 <= temp <= 50
}

print("Temperature dictionary:", temperature_dict)
print("Unique valid temperatures:", temperature_set)

# Experimental investigation
for size in [10000, 100000, 1000000]:
    data = [random.uniform(-60, 60) for _ in range(size)]

    start = time.perf_counter()
    loop_result = []

    for c in data:
        if -50 <= c <= 50:
            loop_result.append((c * 9 / 5) + 32)

    loop_time = time.perf_counter() - start

    start = time.perf_counter()
    comprehension_result = [
        (c * 9 / 5) + 32 for c in data if -50 <= c <= 50
    ]
    comprehension_time = time.perf_counter() - start

    start = time.perf_counter()
    map_result = list(map(
        lambda c: (c * 9 / 5) + 32,
        filter(lambda c: -50 <= c <= 50, data)
    ))
    map_time = time.perf_counter() - start

    print("\nReadings:", size)
    print("Loop time:", loop_time)
    print("Comprehension time:", comprehension_time)
    print("Map/filter time:", map_time)
    print("All results equal:", 
          loop_result == comprehension_result == map_result)

# Memory comparison
list_data = [x for x in range(10000)]
generator_data = (x for x in range(10000))

print("\nList memory:", sys.getsizeof(list_data))
print("Generator memory:", sys.getsizeof(generator_data))

# Edge cases
all_valid = [3, 4, 5]
all_invalid = [60, -70, 100]

print("All valid:", [x for x in all_valid if -50 <= x <= 50])
print("All invalid:", [x for x in all_invalid if -50 <= x <= 50])
