with open("sample_one.txt") as f:
    lines = f.readlines()

word_map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def scan_line_for_matches(line: str, lookup_dict: dict):
    line_clone = line
    first_number = None
    while first_number is None:
        first_char = line_clone[0]

        is_number = first_char.isnumeric()

        if is_number:
            first_number = first_char
            continue

        for k, v in lookup_dict.items():
            match = line_clone.find(k, 0)
            if match == 0:
                first_number = v
                break

        line_clone = line_clone[1:]

    return first_number


total = 0
invert_word_map = {k[::-1]: v for k, v in word_map.items()}

for line in lines:
    first_number = scan_line_for_matches(line, word_map)
    last_number = scan_line_for_matches(line[::-1], invert_word_map)
    final = int(f"{first_number}{last_number}")
    total += final

print(total)
