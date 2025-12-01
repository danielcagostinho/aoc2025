def read_input(filename='input.txt'):
    with open(filename) as f:
        return f.read().strip()


def part1(data):
    # initialize zero count to 0
    zero_count = 0
    position = 50
    
    # iterate through input
    for line in data.split("\n"):
        # parse the string into a tuple of [direction, amount]
        [direction, amount] = parse_rotation(line)
        
        # if direction is left, rotate left
        if direction == "L":
            position = rotate_left(position, amount)
        # elif direciton is right, rotate right
        elif direction == "R":
            position = rotate_right(position, amount)
        # if position is now 0, increment counter
        if position == 0:
            zero_count += 1
    return zero_count

def rotate_left(position, amount, limit=100):
    # do modular aritmetic to make sure rotating past 99 will reset to 0
    new_position = (position - amount) % limit
    return new_position

def rotate_right(position, amount, limit=100):
    # do modular aritmetic to make sure rotating past 99 will reset to 0
    new_position = (position + amount) % limit
    return new_position

def part2(data):
    # initialize zero count to 0
    zero_count = 0
    position = 50
    
    # iterate through input
    for line in data.split("\n"):
        
        # parse the string into a tuple of [direction, amount]
        [direction, amount] = parse_rotation(line)

        # if direction is left, rotate left
        if direction == "L":
            # if starting position is 0 
            if position == 0:
                times_crossed = (amount) // 100
            
            # if amount >= position we cross at least once
            elif amount >= position:
                times_crossed = (amount - position + 100) // 100
            
            # if amount < position, we dont cross
            else:
                times_crossed = 0
                
            position = rotate_left(position, amount)

            zero_count += times_crossed
            
        # elif direciton is right, rotate right
        elif direction == "R":
            times_crossed = (position + amount) // 100
            position = rotate_right(position, amount)
            zero_count += times_crossed
    return zero_count

def parse_rotation(line):
    # Split the first char of the substring. we should return a tuple of [direction, amount]
    direction = line[0]
    amount = int(line[1:])
    return [direction, amount]

    
if __name__ == '__main__':
    data = read_input()
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
