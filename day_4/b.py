import re

with open("04.txt") as f:
    lines = f.readlines()


def process_card_numbers(numbers_line: str):
    return [int(a) for a in numbers_line.strip().split(" ") if len(a) > 0]


def process_card(card_line: str):
    card_id_str, card_lists = card_line.strip().split(":")
    card_winning, card_numbers_you_have = card_lists.split("|")

    card_id = int(re.search(r"\d+", card_id_str)[0])
    return (
        card_id,
        process_card_numbers(card_winning),
        process_card_numbers(card_numbers_you_have),
    )


def calculate_card_points(winning_numbers, your_numbers):
    value = 0
    for num in your_numbers:
        if num in winning_numbers:
            value += 1
    return value


cards = {}
for line in lines:
    id, winning, your = process_card(line)
    cards[id] = {"winning": winning, "your": your, "count": 1}


for card_id, card in cards.items():
    value = calculate_card_points(card["winning"], card["your"])
    print(card_id, value)
    if value > 0:
        for i in range(card_id + 1, card_id + value + 1):
            if cards.get(i) != None:
                cards[i]["count"] += card["count"]


print(sum([card["count"] for card in cards.values()]))
