from typing import List, Tuple


def read_input(filename="input.txt"):
    with open(filename) as f:
        return f.read().strip()


def can_move_roll(rows: List[List[str]], i: int, j: int) -> bool:
    count = 0
    for new_row_index in range(i - 1, i + 2):
        for new_col_index in range(j - 1, j + 2):
            if (
                0 <= new_row_index < len(rows)
                and 0 <= new_col_index < len(rows[i])
                and (new_row_index != i or new_col_index != j)
            ):
                count += rows[new_row_index][new_col_index] == "@"
    return count < 4


def find_accessible_rolls(rows: List[List[str]]) -> List[Tuple[int, int]]:
    return [
        (i, j)
        for i, row in enumerate(rows)
        for j, cell in enumerate(row)
        if cell == "@" and can_move_roll(rows, i, j)
    ]


def part1(data: str) -> int:
    rows = [list(row) for row in data.split("\n")]
    return len(find_accessible_rolls(rows))


def part2(data: str) -> int:
    rows = [list(row) for row in data.split("\n")]
    total_removed = 0

    while True:
        accessible = find_accessible_rolls(rows)
        if not accessible:
            break

        for i, j in accessible:
            rows[i][j] = "."

        total_removed += len(accessible)

    return total_removed


if __name__ == "__main__":
    data = read_input()
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
