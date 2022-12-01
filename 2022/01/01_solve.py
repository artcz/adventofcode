
def main(inp):
    batches = inp.split("\n\n")

    sums = []
    for b in batches:
        sums.append(sum(int(x) for x in b.splitlines()))

    sums.sort()
    ans = sum(sums[-1:])
    print("Part1", ans)

    ans = sum(sums[-3:])
    print("Part2", ans)



if __name__ == "__main__":
    file = "input"
    with open(file) as fd:
        inp = fd.read().strip()
        main(inp)
