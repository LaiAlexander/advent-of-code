with open("input.txt", "r") as file:
    PASSPORTS = file.read().split("\n\n")
    for i, item in enumerate(PASSPORTS):
        PASSPORTS[i] = item.replace("\n", " ")

# ignoring field "cid"
FIELDS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

VALID_PASSPORTS_P1 = 0
VALID_PASSPORTS_P2 = 0

def validate_int(minimum, maximum, number):
    """
    number must be an int.
    """
    return minimum <= number <= maximum

def validate_pid(pid):
    return len(pid) == 9 and pid.isnumeric()

def validate_hcl(hcl):
    if hcl[0] != "#":
        return False
    hcl = hcl.replace("#", "")

    if len(hcl) != 6:
        return False

    valid_symbols = [str(i) for i in range(10)] + [chr(l) for l in range(ord('a'), ord('a') + 6)]

    for symbol in hcl:
        if symbol not in valid_symbols:
            return False

    return True

def validate_ecl(ecl):
    colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    return ecl in colors

def validate_hgt(hgt):
    if len(hgt) > 3:
        if hgt[-2:] == "cm":
            hgt = int(hgt[:-2])
            return validate_int(150, 193, hgt)
        if hgt[-2:] == "in":
            hgt = int(hgt[:-2])
            return validate_int(59, 76, hgt)
    return False

def validated_p2(passport):
    return (validate_int(1920, 2002, int(passport["byr"]))
            and validate_int(2010, 2020, int(passport["iyr"]))
            and validate_int(2020, 2030, int(passport["eyr"]))
            and validate_pid(passport["pid"])
            and validate_hcl(passport["hcl"])
            and validate_ecl(passport["ecl"])
            and validate_hgt(passport["hgt"]))

for passport in PASSPORTS:
    details = passport.split(" ")
    passport_dict = {}
    for detail in details:
        if detail:
            detail = detail.split(":")
            passport_dict[detail[0]] = detail[1]

    valid = True
    for field in FIELDS:
        if not passport_dict.get(field):
            valid = False

    if valid:
        VALID_PASSPORTS_P1 += 1
        if validated_p2(passport_dict):
            VALID_PASSPORTS_P2 += 1

print(VALID_PASSPORTS_P1)
print(VALID_PASSPORTS_P2)
