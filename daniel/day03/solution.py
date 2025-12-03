def read_input(filename: str = "input.txt") -> str:
    with open(filename) as f:
        return f.read().strip()


def calculate_max_joltage_index(
    bank: str, start_index: int, remaining_batteries: int
) -> int:
    largest_joltage_index = start_index
    max_value = int(bank[start_index])
    for i in range(start_index, len(bank)):
        if (
            (current_value := int(bank[i])) > max_value
            and len(bank) - i > remaining_batteries
        ):
            largest_joltage_index = i
            max_value = current_value
    return largest_joltage_index


def find_max_joltage(bank: str, num_batteries: int) -> int:
    max_joltage_str = ""
    pointer = 0
    for i in range(num_batteries):
        next_index = calculate_max_joltage_index(bank, pointer, num_batteries - i - 1)
        max_joltage_str += bank[next_index]
        pointer = next_index + 1
    return int(max_joltage_str)


def part1(data: str) -> int:
    return sum(find_max_joltage(bank, 2) for bank in data.split("\n"))


def part2(data: str) -> int:
    return sum(find_max_joltage(bank, 12) for bank in data.split("\n"))


if __name__ == "__main__":
    data = read_input()
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
