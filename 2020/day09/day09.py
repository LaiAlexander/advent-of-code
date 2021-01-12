from collections import deque

with open("input.txt") as file:
    NUMBERS = [int(line.replace("\n", "")) for line in file.readlines()]

def part_1():
    last_numbers = deque(maxlen=25)
    for number in NUMBERS:
        if len(last_numbers) == last_numbers.maxlen:
            sums = set()
            for i in last_numbers:
                for j in last_numbers:
                    if i != j:
                        sums.add(i + j)
            if number not in sums:
                return number
        last_numbers.append(number)
    return None

def part_2(target):
    for i, start_number in enumerate(NUMBERS):
        cont_numbers = deque()
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
