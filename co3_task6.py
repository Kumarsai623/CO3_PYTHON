import time

# Railway timetable
trains = {
    "12601": {
        "name": "Chennai Express",
        "stops": [
            ("Chennai", "06:00", "06:10"),
            ("Katpadi", "08:00", "08:05"),
            ("Bengaluru", "10:30", "10:40")
        ],
        "days": {"Mon", "Wed", "Fri"}
    },

    "12602": {
        "name": "City Express",
        "stops": [
            ("Chennai", "07:00", "07:15"),
            ("Katpadi", "09:00", "09:05"),
            ("Coimbatore", "12:00", "12:10")
        ],
        "days": {"Tue", "Thu", "Sat"}
    },

    "12603": {
        "name": "Southern Express",
        "stops": [
            ("Chennai", "08:00", "08:10"),
            ("Salem", "11:00", "11:05"),
            ("Coimbatore", "13:00", "13:10")
        ],
        "days": {"Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"}
    },

    "12604": {
        "name": "Metro Express",
        "stops": [
            ("Chennai", "09:00", "09:10"),
            ("Katpadi", "11:00", "11:05"),
            ("Bengaluru", "13:00", "13:10")
        ],
        "days": {"Sun"}
    },

    "12605": {
        "name": "Coastal Express",
        "stops": [
            ("Chennai", "10:00", "10:10"),
            ("Salem", "12:00", "12:05"),
            ("Coimbatore", "14:00", "14:10")
        ],
        "days": {"Mon", "Fri"}
    }
}

# Create station index
station_index = {}

for train_no, details in trains.items():
    for station, arrival, departure in details["stops"]:
        station_index.setdefault(station, []).append(train_no)

# Search trains
def find_trains(station, day):
    results = []

    for train_no in station_index.get(station, []):
        train = trains[train_no]

        if day in train["days"]:
            for stop in train["stops"]:
                if stop[0] == station:
                    results.append(
                        (train_no, train["name"], stop[2])
                    )

    return sorted(results, key=lambda x: x[2])

station = "Katpadi"
day = "Mon"

print("Trains at", station, "on", day)

for train_no, name, departure in find_trains(station, day):
    print(train_no, name, departure)

# Print complete timetable
print("\nComplete Timetable:")

for train_no, details in trains.items():
    print("\nTrain:", train_no, details["name"])
    print("Running days:", sorted(details["days"]))

    for station, arrival, departure in details["stops"]:
        print(station, arrival, departure)

# Performance comparison
for size in [100, 1000, 10000]:
    timetable = {}
    index = {}

    for i in range(size):
        train_no = str(i)
        station_name = "Station" + str(i % 100)

        timetable[train_no] = {
            "stops": [
                (station_name, "10:00", "10:10")
            ],
            "days": {"Mon"}
        }

        index.setdefault(station_name, []).append(train_no)

    target = "Station50"

    start = time.perf_counter()
    without_index = []

    for train_no, details in timetable.items():
        for stop in details["stops"]:
            if stop[0] == target and "Mon" in details["days"]:
                without_index.append(train_no)

    time_without_index = time.perf_counter() - start

    start = time.perf_counter()
    with_index = [
        train_no for train_no in index.get(target, [])
        if "Mon" in timetable[train_no]["days"]
    ]

    time_with_index = time.perf_counter() - start

    print("\nNumber of trains:", size)
    print("Without index:", time_without_index)
    print("With index:", time_with_index)
    print("Same result:", set(without_index) == set(with_index))

# Unknown station
print("\nUnknown station:", find_trains("Unknown", "Mon"))

# Train that does not run on the selected day
print("Sunday trains at Katpadi:", find_trains("Katpadi", "Sun"))
