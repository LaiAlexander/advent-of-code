def validate_part1(minimum, maximum, letter, password):
    lettercount = password.count(letter)
    if minimum <= lettercount <= maximum:
        return True
    return False


def validate_part2(first_pos, second_pos, letter, password):
    first_pos -= 1
    second_pos -= 1
    if bool(password[first_pos] == letter) ^ bool(password[second_pos] == letter):
        return True
    return False

with open("input.txt", "r") as file:
    valid_passwords_part1 = 0
    valid_passwords_part2 = 0

    for line in file.readlines():
        policy, password = line.split(": ")
        password = password.translate({ord("\n"): None})

        first_num, second_num = policy.split("-")
        second_num, letter = second_num.split(" ")

        first_num = int(first_num)
        second_num = int(second_num)

        if validate_part1(first_num, second_num, letter, password):
            valid_passwords_part1 += 1
        if validate_part2(first_num, second_num, letter, password):
            valid_passwords_part2 += 1

    print(f"Valid passwords part 1: {valid_passwords_part1}")
    print(f"Valid passwords part 2: {valid_passwords_part2}")
