import re

with open("sample_one.txt") as f:
    lines = f.readlines()

total = 0
for line in lines:
    first_number = re.search(r"\d", line)[0]
    last_number = re.search(r"\d", line[::-1])[0]
    final = int(f"{first_number}{last_number}")
    total += final

print(total)
