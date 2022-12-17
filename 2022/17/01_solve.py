from collections import defaultdict

input_files = [
    "test",
    "input",
]


EMPTY = "."
SOLID = "#"
MOVING = "@"

Shapes = \
"""@@@@

.@.
@@@
.@.

..@
..@
@@@

@
@
@
@

@@
@@""".strip().split("\n\n")


def print_grid(grid, maxx, maxy):
    header = ["    "]
    for x in range(maxx):
        header.append(str(x % 10))

    print("".join(header))

    for y in range(maxy):
        row = [str(y).zfill(3), " "]
        for x in range(maxx):
            row.append(grid[y, x])

        print("".join(row))



def main(inp):
    lines = inp.splitlines()
    G = defaultdict(lambda: EMPTY)
    jets = lines[0]

    # This needs to be big, because we will take min later.
    highest = 1e9

    # The actual value of R is not relevant, because we use a growing dict, and
    # the only thing that matters later is a delta with this number. However
    # keeping it reasonably small allows us to make an easier visualisation of
    # the bottom few rows for sanity checks.
    R = 30
    spawn = R - 3
    C = 7

    def place(G, topleft, shape):
        # Let's just do horizontal shape for now
        r, c = topleft
        for rr, row in enumerate(shape):
            for cc, ch in enumerate(row):
                if ch == MOVING:
                    G[r+rr, c+cc] = ch

    def move(G, topleft, shape, dr, dc):
        r, c = topleft
        copy = {}
        for rr, row in enumerate(shape):
            for cc, ch in enumerate(row):
                if ch == MOVING:
                    copy[r+rr, c+cc] = ch
                    # I wasted a lot of time here, because this line wasn't
                    # indented correctly. Remember to only remove items that
                    # are already copied :)
                    G[r+rr, c+cc] = EMPTY

        for rr, cc in copy:
            G[rr+dr, cc+dc] = copy[rr, cc]

        # Returns updated top left
        return r+dr, c+dc

    def can_move(G, topleft, shape, dr, dc):
        r, c = topleft

        # Moving right
        if dc > 0:
            # First case is the edge
            for rr, line in enumerate(shape):
                for cc, ch in enumerate(line):
                    if ch == MOVING and c + cc + dc >= C:
                        return False

            # Second is the collision with existing piece
            for rr, line in enumerate(shape):
                for cc, ch in enumerate(line):
                    if ch == MOVING and G[r+rr, c+cc+dc] == SOLID:
                        return False


        # Moving left
        elif dc < 0:
            # Edge
            for rr, line in enumerate(shape):
                for cc, ch in enumerate(line):
                    if ch == MOVING and c + cc + dc < 0:
                        return False

            for rr, line in enumerate(shape):
                for cc, ch in enumerate(line):
                    if ch == MOVING and G[r+rr, c+cc+dc] == SOLID:
                        return False

        # using elif because we don't support diagonal moves.
        # Only one of (row, col) at the time.
        elif dr > 0:
            # Check every cell, because shapes have holes
            for rr, line in enumerate(shape):
                for cc, ch in enumerate(line):
                    if ch == MOVING and G[r+rr+dr, c+cc] == SOLID:
                        return False

        elif dr < 0:
            # I can skip this because we never move up
            assert False  # for now

        return True

    def toprow(G, spawn_row):
        # Looks like having location of all the highest items relative to
        # spawn location is enough to find the cycle.
        offsets = []
        for c in range(C):
            r = 0
            while G[spawn_row+r, c] != SOLID:
                r += 1
            offsets.append(r)

        return offsets

    def fingerprint(G, piece, spawn, wind):
        # Assume we can fingerprint spawn location, and don't need to
        # fingerprint anything else.
        tt = toprow(G, spawn)
        return (tuple(tt), piece, wind)

    # instead of implementing collisions with the bottom, we can just add a
    # bottom.
    # We could probably do the same for columns -1 and 7.
    for c in range(C):
        G[R, c] = SOLID

    current_jet = 0
    SEEN = set()
    found = None
    cycle = {}

    # Enough to find a cycle for part2
    rocks = 10_000
    save = {}
    for i in range(rocks):
        shape = Shapes[i%len(Shapes)].splitlines()
        r, c = spawn - len(shape) , 2

        save[i] = R - highest

        # if i == 2022:
        #     ans = abs(R-highest)
        #     print("Part1", ans)

        if i >= 1:
            # To find the cycle you need to check if the state is going to
            # repeat. That means you need to check if:
            # * tetramino is going to be the same
            # * jets are in the same position
            # * the board (or at least top of the board) is in the same
            # position.
            ff = fingerprint(G, i%len(Shapes), spawn, current_jet % len(jets))
            if ff in SEEN and found == ff:
                # This will trigger when we hit the cycle *2nd* time.
                # Hence why the formula for left offset is using (-2)
                # The reason why we do this when we hit the second cycle is so
                # we can easily set up extra tracking once we know for sure
                # we're inside the cycle.
                # Because of that we don't have to do more math on `save`
                # indexes and instead we can just look through `cycle`
                def computefor(rounds):
                    loff = i-2*len(cycle)
                    roff = (rounds - loff) % len(cycle)
                    repeats = (rounds - loff - roff) / len(cycle)
                    cyclevalue = cycle[len(cycle)-1]

                    result = save[loff-1] + repeats * cyclevalue + cycle[roff]
                    return int(result)

                # Since the cycle is less than 2022, once we have the cycle
                # length and all the other data, we can recompute the result
                # for 2022, without breaking out of the loop at 2022
                print("Part1", computefor(2022))
                print("Part2", computefor(1000000000000))
                return


            if ff in SEEN and not found:
                found = ff
                cycle_start = i
                height_at_cycle_start = prev

            if ff in SEEN and found:
                cycle[i-cycle_start] = abs(highest - height_at_cycle_start)

            SEEN.add(ff)
            prev = highest

        place(G, (r,c), shape)

        bottom = False
        gg = lambda: print_grid(G, C, R)
        interactive = False

        while 1:
            jet = jets[current_jet%len(jets)]
            if interactive:
                gg()
                print(f"Next {jet}")
                input()

            # Increment after interactive - this is just to make debugging
            # clearer
            current_jet += 1

            # First check the left/right movement
            dc = "< >".index(jet)-1
            if can_move(G, (r, c), shape, dr=0, dc=dc):
                r, c = move(G, (r, c), shape, dr=0, dc=dc)

            # Then, check if it can fall down
            if not can_move(G, (r, c), shape, dr=+1, dc=0):
                # When we find the bottom we convert a moving shape into
                # stationary object. Because moving and stationary objects
                # use different characters we don't have to worry about
                # items coliding with themselves when moving.
                # NOTE: shapes are at most 4x4 so just scan that range.
                for gr in range(4):
                    for gc in range(4):
                        if G[r+gr, c+gc] == MOVING:
                            G[r+gr, c+gc] = SOLID

                bottom = True
            else:
                r, c = move(G, (r, c), shape, dr=+1, dc=0)

            if bottom:
                spawn = min(spawn, r-3)
                highest = min(r, highest)
                break


if __name__ == "__main__":
    print("\n" * 60)
    for file in input_files:
        print("\n" + file)
        with open(file) as fd:
            inp = fd.read().strip()

        main(inp)
