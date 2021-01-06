with open("input.txt", "r") as file:
    B_PASSES = [[int(item[:-4].replace("B", "1").replace("F", "0"), 2),
                 int(item[-4:-1].replace("R", "1").replace("L", "0"), 2)]
                for item in file.readlines()]


IDS = [item[0] * 8 + item[1] for item in B_PASSES]
print(max(IDS))

IDS = sorted(IDS)

for i, bid in enumerate(IDS):
    if i + 1 < len(IDS):
        if IDS[i + 1] - bid == 2:
            print(bid + 1)
