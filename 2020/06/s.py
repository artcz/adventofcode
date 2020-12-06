from collections import defaultdict

batches = open("input").read().strip().split("\n\n")

print("--- Day06 ---")


def p1():
    ans = 0
    for b in batches:
        bb = set(b.replace('\n', ''))
        ans += len(bb)

    print(ans)


def p2():
    ans = 0
    for b in batches:
        counter = defaultdict(int)
        lines = b.splitlines()

        for line in lines:
            for c in line:
                counter[c] += 1

        for k, v in counter.items():
            if v == len(lines):
                ans += 1

    print(ans)


print("Part1", end="=> ")
p1()
print("Part2", end="=> ")
p2()
print("---- EOD ----")
