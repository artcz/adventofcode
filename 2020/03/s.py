lines = open("input").read().strip().splitlines()

# lines = """
# ..##.......
# #...#...#..
# .#....#..#.
# ..#.#...#.#
# .#...##..#.
# ..#.##.....
# .#.#.#....#
# .#........#
# #.##...#...
# #...##....#
# .#..#...#.#
# """.strip().splitlines()


def p1():
    TREE = "#"

    pos = [0, 0]
    trees = 0

    while True:
        pos[0] += 3
        pos[1] += 1
        x, y = pos

        try:
            if lines[y][x % len(lines[0])] == TREE:
                trees += 1
        except IndexError:
            break

    print(trees)


p1()


def p2():
    TREE = "#"

    ans = 1

    for slope in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        pos = [0, 0]
        trees = 0
        while True:
            pos[0] += slope[0]
            pos[1] += slope[1]
            x, y = pos

            try:
                if lines[y][x % len(lines[0])] == TREE:
                    trees += 1
            except IndexError:
                print(x, y, trees)
                break

        ans *= trees

    print(ans)


p2()
