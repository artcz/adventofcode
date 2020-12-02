inp = open("input").read().strip().splitlines()


def p1():
    valid = 0
    for line in inp:
        pos, letter, password = line.split()
        x, y = pos.split('-')
        x = int(x)
        y = int(y)
        if x <= password.count(letter.strip(':')) <= y:
            valid += 1

    print(valid)


p1()


# inp = """
# 1-3 a: abcde
# 1-3 b: cdefg
# 2-9 c: ccccccccc
# """.strip().splitlines()

def p2():
    valid = 0
    for line in inp:
        pos, letter, password = line.split()
        x, y = pos.split('-')
        x = int(x)
        y = int(y)
        letter = letter.strip(':')
        xx = {password[x-1], password[y-1]}
        # NOTE: instead of set this can be xored
        if letter in xx and len(xx) == 2:
            valid += 1

    print(valid)


p2()
