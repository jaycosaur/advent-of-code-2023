with open("03.txt") as f:
    lines = f.readlines()


def create_grid(lines):
    grid = []
    for line in lines:
        grid.append([*line.strip()])
    return grid


def find_parts(grid):
    parts = []
    for ir, row in enumerate(grid):
        for ic, col in enumerate(row):
            if not col.isdigit() and col != ".":
                parts.append((ir, ic, col))
    return parts


def find_numbers(grid):
    numbers = []
    for ir, row in enumerate(grid):
        digit_start = None
        digits = []
        for ic, col in enumerate(row):
            if col.isdigit():
                digits.append(col)
                if digit_start == None:
                    digit_start = ic
            elif digit_start != None:
                # not a digit so must be end of number
                numbers.append([(ir, digit_start), (ir, ic - 1), int("".join(digits))])
                digit_start = None
                digits = []
        if digit_start != None:
            # number must have ended on a row
            numbers.append(
                [(ir, digit_start), (ir, len(row) - 1), int("".join(digits))]
            )

    return numbers


grid = create_grid(lines)
parts = find_parts(grid)
possible_part_number_locations = find_numbers(grid)


def row(location):
    return location[0]


def col(location):
    return location[1]


def touches_part(part_location, number_location_range):
    number_start, number_end = number_location_range
    # check rows
    if (
        row(number_start) < row(part_location) - 1
        or row(number_start) > row(part_location) + 1
    ):
        return False

    # check column
    if (
        col(part_location) >= col(number_start) - 1
        and col(part_location) <= col(number_end) + 1
    ):
        return True


total = 0
for part in parts:
    ...
    # scan each possible part number and see if it touches
    part_row, part_col, _ = part

    for (
        part_number_start,
        part_number_end,
        part_number,
    ) in possible_part_number_locations:
        if touches_part((part_row, part_col), [part_number_start, part_number_end]):
            total += part_number

print(total)
