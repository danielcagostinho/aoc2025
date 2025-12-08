def read_input(filename: str="input.txt") -> str:
    with open(filename) as f:
        return f.read().strip()


def part1(data: str) -> int:
    rows = data.split("\n")
    grid = rows
    start_row, start_col = next(
        (row_idx, col_idx)
        for row_idx, row in enumerate(grid)
        for col_idx, char in enumerate(row)
        if char == "S"
    )
    split_count = 0
    active_columns = {start_col}
    for row_idx in range(start_row, len(grid)):
        next_columns = set()
        for col in active_columns:
            if grid[row_idx][col] == "^":
                split_count += 1
                next_columns.add(col - 1)
                next_columns.add(col + 1)
            else:
                next_columns.add(col)
        active_columns = next_columns
        if not active_columns:
            break
    return split_count


def count_paths_from(row, col, grid, memo):
    if (row, col) in memo:
        return memo[(row, col)]
    
    if row >= len(grid):
        return 1
    
    if col < 0 or col >= len(grid[0]):
        return 0
    
    if grid[row][col] == '^':
        result = count_paths_from(row + 1, col -1, grid, memo) + count_paths_from(row+1, col +1, grid, memo)
    else:
        result = count_paths_from(row+1, col, grid, memo)

    
    memo[(row, col)] = result
    return result

def part2(data: str) -> int:
    rows = data.split("\n")
    grid = rows
    start_row, start_col = next(
        (row_idx, col_idx)
        for row_idx, row in enumerate(grid)
        for col_idx, char in enumerate(row)
        if char == "S"
    )
    memo = {}
    answer = count_paths_from(start_row, start_col, grid, memo)
    return answer


if __name__ == "__main__":
    data = read_input()
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
