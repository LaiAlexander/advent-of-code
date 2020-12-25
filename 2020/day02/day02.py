def part1(file):
    valid_passwords = 0
    for line in file.readlines():
        policy, password = line.split(": ")
        password = password.replace("\n", "")
        minimum, maximum = policy.split("-")
        maximum, letter = maximum.split(" ")
        minimum = int(minimum)
        maximum = int(maximum)
        lettercount = password.count(letter)
        if minimum <= lettercount <= maximum:
            valid_passwords += 1
    print(valid_passwords)

def part2(file):
    valid_passwords = 0
    for line in file.readlines():
        policy, password = line.split(": ")
        password = password.translate({ord("\n"): None})
        first_pos, second_pos = policy.split("-")
        second_pos, letter = second_pos.split(" ")
        first_pos = int(first_pos)
        second_pos = int(second_pos)
        first_pos -= 1
        second_pos -= 1
        if bool(password[first_pos] == letter) ^ bool(password[second_pos] == letter):
            valid_passwords += 1
    print(valid_passwords)

with open("input.txt", "r") as file:
    part1(file)

with open("input.txt", "r") as file:
    part2(file)
