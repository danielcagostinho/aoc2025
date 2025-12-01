def read_input(filename="input.txt"):
    with open(filename) as f:
        return f.read().strip()


STARTING_POSITION = 50
DIAL_SIZE = 100


def rotate_left(position, amount):
    return (position - amount) % DIAL_SIZE


def rotate_right(position, amount):
    return (position + amount) % DIAL_SIZE


def count_zero_crossings_left(position, amount):
    if position == 0:
        return amount // DIAL_SIZE
    elif amount >= position:
        return (amount - position + DIAL_SIZE) // DIAL_SIZE
    else:
        return 0


def count_zero_crossings_right(position, amount):
    return (position + amount) // DIAL_SIZE


def part1(data):
    zero_count = 0
    position = STARTING_POSITION

    for line in data.split("\n"):
        (direction, amount) = parse_rotation(line)

        if direction == "L":
            position = rotate_left(position, amount)
        elif direction == "R":
            position = rotate_right(position, amount)
        if position == 0:
            zero_count += 1
    return zero_count


def part2(data):
    zero_count = 0
    position = STARTING_POSITION

    for line in data.split("\n"):
        (direction, amount) = parse_rotation(line)

        if direction == "L":
            times_crossed = count_zero_crossings_left(position, amount)
            position = rotate_left(position, amount)
            zero_count += times_crossed

        elif direction == "R":
            times_crossed = count_zero_crossings_right(position, amount)
            position = rotate_right(position, amount)
            zero_count += times_crossed
    return zero_count


def parse_rotation(line):
    direction = line[0]
    amount = int(line[1:])
    return (direction, amount)


if __name__ == "__main__":
    data = read_input()
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
