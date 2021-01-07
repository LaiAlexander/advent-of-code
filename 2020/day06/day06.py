with open("input.txt", "r") as file:
    ALL_ANSWERS = file.read().split("\n\n")

LETTERS = [chr(letter) for letter in range(ord("a"), ord("z") + 1)]

def part_1():
    count = 0
    for answer_from_group in ALL_ANSWERS:
        current_letters = LETTERS.copy()
        for letter in answer_from_group:
            try:
                current_letters.remove(letter)
            except ValueError:
                pass
        count += (len(LETTERS) - len(current_letters))
    return count

def part_2():
    count = 0
    for answer_from_group in ALL_ANSWERS:
        single_answers = answer_from_group.split("\n")
        # last answer_from_group has an empty entry at the end, need to remove it
        try:
            single_answers.remove("")
        except ValueError:
            pass
        # create dict to store how many of each letter/answer
        letters_dict = {LETTERS[i]: 0 for i in range(0, len(LETTERS))}

        for single_answer in single_answers:
            for letter in single_answer:
                letters_dict[letter] += 1

        for value in letters_dict.values():
            if value == len(single_answers):
                count += 1
    return count

print(part_1())
print(part_2())
