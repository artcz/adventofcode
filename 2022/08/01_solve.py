
input_files = [
    "test",
    "input",
]


def main(inp):
    lines = inp.splitlines()

    G = {}
    for h, line in enumerate(lines):
        for w, ch in enumerate(line):
            G[h, w] = int(ch)

    h = len(lines)
    w = len(lines[0])

    def check(r, c):
        val = G[r, c]
        S = [G[rr, c] < val for rr in range(r+1, w)]
        N = [G[rr, c] < val for rr in range(r-1, -1, -1)]
        W = [G[r, cc] < val for cc in range(c-1, -1, -1)]
        E = [G[r, cc] < val for cc in range(c+1, w)]

        return any(all(x) for x in [N, E, W, S])

    def score(r, c):
        val = G[r, c]

        def sc(x):
            if False in x:
                return x.index(False) + 1
            return len(x)

        S = sc([G[rr, c] < val for rr in range(r+1, w)])
        N = sc([G[rr, c] < val for rr in range(r-1, -1, -1)])
        W = sc([G[r, cc] < val for cc in range(c-1, -1, -1)])
        E = sc([G[r, cc] < val for cc in range(c+1, w)])

        return N * E * W * S

    ans1 = 0
    ans2 = 0
    for r in range(0, h):
        for c in range(0, w):
            if check(r, c):
                ans1 += 1
            ans2 = max(ans2, score(r, c))

    print("Part1", ans1)
    print("Part2", ans2)


if __name__ == "__main__":
    for file in input_files:
        print("\n" + file)
        with open(file) as fd:
            inp = fd.read().strip()

        main(inp)
