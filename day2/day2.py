from itertools import pairwise

def is_safe(levels):
    diffs = [a - b for a, b in pairwise(levels)]
    return (all(d > 0 for d in diffs) or all(d < 0 for d in diffs)) and all(0 < abs(d) <= 3 for d in diffs)

with open('day2_input.txt', 'r') as file:
    reports = [list(map(int, line.split())) for line in file]

safe_reports = [report for report in reports if is_safe(report)]

safe_with_one_removed = {
    tuple(report)
    for report in reports
    for i in range(len(report))
    if is_safe(report[:i] + report[i + 1:])
}

print(f"The number of safe reports is: {len(safe_reports)}")
print(f"The number of safe reports with one removed is: {len(safe_with_one_removed)}")
