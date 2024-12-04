import re

# Read the file as input
with open('day3_input.txt', 'r') as file:
    corrupted_memory = file.read().replace('\n', '')

# Calculate the total sum of the valid multiplication instructions
total = sum(int(x) * int(y) for x, y in re.findall(r'\bmul\((\d{1,3}),(\d{1,3})\)', corrupted_memory))

print("Total sum of valid mul instructions:", total)

mul_enabled = True  # Mul instructions are enabled by default
total = 0  # Total sum of enabled mul results

# Scan through the memory sequentially
index = 0
while index < len(corrupted_memory):
    # Check for "do()" or "don't()"
    if match := re.match(r'\bdo\(\)', corrupted_memory[index:]):
        mul_enabled = True
        index += match.end()
    elif match := re.match(r'\bdon\'t\(\)', corrupted_memory[index:]):
        mul_enabled = False
        index += match.end()
    # Check for "mul(X,Y)"
    elif match := re.match(r'\bmul\((\d{1,3}),(\d{1,3})\)', corrupted_memory[index:]):
        if mul_enabled:
            x, y = map(int, match.groups())
            total += x * y
        index += match.end()
    else:
        # Skip invalid or unimportant characters
        index += 1

print("Total sum of enabled mul instructions:", total)