import re

with open("b.txt") as f:
    lines = f.readlines()


def get_handful_contents(handful):
    contents = handful.split(",")
    result = []
    for content in contents:
        count = int(re.search(r"\d+", content)[0])

        if "blue" in content:
            result.append((count, "blue"))
        elif "red" in content:
            result.append((count, "red"))
        elif "green" in content:
            result.append((count, "green"))

    return result


def get_minimum_bag_contents(contents):
    bag = {"red": 0, "green": 0, "blue": 0}
    for content in contents:
        for count, color in content:
            if bag[color] < count:
                bag[color] = count
    return bag


def parse_game_line(line_record: str):
    game_info, rounds_string = line_record.split(":")
    id = re.search(r"\d+", game_info)[0]
    handfuls = rounds_string.split(";")

    contents = [get_handful_contents(handful) for handful in handfuls]

    return id, contents, get_minimum_bag_contents(contents)


test_bag = {"red": 12, "green": 13, "blue": 14}

total = 0
for line in lines:
    id, _, bag = parse_game_line(line)

    power = bag["red"] * bag["blue"] * bag["green"]

    total += power

print(total)
