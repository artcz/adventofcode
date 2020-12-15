numbers = open("input").read().strip().split(",")
numbers = [int(x) for x in numbers]

print("\nDay 15", "=" * 79)


def run(upto=2020):
    last = {}
    for turn, num in enumerate(numbers, start=1):
        last[num] = turn

    new = numbers[-1]
    for turn in range(turn, upto):
        old = new
        new = turn - last[old] if old in last else 0
        last[old] = turn

    print(new)


def p1():
    run(2020)


def p2():
    run(30_000_000)


print("Part1", "-" * 80)
print("")
p1()
print("")
print("Part2", "-" * 80)
print("")
p2()
print("")
print("---- EOD ----")
