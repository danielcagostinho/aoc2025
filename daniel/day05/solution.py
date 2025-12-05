from typing import List
from bisect import bisect_right


def read_input(filename="input.txt"):
    with open(filename) as f:
        return f.read().strip()


def parse_input(data: str):
    ranges_text, ingredients_text = data.split("\n\n")
    ranges = parse_ranges_to_lists(ranges_text)
    ranges = merge_ranges(ranges)
    ingredients = [int(x) for x in ingredients_text.split("\n")]
    return ranges, ingredients


def parse_ranges_to_lists(data: str) -> List[List[int]]:
    ranges = data.split("\n")
    range_list = []
    for range in ranges:
        [lower, upper] = range.split("-")
        range_list.append([int(lower), int(upper)])
    return range_list


def merge_ranges(ranges: List[List[int]]) -> List[List[int]]:
    sorted_ranges = sorted(ranges)
    merged = [sorted_ranges[0]]
    for current_range in sorted_ranges[1:]:
        last_merged = merged[-1]
        [current_range_lower, current_range_upper] = current_range
        [_, last_range_upper] = last_merged
        if current_range_lower <= last_range_upper + 1:
            last_merged[1] = max(last_range_upper, current_range_upper)
        else:
            merged.append(current_range)
    return merged


def part1(data: str) -> int:
    fresh_ingredients = set()
    ranges, ingredients = parse_input(data)
    for ingredient in ingredients:
        for ingredient_range in ranges:
            [lower_bound, upper_bound] = ingredient_range
            if lower_bound <= ingredient <= upper_bound:
                fresh_ingredients.add(ingredient)
    return len(fresh_ingredients)


def part1_binary_search(data: str) -> int:
    fresh_ingredients = set()
    ranges, ingredients = parse_input(data)
    range_starts = [r[0] for r in ranges]
    for ingredient in ingredients:
        idx = bisect_right(range_starts, ingredient)
        if idx > 0:
            range_to_check = ranges[idx - 1]
            [lower_bound, upper_bound] = range_to_check
            if lower_bound <= ingredient <= upper_bound:
                fresh_ingredients.add(ingredient)
    return len(fresh_ingredients)


def part1_two_pointers(data: str) -> int:
    ranges, ingredients = parse_input(data)
    sorted_ingredients = sorted(ingredients)
    range_idx = 0
    fresh_count = 0
    for ingredient in sorted_ingredients:
        while range_idx < len(ranges) and ranges[range_idx][1] < ingredient:
            range_idx += 1
        if range_idx < len(ranges):
            start, end = ranges[range_idx]
            if start <= ingredient <= end:
                fresh_count += 1
    return fresh_count


def part2(data: str) -> int:
    ranges_text = data.split("\n\n")[0]
    ranges = parse_ranges_to_lists(ranges_text)
    merged = merge_ranges(ranges)
    total = 0
    for start, end in merged:
        total += end - start + 1
    return total


if __name__ == "__main__":
    data = read_input()
    print(f"Part 1: {part1(data)}")
    print(f"Part 1 (Binary Search): {part1_binary_search(data)}")
    print(f"Part 1 (Two Pointers): {part1_two_pointers(data)}")
    print(f"Part 2: {part2(data)}")
