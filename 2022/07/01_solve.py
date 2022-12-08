from collections import defaultdict

input_files = [
    "test",
    "input",
]


def main(inp):
    lines = inp.splitlines()
    path = []
    FS = defaultdict(int)
    for line in lines:
        x = line.split()
        if len(x) == 3:
            assert line.startswith("$ cd")

            if x[2] == "..":
                path.pop()
            else:
                path.append(x[2])

        elif len(x) == 2:
            if x[0].isdigit():
                temp = path[:]
                while temp:
                    FS["/".join(temp)] += int(x[0])
                    temp.pop()

    ans = sum(v for v in FS.values() if v < 100_000)
    print("Part1", ans)

    total = 70000000
    root = total - FS["/"]
    target = 30000000 - root

    ans = min(v for v in FS.values() if v > target)
    print("Part2", ans)


if __name__ == "__main__":
    for file in input_files:
        print("\n" + file)
        with open(file) as fd:
            inp = fd.read().strip()

        main(inp)
