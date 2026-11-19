import copy
import sys
import time

rows, cols = 3, 4

# Incorrect grid: all rows refer to the same list
bad = [[0] * cols] * rows
bad[0][1] = 7

# Correct grid: each row is a separate list
good = [[0 for _ in range(cols)] for _ in range(rows)]
good[0][1] = 7

print("bad :", bad)
print("good:", good)
print(bad[0] is bad[1], good[0] is good[1])

# Tuples as dictionary keys
stops = {
    (13.0827, 80.2707): "Chennai Central",
    (13.0418, 80.2341): "T. Nagar"
}

print(stops[(13.0418, 80.2341)])

# Aliasing
original = [[1, 2], [3, 4]]
alias = original
alias[0][0] = 99
print("Aliasing:", original)

# Shallow copy
shallow = copy.copy(original)
shallow[0][1] = 88
print("Shallow copy:", original)

# Deep copy
deep = copy.deepcopy(original)
deep[0][0] = 55
print("Deep copy:", original)
print("Independent deep copy:", deep)

# Tuple unpacking
coordinates = [(13.08, 80.27), (13.04, 80.23)]

for latitude, longitude in coordinates:
    print("Latitude:", latitude, "Longitude:", longitude)

# List and tuple memory comparison
values_list = list(range(1000000))
values_tuple = tuple(range(1000000))

print("List memory:", sys.getsizeof(values_list))
print("Tuple memory:", sys.getsizeof(values_tuple))

# Creation and indexing time
for label, creator in [("List", list), ("Tuple", tuple)]:
    start = time.perf_counter()
    data = creator(range(100000))
    creation_time = time.perf_counter() - start

    start = time.perf_counter()
    item = data[50000]
    indexing_time = time.perf_counter() - start

    print(label, "creation:", creation_time)
    print(label, "indexing:", indexing_time)

# A list inside a tuple can still be modified
example = ([10, 20], 30)
example[0].append(40)
print("Tuple containing a list:", example)

# A list cannot be used as a dictionary key
try:
    test = {[13.0418, 80.2341]: "T. Nagar"}
except TypeError as error:
    print("Error:", error)
