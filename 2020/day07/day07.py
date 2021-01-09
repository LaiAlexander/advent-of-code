def clean_up_color_values(colors):
    new_colors = []
    if colors != "no other bags.\n":
        new_colors = colors.split(", ")
        for i, new_color in enumerate(new_colors):
            single_color = new_color.split(" bag")
            new_colors[i] = (int(single_color[0][0]), single_color[0][2:])
    return new_colors

with open("input.txt", "r") as file:
    ALL_BAGS = {bag.split(" bags contain ")[0]: bag.split(" bags contain ")[1] for bag in file.readlines()}
    for key, value in ALL_BAGS.items():
        ALL_BAGS[key] = clean_up_color_values(value)

def find_bag(bag, color):
    for item in ALL_BAGS[bag]:
        if item:
            if item[1] == color:
                return True
            if find_bag(item[1], color):
                return True
    return False

def part_1():
    count = 0
    for key in ALL_BAGS:
        if find_bag(key, "shiny gold"):
            count += 1
    return count

def find_count(color):
    total_count = 0
    if ALL_BAGS[color]:
        for number, bag in ALL_BAGS[color]:
            total_count += number + number * find_count(bag)
    return total_count

def part_2():
    return None

print(part_1())
print(find_count("shiny gold"))