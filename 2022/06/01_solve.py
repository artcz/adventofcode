
input_files = [
    "test",
    "input",
]


def main(inp):
    lines = inp.splitlines()
    line = lines[0]
    def find(size):
        ans = size - 1
        for x in zip(*[line[x:] for x in range(size)]):
            ans += 1
            if len(set(x)) == size:
                break

        return ans

    ans = find(size=4)
    print("Part1", ans)

    ans = find(size=14)
    print("Part2", ans)


if __name__ == "__main__":
    for file in input_files:
        print("\n" + file)
        with open(file) as fd:
            inp = fd.read().strip()

        main(inp)
