with open("04.txt") as f:
    lines = f.readlines()


def process_card_numbers(numbers_line: str):
    return [int(a) for a in numbers_line.strip().split(" ") if len(a) > 0]


def process_card(card_line: str):
    card_id, card_lists = card_line.strip().split(":")
    card_winning, card_numbers_you_have = card_lists.split("|")

    return (
        card_id,
        process_card_numbers(card_winning),
        process_card_numbers(card_numbers_you_have),
    )


def calculate_card_points(winning_numbers, your_numbers):
    value = 0
    for num in your_numbers:
        if num in winning_numbers:
            if value == 0:
                value = 1
            else:
                value *= 2
    return value


total = 0
for line in lines:
    id, winning, your = process_card(line)
    value = calculate_card_points(winning, your)
    total += value
print(total)
