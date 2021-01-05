with open("input.txt", "r") as file:
    PASSPORTS = file.read().split("\n\n")
    for i, item in enumerate(PASSPORTS):
        PASSPORTS[i] = item.replace("\n", " ")

# ignoring field "cid"
FIELDS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

VALID_PASSPORTS_P1 = 0
VALID_PASSPORTS_P2 = 0

def validated_p2(passport):
    if int(passport["byr"]) < 1920 or int(passport["byr"]) > 2002:
        return False

    if int(passport["iyr"]) < 2010 or int(passport["iyr"]) > 2020:
        return False

    if int(passport["eyr"]) < 2020 or int(passport["eyr"]) > 2030:
        return False

    if len(passport["pid"]) != 9 or not passport["pid"].isnumeric():
        return False

    hcl = passport["hcl"]
    if hcl[0] != "#":
        return False
    hcl = hcl.replace("#", "")
    letters = ["a", "b", "c", "d", "e", "f"]
    if len(hcl) != 6:
        return False
    for alphanum in hcl:
        if not alphanum.isnumeric() and alphanum not in letters:
            return False

    ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if passport["ecl"] not in ecl:
        return False

    hgt = passport["hgt"]
    if len(hgt) > 3:
        if hgt[-2:] == "cm":
            hgt = int(hgt[:-2])
            if hgt < 150 or hgt > 193:
                return False
        elif hgt[-2:] == "in":
            hgt = int(hgt[:-2])
            if hgt < 59 or hgt > 76:
                return False
        else:
            return False
    else:
        return False

    return True

for passport in PASSPORTS:
    details = passport.split(" ")
    passport_dict = {}
    for detail in details:
        if detail:
            detail = detail.split(":")
            passport_dict[detail[0]] = detail[1]

    valid = True
    for field in FIELDS:
        if passport_dict.get(field):
            pass
        else:
            valid = False

    if valid:
        VALID_PASSPORTS_P1 += 1
        if validated_p2(passport_dict):
            VALID_PASSPORTS_P2 += 1

print(VALID_PASSPORTS_P1)
print(VALID_PASSPORTS_P2)
