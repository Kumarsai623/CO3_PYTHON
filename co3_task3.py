import random
import string
import time
from collections import Counter

calls = [
    "seeds not received seeds delayed",
    "fertiliser price high",
    "seeds price high subsidy not received"
]

STOP = {"not", "high"}

# Count word frequencies
def frequencies(texts, stop):
    counts = {}

    for text in texts:
        words = text.lower().translate(
            str.maketrans("", "", string.punctuation)
        ).split()

        for word in words:
            if word not in stop:
                counts[word] = counts.get(word, 0) + 1

    return counts

# Find top k words
def top(counts, k):
    return sorted(
        counts.items(),
        key=lambda item: (-item[1], item[0])
    )[:k]

print("Top words:", top(frequencies(calls, STOP), 3))

# Group complaints by district
complaints = [
    ("Chennai", "Seeds not received"),
    ("Madurai", "Water supply problem"),
    ("Chennai", "Fertiliser price high"),
    ("Salem", "Crop damage")
]

district_groups = {}

for district, complaint in complaints:
    district_groups.setdefault(district, []).append(complaint)

print("\nComplaints by district:")

for district, items in district_groups.items():
    print(district, ":", items)

# Experimental investigation
sample_words = ["seeds", "price", "water", "seeds", "crop"]

print("\nCounter result:", Counter(sample_words))

# Compare dictionary counting and list.count()
for size in [1000, 10000, 100000]:
    data = [random.choice(sample_words) for _ in range(size)]

    start = time.perf_counter()
    result = {}

    for word in data:
        result[word] = result.get(word, 0) + 1

    dictionary_time = time.perf_counter() - start

    start = time.perf_counter()
    distinct = set(data)
    list_result = {word: data.count(word) for word in distinct}
    list_count_time = time.perf_counter() - start

    start = time.perf_counter()
    counter_result = Counter(data)
    counter_time = time.perf_counter() - start

    print("\nComplaints:", size)
    print("Dictionary time:", dictionary_time)
    print("List.count time:", list_count_time)
    print("Counter time:", counter_time)

# Edge cases
print("\nEmpty text:", frequencies([""], STOP))
print("Upper/lower case:", frequencies(
    ["SEEDS seeds Seeds"], STOP
))
print("Punctuation:", frequencies(
    ["Seeds, seeds! price."], STOP
))
