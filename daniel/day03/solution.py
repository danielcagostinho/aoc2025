def read_input(filename="input.txt"):
    with open(filename) as f:
        return f.read().strip()


BATTERIES_TO_TURN_ON = 12


def calculate_max_joltage_index(bank: str) -> int:
    largest_joltage_index = 0
    print(f"parsing sub-bank: {bank}, length: {len(bank)}")
    for i in range(1, len(bank)):
        if int(bank[i]) > int(bank[largest_joltage_index]):
            largest_joltage_index = i
    return largest_joltage_index


def calculate_max_joltage_index_part_2(bank: str, remaining_batteries: int) -> int:
    largest_joltage_index = 0
    for i in range(1, len(bank)):
        if (
            int(bank[i]) > int(bank[largest_joltage_index])
            and len(bank) - i >= remaining_batteries
        ):
            largest_joltage_index = i
    return largest_joltage_index


def part1(data: str) -> int:
    max_joltages = []
    for bank in data.split("\n"):
        max_joltage_a = calculate_max_joltage_index(bank[: len(bank) - 1])
        substring = bank[max_joltage_a + 1 :]
        max_joltage_b = calculate_max_joltage_index(substring)
        max_joltage = bank[max_joltage_a] + bank[max_joltage_a + 1 + max_joltage_b]
        max_joltages.append(int(max_joltage))
    return sum(max_joltages)


def part2(data):
    max_joltages = []
    for bank in data.split("\n"):
        highest_first_index = calculate_max_joltage_index_part_2(
            bank[: len(bank) - 1], BATTERIES_TO_TURN_ON - 1
        )
        max_joltage_str = bank[highest_first_index]
        pointer = highest_first_index
        for i in range(BATTERIES_TO_TURN_ON - 1):
            sub_bank = bank[pointer + 1 :]
            next_max_joltage_index = (
                calculate_max_joltage_index_part_2(sub_bank, BATTERIES_TO_TURN_ON - i - 1) + pointer + 1
            )
            max_joltage_str = max_joltage_str + bank[next_max_joltage_index]
            pointer = next_max_joltage_index
        max_joltages.append(int(max_joltage_str))

    return sum(max_joltages)


if __name__ == "__main__":
    data = read_input()
    # print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
