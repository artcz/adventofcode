import itertools

lines = open("input").read().strip().splitlines()

print("\nDay 17", "-" * 78, "\n")


def n_dim_gol(lines, D, cycles):
    G = set()

    for y, line in enumerate(lines):
        for x, ch in enumerate(line):
            if ch == "#":
                G.add((x, y) + (0,) * (D - 2))

    for cycle in range(cycles):
        NG = set()
        # print(cycle)

        borders = []
        for d in range(D):
            max_ = max(G, key=lambda x: x[d])[d]
            min_ = min(G, key=lambda x: x[d])[d]
            borders.append((min_, max_))

        nbs = [n for n in itertools.product((-1, 0, 1), repeat=D) if n != (0,) * D]

        coordinates = itertools.product(
            *[range(bmin - 1, bmax + 2) for bmin, bmax in borders]
        )

        for k in coordinates:
            nk = [tuple((k0 + d) for k0, d in zip(k, n)) for n in nbs]

            active = sum(c in G for c in nk)

            if k in G and active in (2, 3):
                NG.add(k)

            elif k not in G and active == 3:
                NG.add(k)

        G = NG

    return G


def p1():
    G = n_dim_gol(lines, 3, 6)
    print(len(G))


def p2():
    G = n_dim_gol(lines, 4, 6)
    print(len(G))


print("Part1", "-" * 79)
print()
p1()
print()
print("\nPart2", "-" * 79)
print()
p2()
print("\n---- EOD ----")
