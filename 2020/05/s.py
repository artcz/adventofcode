"""
This is a slightly nicer version than the one I used to get the stars, but
works on the same premise.

I didn't notice that you could just cast to int() and hence performed a binary
search on a list instead...

For part2 I originally did `for r in range(11, 111): ...` as this worked well
for my input, but I replaced it here with a more general solution as per the
puzzle description.
"""
lines = open("input").read().strip().splitlines()

print("--- Day05 ---")


def p1():
    maxsid = 0
    for line in lines:
        row = [*range(128)]
        col = [*range(8)]

        for c in line:
            if c == "F":
                row = row[: len(row) // 2]
            elif c == "B":
                row = row[len(row) // 2 :]
            elif c == "L":
                col = col[: len(col) // 2]
            elif c == "R":
                col = col[len(col) // 2 :]

        sid = row[0] * 8 + col[0]
        maxsid = max(maxsid, sid)

    print(maxsid)


def p2():
    seats = {}
    for line in lines:
        row = [*range(128)]
        col = [*range(8)]

        for c in line:
            if c == "F":
                row = row[: len(row) // 2]
            elif c == "B":
                row = row[len(row) // 2 :]
            elif c == "L":
                col = col[: len(col) // 2]
            elif c == "R":
                col = col[len(col) // 2 :]

        sid = row[0] * 8 + col[0]
        seats[row[0], col[0]] = sid

    for (r, c), sid in seats.items():
        if sid - 2 in seats.values() and sid - 1 not in seats.values():
            print(r * 8 + c - 1)


print("Part1", end="=> ")
p1()
print("Part2", end="=> ")
p2()
print("---- EOD ----")
