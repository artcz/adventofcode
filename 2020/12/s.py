lines = open("input").read().strip().splitlines()

print("--- Day12 ---")


def p1():
    x, y = 0, 0
    orient = "E"

    for step in lines:
        direction = step[0]
        count = int(step[1:])

        dds = {
            "N": (0, +1),
            "S": (0, -1),
            "E": (+1, 0),
            "W": (-1, 0),
        }

        if direction in "LR":
            dirs = "NWSE"
            count //= 90
            orient = dirs.index(orient) + {"L": count, "R":-count}[direction]
            orient = dirs[orient % len(dirs)]
            continue

        if direction in dds:
            dx, dy = dds[direction]
        elif direction == "F":
            dx, dy = dds[orient]

        x += dx * count
        y += dy * count

    print(man((x, y), (0, 0)))


def p2():
    sx, sy = 0, 0
    wx, wy = 10, 1

    for step in lines:
        direction = step[0]
        count = int(step[1:])

        dds = {
            "N": (0, +1),
            "S": (0, -1),
            "E": (+1, 0),
            "W": (-1, 0),
        }

        if direction in dds:
            dx, dy = dds[direction]
            wx += dx * count
            wy += dy * count

        elif direction == "L":
            for _ in range(count // 90):
                wx, wy = -wy, wx

        elif direction == "R":
            for _ in range(count // 90):
                wx, wy = wy, -wx

        elif direction == "F":
            sx += wx * count
            sy += wy * count

    print(man((sx, sy), (0, 0)))


def man(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


print("Part1")
p1()
print("Part2")
p2()
print("---- EOD ----")
