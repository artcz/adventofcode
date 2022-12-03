import sys

def main(inp):
    lines = inp.splitlines()
    ans = 0

    def p(x):
        zz = (
            "abcdefghijklmnopqrstuvwxyz"
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        )
        return zz.index(x) + 1


    for line in lines:
        ll = len(line)//2
        a, b = line[:ll], line[ll:]

        ans += p((set(a) & set(b)).pop())

    print("Part1", ans)

    ans = 0

    batches, batch = [], []
    for i,line in enumerate(lines):
        if i > 0 and i % 3 == 0:
            batches.append(batch)
            batch = []
        batch.append(line)
    batches.append(batch)

    for b in batches:
        ans += p((set(b[0]) & set(b[1]) & set(b[2])).pop())

    print("Part2", ans)


if __name__ == "__main__":
    file = sys.argv[1]
    with open(file) as fd:
        inp = fd.read().strip()
        main(inp)
