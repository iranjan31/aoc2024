import os, sys
from itertools import pairwise

# Read in the data
with open('day2_input.txt', 'r') as file:
    data = file.read().splitlines()

# is_safe method adapted from nitekat 
# Source: https://github.com/nitekat1124/advent-of-code-2024/tree/main
def is_safe(levels):
    differs = [a - b for a, b in zip(levels, levels[1:])]
    is_monotonic = all(i > 0 for i in differs) or all(i < 0 for i in differs)
    is_in_range = all(0 < abs(i) <= 3 for i in differs)
    if is_monotonic and is_in_range:
        return True
    return False

# Convert the data into a list of reports which themselves are lists of levels or integers
reports = [list(map(int, item.split(' '))) for item in data]

# Find the number of safe reports
safe_reports = [report for report in reports if is_safe(report)]

print(f"The number of safe reports is: {len(safe_reports)}")

safe_with_one_removed = []

# Find the number of safe reports with one level removed
for report in reports:
    for i in range(len(report)):
        tolerated_levels = report[:i] + report[i + 1 :]
        if is_safe(tolerated_levels):
            safe_with_one_removed.append(tolerated_levels)
            break

print(f"The number of safe reports with one removed is: {len(safe_with_one_removed)}")