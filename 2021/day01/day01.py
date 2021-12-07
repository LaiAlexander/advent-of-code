with open("input.txt", "r") as file:
    DEPTHS = [int(item) for item in file.readlines()]

def part_1():
    depth_increases = 0

    for i, depth in enumerate(DEPTHS):
        if i + 1 < len(DEPTHS):
            if DEPTHS[i + 1] > depth:
                depth_increases += 1

    return depth_increases

# This can probably be optimized by memoization or something.
# There's repetion of the calculation of the rolling depths
# Could probably just make a list and then use part_1() actually
def part_2():
    rolling_depth_increases = 0

    for i, _depth in enumerate(DEPTHS):
        if i + 3 < len(DEPTHS):
            first_d = DEPTHS[i] + DEPTHS[i + 1] + DEPTHS[i + 2]
            second_d = DEPTHS[i + 1] + DEPTHS[i + 2] + DEPTHS[i + 3]
            if second_d > first_d:
                rolling_depth_increases += 1

    return rolling_depth_increases

print(part_1())
print(part_2())