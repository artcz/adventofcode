
input_files = [
    "test",
    "input",
]


def main(inp):
    lines = inp.splitlines()
    ans1 = 0
    ans2 = 0
    for line in lines:
        a, b = line.split(',')
        a, aa = a.split('-')
        b, bb = b.split('-')
        a, aa, b , bb = int(a), int(aa), int(b), int(bb)
        if a <= b and aa >= bb:
            ans1 += 1
        elif b <= a and bb >= aa:
            ans1 += 1

        found = 0
        for i in range(a, aa+1):
            for j in range(b, bb+1):
                if i == j:
                    ans2 += 1
                    found = 1
                    break

            if found:
                break


    print("Part1", ans1)
    print("Part2", ans2)


if __name__ == "__main__":
    for file in input_files:
        print("\n" + file)
        with open(file) as fd:
            inp = fd.read().strip()

        main(inp)
