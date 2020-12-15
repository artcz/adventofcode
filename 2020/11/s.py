lines = open("input").read().strip().splitlines()


print("--- Day11 ---")


class Seat:

    directions = [
        (dx, dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1] if (dx, dy) != (0, 0)
    ]

    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy


def p1(part2=False):
    G, rows, columns = load_grid(lines)

    i = 0
    while True:
        i += 1
        NG = {}
        for x in range(rows):
            for y in range(columns):
                other = [Seat(x + d[0], y + d[1], *d) for d in Seat.directions]
                adjacent = 4

                if part2:
                    for seat in other:
                        while G.get((seat.x, seat.y)) == ".":
                            seat.x += seat.dx
                            seat.y += seat.dy

                    adjacent = 5

                other = [G[s.x, s.y] for s in other if (s.x, s.y) in G]

                if G[x, y] == "L" and all(s != "#" for s in other):
                    NG[x, y] = "#"

                elif G[x, y] == "#" and (sum([s == "#" for s in other]) >= adjacent):
                    NG[x, y] = "L"

                else:
                    NG[x, y] = G[x, y]

        if G == NG:
            break

        G = NG

    print(sum([cell == "#" for cell in G.values()]))


def p2():
    p1(part2=True)


def load_grid(lines):
    G = {}
    first_row = lines[0]
    for y, line in enumerate(lines):
        # Check if grid is really a grid.
        assert len(line) == len(first_row)
        for x, ch in enumerate(line):
            G[y, x] = ch

    rows = len(lines)
    columns = len(first_row)
    return G, rows, columns


def print_grid(grid, maxx, maxy, zfill_padding=3):
    header = [" " * zfill_padding, " "]
    for x in range(maxx):
        header.append(str(x % 10))

    print("".join(header))

    for y in range(maxy):
        row = [str(y).zfill(zfill_padding), " "]
        for x in range(maxx):
            row.append(grid[x, y])

        print("".join(row))


print("Part1")
p1()
print("Part2")
p2()
print("---- EOD ----")
