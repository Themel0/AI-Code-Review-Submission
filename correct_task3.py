# Write your corrected implementation for Task 3 here.
# Do not modify `task3.py`.
def average_valid_measurements(values):
    total = 0
    valid_count = 0

    for v in values:
        if isinstance(v, (float, int)):
            total += v
            valid_count += 1

    if valid_count == 0:
        return 0
    return total/valid_count
