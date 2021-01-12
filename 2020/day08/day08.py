with open("input.txt") as file:
    INSTRUCTIONS = [(line.split(" ")[0], line.split(" ")[1][:-1]) for line in file.readlines()]

def part_1():
    """
    Returns (bool, int). The bool describes whether or not it reached the
    end of the instructions. The int is the value in the acc before termination.
    """
    visited_instructions = [False for i in INSTRUCTIONS]

    index = 0
    acc = 0
    while True:
        if index >= len(INSTRUCTIONS):
            return True, acc
        instruction, value = INSTRUCTIONS[index]
        if visited_instructions[index]:
            return False, acc
        visited_instructions[index] = True
        if instruction == "nop":
            index += 1
        elif instruction == "acc":
            acc += int(value)
            index += 1
        elif instruction == "jmp":
            index += int(value)

def part_2():
    """
    Returns either a bool or an int. The bool is returned if no end is found in the instructions.
    The int is the value in the accumulator before termination.
    """
    found_end = False
    for i, instruction in enumerate(INSTRUCTIONS):
        if instruction[0] == "nop":
            INSTRUCTIONS[i] = ("jmp", instruction[1])
            if part_1()[0]:
                found_end = True
                return part_1()[1]
            INSTRUCTIONS[i] = ("nop", instruction[1])
        elif instruction[0] == "jmp":
            INSTRUCTIONS[i] = ("nop", instruction[1])
            if part_1()[0]:
                found_end = True
                return part_1()[1]
            INSTRUCTIONS[i] = ("jmp", instruction[1])
    if not found_end:
        return False

print(part_1()[1])
print(part_2())
