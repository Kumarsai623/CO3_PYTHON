import random
import time

ai_elective = {
    "192311001", "192311004", "192311007", "192311009"
}

iot_elective = {
    "192311002", "192311004", "192311009", "192311010"
}

all_students = {
    f"1923110{i:02d}" for i in range(1, 11)
}

# Set operators
both = ai_elective & iot_elective
exactly_one = ai_elective ^ iot_elective
neither = all_students - (ai_elective | iot_elective)

print("clash :", sorted(both))
print("exactly one:", sorted(exactly_one))
print("neither :", sorted(neither))

# Set methods
both_method = ai_elective.intersection(iot_elective)
one_method = ai_elective.symmetric_difference(iot_elective)
neither_method = all_students.difference(
    ai_elective.union(iot_elective)
)

print("\nMethod results:")
print(both_method == both)
print(one_method == exactly_one)
print(neither_method == neither)

# Remove duplicate registrations
registrations = [
    "192311001", "192311004", "192311001", "192311007"
]

unique_registrations = set(registrations)
print("\nUnique registrations:", sorted(unique_registrations))

# Membership timing
for size in [10000, 100000, 1000000]:
    data = list(range(size))
    data_set = set(data)
    target = size - 1

    start = time.perf_counter()
    target in data
    list_time = time.perf_counter() - start

    start = time.perf_counter()
    target in data_set
    set_time = time.perf_counter() - start

    print("\nSize:", size)
    print("List membership time:", list_time)
    print("Set membership time:", set_time)

# Nested loops and set intersection
a = list(range(1000))
b = list(range(500, 1500))

start = time.perf_counter()
common_nested = []

for x in a:
    for y in b:
        if x == y:
            common_nested.append(x)

nested_time = time.perf_counter() - start

start = time.perf_counter()
common_set = set(a) & set(b)
set_time = time.perf_counter() - start

print("\nNested-loop time:", nested_time)
print("Set intersection time:", set_time)
print("Same result:", set(common_nested) == common_set)

# Edge cases
print("\nEmpty electives:", set() & set())
print("Identical electives:", {1, 2} & {1, 2})
