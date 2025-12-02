def read_input(filename: str = "input.txt") -> str:
    with open(filename) as f:
        return f.read().strip()


def parse_range(line: str) -> tuple[int, int]:
    # Parse a range string like '11-22' into (lower, upper)
    range_part = line.split("-")
    lower = int(range_part[0])
    upper = int(range_part[1])
    return (lower, upper)


def is_repeated_pattern(id: int) -> bool:
    # Check if a number is made of a pattern repeated at least twice
    id_str = str(id)
    id_length = len(id_str)

    # Try each possible pattern length (1 to half the total length)
    for pattern_length in range(1, id_length // 2 + 1):
        if id_length % pattern_length != 0:
            continue
        pattern = id_str[:pattern_length]
        repetitions = id_length // pattern_length
        if repetitions >= 2 and pattern * repetitions == id_str:
            return True

    return False


def generate_part1_candidates(lower: int, upper: int) -> set[int]:
    # Part 1: pattern is repeated exactly twice
    invalid_ids = set[int]()
    min_digits = len(str(lower))
    max_digits = len(str(upper))

    for num_digits in range(min_digits, max_digits + 1):
        # Only even length numbers
        if num_digits % 2 == 1:
            continue

        pattern_length = num_digits // 2
        for pattern in range(10 ** (pattern_length - 1), 10**pattern_length):
            # pattern * (10^k + 1) creates pattern repeated twice
            # For example 123 * (10^3 + 1) = 123 * 1001 = 123123
            candidate = pattern * (10**pattern_length + 1)
            if lower <= candidate <= upper:
                invalid_ids.add(candidate)

    return invalid_ids


def generate_part2_candidates(lower: int, upper: int) -> set[int]:
    # Part 2: patterns repeated 2+ times
    invalid_ids = set[int]()
    min_digits = len(str(lower))
    max_digits = len(str(upper))

    for num_digits in range(min_digits, max_digits + 1):
        # Try each pattern length that could repeat at least 2 times
        for pattern_length in range(1, num_digits // 2 + 1):
            # Pattern length must be divisor of total_length
            if num_digits % pattern_length != 0:
                continue

            # Generate all possible patterns of pattern_length
            for pattern in range(10 ** (pattern_length - 1), 10**pattern_length):
                repetitions = num_digits // pattern_length
                # For pattern "12" repeated 3 times: 12 * (10^4 + 10^2 + 10^0) = 121212
                # For pattern "123" repeated 2 times: 123 * (10^3 + 10^0) = 123123
                candidate = pattern * sum(
                    10 ** (pattern_length * i) for i in range(repetitions)
                )

                if lower <= candidate <= upper:
                    invalid_ids.add(candidate)

    return invalid_ids


def part1_brute_force(data: str) -> int:
    # Check every number in each range
    invalid_ids = []
    for line in data.split(","):
        (lower, upper) = parse_range(line)
        for i in range(lower, upper + 1):
            id_str = str(i)
            id_len = len(id_str)
            # Only check even-length numbers
            if id_len % 2 == 1:
                continue
            # Check if first half equals second half
            if id_str[: id_len // 2] == id_str[id_len // 2 :]:
                invalid_ids.append(i)
    return sum(invalid_ids)


def part1_optimized(data: str) -> int:
    # Generate only repeated pattern candidates
    all_invalid_ids = set[int]()
    for line in data.split(","):
        (lower, upper) = parse_range(line)
        candidates = generate_part1_candidates(lower, upper)
        all_invalid_ids.update(candidates)
    return sum(all_invalid_ids)


def part2_brute_force(data: str) -> int:
    # Check every number in each range
    invalid_ids = []
    for line in data.split(","):
        (lower, upper) = parse_range(line)
        for i in range(lower, upper + 1):
            if is_repeated_pattern(i):
                invalid_ids.append(i)
    return sum(invalid_ids)


def part2_optimized(data: str) -> int:
    # Generate only repeated pattern candidates
    all_invalid_ids = set[int]()
    for line in data.split(","):
        (lower, upper) = parse_range(line)
        candidates = generate_part2_candidates(lower, upper)
        all_invalid_ids.update(candidates)
    return sum(all_invalid_ids)


if __name__ == "__main__":
    data = read_input()
    print(f"Part 1 (Brute Force): {part1_brute_force(data)}")
    print(f"Part 1 (Optimized): {part1_optimized(data)}")
    print(f"Part 2 (Brute Force): {part2_brute_force(data)}")
    print(f"Part 2 (Optimized): {part2_optimized(data)}")
