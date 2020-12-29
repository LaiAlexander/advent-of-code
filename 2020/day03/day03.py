with open("input.txt", "r") as file:
    HILL = [line.replace("\n", "") for line in file.readlines()]

def traverse(hill, right, down):
    trees = 0
    height = len(hill)
    width = len(hill[0])

    column = 0
    row = 0

    while row < height:
        column = ((column + right) % width)
        row += down
        if row < height:
            if hill[row][column] == "#":
                trees += 1

    return trees

def part1():
    return traverse(HILL, 3, 1)

def part2():
    return (traverse(HILL, 1, 1) * traverse(HILL, 3, 1) * traverse(HILL, 5, 1)
            * traverse(HILL, 7, 1) * traverse(HILL, 1, 2))

print(part1())
print(part2())
