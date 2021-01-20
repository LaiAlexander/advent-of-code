from collections import deque

with open("input.txt") as file:
    NUMBERS = [int(line.replace("\n", "")) for line in file.readlines()] # may use line.strip() instead, simpler.

def part_1():
    def validate_number(current_numbers, num):
        for i in current_numbers:
            for j in current_numbers:
                if i != j:
                    if (i + j) == num:
                        return True
        return False

    current_numbers = deque(maxlen=25)
    for number in NUMBERS:
        if len(current_numbers) == current_numbers.maxlen:
            if not validate_number(current_numbers, number):
                return number
        current_numbers.append(number)
    return None

def part_2(target):
    for i, start_number in enumerate(NUMBERS):
        cont_numbers = [] # is deque() better?
        cont_numbers.append(start_number)
        for end_number in NUMBERS[i + 1:]:
            if sum(cont_numbers) == target:
                return min(cont_numbers) + max(cont_numbers)
            if sum(cont_numbers) > target:
                break
            cont_numbers.append(end_number)
    return None

answer_p1 = part_1()
print(answer_p1)
print(part_2(answer_p1))
