import re

# Regex patterns
mul_pattern = r"mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)"  # Matches mul(X, Y) where X and Y are 1-3 digit integers
control_pattern = r"do\(\)|don't\(\)"  # Matches do() or don't()

# Initialize variables
total_sum = 0
mul_enabled = True  # Multiplications are enabled by default

# Read the puzzle input from a file (assumed to be "input.txt")
with open("Day Three/day3input.txt", "r") as file:
    for line in file:
        # Process control instructions in the order they appear
        controls = re.findall(control_pattern, line)
        for control in controls:
            if control == "do()":
                mul_enabled = True
            elif control == "don't()":
                mul_enabled = False

        # Process mul(X, Y) instructions only if enabled
        matches = re.findall(mul_pattern, line)
        for match in matches:
            if mul_enabled:
                num1, num2 = map(int, match)  # Convert the captured integers
                total_sum += num1 * num2

# Print the result
print(f"The total sum of all enabled mul(X, Y) results is: {total_sum}")
