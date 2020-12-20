"""
No sparation into p1() and p2() today, there's no point...
Just global variables and global everything...

"""
import math
from collections import defaultdict, deque

tiles_ = open("input").read().strip().split("\n\n")
# tiles_ = open("test").read().strip().split("\n\n")


# Those functions implement transformations
def rot90(tile):
    # zip will also flip so we need to unflip
    zz = ["".join(z) for z in list(zip(*tile))[::-1]]
    return zz


def rot180(tile):
    return rot90(rot90(tile))


def rot270(tile):
    return rot90(rot90(rot90(tile)))


def flip_h(tile):
    return [line[::-1] for line in tile]


def flip_v(tile):
    return tile[::-1]


def flip_v_rot90(tile):
    return flip_v(rot90(tile))


def flip_h_rot90(tile):
    return flip_h(rot90(tile))


def nop(tile):
    return tile


# Those are the functions to get the edges
def top(tile):
    return tile[0]


def bottom(tile):
    return tile[-1]


def left(tile):
    return "".join([x[0] for x in tile[::-1]])


def right(tile):
    return "".join([x[-1] for x in tile[::-1]])


tiles = {}
for tile in tiles_:
    enum, *rest = tile.splitlines()
    enum = int(enum.split()[1].strip(":"))
    tiles[enum] = rest

EDGES = defaultdict(lambda: defaultdict(set))
Ecount = defaultdict(int)

size = int(len(tiles) ** 0.5)

transformations = [
    nop,
    flip_h,
    flip_v,
    rot90,
    rot180,
    rot270,
    flip_h_rot90,
    flip_v_rot90,
]

# This will be used as a base set to compare options against it, hence why it
# includes all possible tiles in all legal premutations
alloptions = {(op, t) for op in transformations for t in tiles}


# This part computes all the edges going to the right or down the bottom.
# We will use this part later for lookup when building the grid.
for tile_id, t1 in tiles.items():
    t1og = t1

    for op1 in transformations:
        t1 = op1(t1og)

        for tile2_id, t2 in tiles.items():
            if tile_id == tile2_id:
                continue

            for op2 in transformations:
                if right(t1) == left(op2(t2)):
                    EDGES[(op1, tile_id)]["R"].add((op2, tile2_id))
                    Ecount[tile_id] += 1

                if bottom(t1) == top(op2(t2)):
                    EDGES[(op1, tile_id)]["B"].add((op2, tile2_id))
                    Ecount[tile_id] += 1


# For Part1 we don't actually need to solve the puzzle, we can just count the
# number of edges. Corners will have only two edges, sides will have 3, center
# pieces will have 4.
corners = [k for k, v in Ecount.items() if v // 4 == 2]
print("Part1", math.prod(corners))

# For Part2 we actually need to solve the puzzle.
# This is a BFS-ish solution, starting with an empty grid, and, to simplify the
# number of operations we need to handle, we just go left to right, top to
# bottom from (0, 0) (top left), and then check one square up and one square to
# the left to match the tile.
# To simplify how many cases we need to check we can seed with  one of the
# corners found in part1. It shouldn't matter which one we'll pick, but just in
# case we're going to add all of them.
# They are added with all the various transformations we could apply to them.

Q = deque()
for option in alloptions:
    grid = [[None for _ in range(size)] for _ in range(size)]
    orient, number = option
    if number in corners:
        grid[0][0] = option
        Q.append((grid))


while Q:
    grid = Q.popleft()

    if all(all(row) for row in grid):
        # it finds 8 grids, we can break after first one, because they should
        # all be veriants of the same grid but with different transformations
        # which we apply later anyway
        break

    # Find the first blank spot going left to right and top to bottom, and then
    # check what are the options. If nothing can be found, break the loop.
    # If something can be found, queue all the options and break, because
    # there's no point in checking other empty squares at this point.
    for y in range(size):
        for x in range(size):
            # Skip the fields that are already filled in.
            if grid[y][x] is not None:
                continue

            up = grid[y - 1][x] if y > 0 else None
            lf = grid[y][x - 1] if x > 0 else None

            up = EDGES[up]["B"] if up else alloptions
            lf = EDGES[lf]["R"] if lf else alloptions

            available = up & lf

            if not available:
                break

            for av in available:
                newgrid = [row[:] for row in grid]
                newgrid[y][x] = av
                Q.append(newgrid)

            break
        else:
            continue
        break


def remove_stitches(tile):
    assert len(tile) == len(tile[0])
    tile = tile[1:-1]

    ntile = []
    for row in tile:
        ntile.append(row[1:-1])
    assert len(ntile) == len(ntile[0])
    return ntile


def picture(grid):
    pic = []
    for grid_row in grid:
        bigrow = defaultdict(list)

        for tile in grid_row:
            for i, row in enumerate(tile):
                bigrow[i].append(row)

        for i in range(8):
            arow = "".join(bigrow[i])
            pic.append(arow)

    return pic


without_stitches = [
    [remove_stitches(op(tiles[tile])) for op, tile in row] for row in grid
]

apic = picture(without_stitches)


def search_for_monsters(pic):
    monster = [
        "..................#.",
        "#....##....##....###",
        ".#..#..#..#..#..#...",
    ]

    coords = []
    for y, line in enumerate(monster):
        for x in [i for i, ch in enumerate(line) if ch == "#"]:
            coords.append((x, y))

    ogpic = pic
    dragons = 0

    for trans in transformations:
        pic = [list(row) for row in trans(ogpic)]
        size = len(pic)
        assert size == len(pic[0]), (trans, len(pic[0]), size)

        for y in range(size):
            for x in range(size):
                try:
                    if all(pic[y + dy][x + dx] == "#" for dx, dy in coords):
                        dragons += 1
                        for dx, dy in coords:
                            pic[y + dy][x + dx] = "0"
                except IndexError:
                    pass

        # Dragons seems to be only on one of the versions, so if we found a
        # dragon we don't check other transformations.
        # Otherwise we would overwrite pic below and return a number without
        # the monsters subtracted
        if dragons:
            break

    pic = "\n".join(["".join(row) for row in pic])
    print("Part2", pic.count("#"))


search_for_monsters(apic)
