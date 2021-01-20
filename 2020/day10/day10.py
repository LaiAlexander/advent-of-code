with open("input.txt") as file:
    JOLTAGES = [int(line.strip()) for line in file.readlines()]
    JOLTAGES.append(0)
    JOLTAGES.append(max(JOLTAGES) + 3)
    JOLTAGES.sort()

def part_1():
    ones = 0
    threes = 0
    for i in range(len(JOLTAGES) - 1):
        difference = JOLTAGES[i + 1] - JOLTAGES[i]
        if difference == 1:
            ones += 1
        elif difference == 3:
            threes += 1

    return ones * threes

def part_2():
    intervals = {}
    length_of_consecutive_numbers = 1
    for i in range(len(JOLTAGES) - 1):
        difference = JOLTAGES[i + 1] - JOLTAGES[i]
        if difference == 1:
            length_of_consecutive_numbers += 1
        elif difference == 3:
            if intervals.get(length_of_consecutive_numbers):
                intervals[length_of_consecutive_numbers] += 1
            else:
                if length_of_consecutive_numbers > 2:
                    intervals[length_of_consecutive_numbers] = 1
            length_of_consecutive_numbers = 1

    configurations = 1
    for length, count in intervals.items():
        for i in range(count):
            configurations *= calculate_number_of_paths(3, length)

    return configurations

def calculate_number_of_paths(max_jump, length):

    def memoize_num_of_paths(memoized, max_jump, length):
        paths = 0
        if memoized.get(length):
            return memoized[length]
        if max_jump == 1:
            return 1
        if length <= 0: # may end up with negative length when recursing
            return 0
        if length <= 1:
            return 1
        for i in range(1, max_jump + 1):
            paths += memoize_num_of_paths(memoized, max_jump, length - i)
        memoized[length] = paths
        return paths

    memoized = {}
    return memoize_num_of_paths(memoized, max_jump, length)

print(part_1())
print(part_2())
