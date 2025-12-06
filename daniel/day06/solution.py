def read_input(filename: str = "input.txt") -> str:
    with open(filename) as f:
        return f.read().strip("\n")


def evaluate_expression(expression: tuple[str, ...]) -> int:
    operator = expression[-1]
    operands = [int(x) for x in expression[:-1]]
    if operator == "+":
        return sum(operands)
    else:
        result = 1
        for num in operands:
            result *= num
        return result


def part1(data: str) -> int:
    rows = [line.split() for line in data.split("\n")]
    total = 0
    cols = list(zip(*rows))
    for col in cols:
        result = evaluate_expression(col)
        total += result
    return total


def process_expression_rtl(expression: list[tuple[str, ...]]) -> int:
    operator = next(col[-1] for col in expression if col[-1] != " ")
    numbers = [int("".join(c for c in col[:-1] if c != " ")) for col in expression]
    if operator == "+":
        return sum(numbers)
    else:
        result = 1
        for num in numbers:
            result *= num
        return result


def part2(data: str) -> int:
    cols = list(zip(*data.split("\n")))
    separator_indices = [i for i, col in enumerate(cols) if all(c == " " for c in col)]
    expressions = []
    start = 0
    for idx in separator_indices:
        expressions.append(cols[start:idx])
        start = idx + 1
    expressions.append(cols[start:])
    return sum(process_expression_rtl(expression) for expression in expressions)


if __name__ == "__main__":
    data = read_input()
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
