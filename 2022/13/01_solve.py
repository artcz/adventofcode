import functools

input_files = [
    "test",
    "input",
]


def main(inp):
    lines = inp.splitlines()

    def compare(a, b):
        if isinstance(a, int) and isinstance(b, int):
            if a < b: return -1
            elif a == b: return 0
            else: return 1

        if isinstance(a, list) and isinstance(b, int):
            b = [b]

        if isinstance(a, int) and isinstance(b, list):
            a = [a]

        if isinstance(a, list) and isinstance(b, list):
            for l, r in zip(a, b):
                c = compare(l, r)
                if c != 0: return c

            if len(a) < len(b): return -1
            elif len(a) == len(b): return 0
            else: return 1

    ans = []
    pairs = [x.splitlines() for x in inp.split("\n\n")]
    for i, (a, b) in enumerate(pairs, start=1):
        a = eval(a)
        b = eval(b)
        c = compare(a, b)
        if c == -1:
            ans += [i]

    ans = sum(ans)
    print("Part1", ans)

    ans = 0
    lines = []
    for line in inp.splitlines():
        if not line:
            continue

        lines.append(eval(line))

    lines.append([[2]])
    lines.append([[6]])

    ll = sorted(lines, key=functools.cmp_to_key(compare))
    two = ll.index([[2]]) + 1
    six = ll.index([[6]]) + 1
    ans = two * six
    print("Part2", ans)


if __name__ == "__main__":
    print("\n" * 60)
    for file in input_files:
        print("\n" + file)
        with open(file) as fd:
            inp = fd.read().strip()

        main(inp)
