batches = open("input").read().strip().split("\n\n")

print("--- Day 04 ----")


def compare_keys(k1, k2, optional=None):
    valid = not (k1 ^ k2)
    if optional:
        return valid or (k1 ^ k2 == optional)
    return valid


def p1():
    ans = 0
    for batch in batches:
        batch = batch.replace("\n", " ")
        batch = batch.split()
        psp = dict(tuple(b.split(":")) for b in batch)
        legal_keys = {
            "byr",
            "iyr",
            "eyr",
            "hgt",
            "hcl",
            "ecl",
            "pid",
            "cid",
        }
        # This or makes 'cid' optional.
        # If you want to count things that have CIDs just remove the or part
        # If you want to count things that _donthave_ CIDs just remove cid from
        # the top (and the OR)
        if compare_keys(legal_keys, psp.keys(), optional={'cid'}):
            ans += 1

    print(ans)


def p2():
    ans = 0

    for batch in batches:
        batch = batch.replace("\n", " ")
        batch = batch.split()
        psp = dict(tuple(b.split(":")) for b in batch)
        legal_keys = {
            "byr",
            "iyr",
            "eyr",
            "hgt",
            "hcl",
            "ecl",
            "pid",
            "cid",
        }
        valid = False

        if compare_keys(legal_keys, psp.keys(), {'cid'}):
            valid = True

        if not valid:
            continue

        valid = valid and 1920 <= int(psp["byr"]) <= 2002
        valid = valid and 2010 <= int(psp["iyr"]) <= 2020
        valid = valid and 2020 <= int(psp["eyr"]) <= 2030

        if psp["hgt"].endswith("cm"):
            valid = valid and 150 <= int(psp["hgt"][:-2]) <= 193
        elif psp["hgt"].endswith("in"):
            valid = valid and 59 <= int(psp["hgt"][:-2]) <= 76
        else:
            valid = False

        valid = valid and psp["hcl"][0] == "#"
        valid = valid and len(psp["hcl"][1:]) == 6
        valid = valid and all(c in "abcdef0123456789" for c in psp["hcl"][1:])
        valid = valid and psp["ecl"] in {
            "amb",
            "blu",
            "brn",
            "gry",
            "grn",
            "hzl",
            "oth",
        }

        valid = valid and len([d for d in psp["pid"] if d.isdigit()]) == 9

        if valid:
            ans += 1

    print(ans)


print("Part1")
p1()
print("Part2")
p2()
print("EOD")
