import random
import time

TARGET_COUNT = 10_000
MAX_RANDOM_VALUE = 12_000


def time_in_ms():
    return time.perf_counter() * 1000


def build_unique_random_values(count, upper_bound):
    values = []
    while len(values) < count:
        candidate = random.randint(1, upper_bound)
        if candidate not in values:
            values.append(candidate)
    return values


def search(needle, haystack):
    start_time = time_in_ms()
    try:
        found_item = haystack[haystack.index(needle)]
    except ValueError:
        found_item = None
    duration = time_in_ms() - start_time
    return duration, found_item


values = build_unique_random_values(TARGET_COUNT, MAX_RANDOM_VALUE)
#quick_sort(values, 0, len(values) - 1) #values sorted perform a quicker search

durations = []

for _ in range(100):
    needle = random.choice(values)
    duration, found_item = search(needle, values)
    durations.append(duration)

average_time = sum(durations) / len(durations)

print(f"Average search time over 100 runs: {average_time:.4f} ms")