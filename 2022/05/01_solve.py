"""
In my first solution I skipped the input parsing, and just copied stacks by
hand. This solution includes the parser.

The parser rotates the input by 90degrees and then it's easy to parse line by
line instead of column by column.

It's important to not strip the input as this would break the stacks that are
to the left of the highest stack.
"""

input_files = [
    "test",
    "input",
]


def main(inp):
    stacks, lines = inp.split("\n\n")
    stacks = stacks.splitlines()
    stacks = zip(*stacks)

    out = []
    for s in stacks:
        temp = []
        s = s[::-1]
        if not s[0].isdigit():
            continue

        for c in s[1:]:
            if c.isalpha():
                temp.append(c)
        out.append(temp)

    stacks = out

    def process(x: list[str], p2=False):
        stacks = [list(s) for s in x]
        stacks = {i: s for i, s in enumerate(stacks, start=1)}

        ans = 0
        for line in lines.splitlines():
            _, q, _, start, _, end = line.split()
            q = int(q)
            start = int(start)
            end = int(end)
            if p2:
                temp = stacks[start][-q:]
                stacks[end].extend(temp)

            for _ in range(q):
                xx = stacks[start].pop()
                if not p2:
                    stacks[end].append(xx)

        ans = []
        for v in stacks.values():
            ans += v[-1]
        ans = "".join(ans)
        return ans


    ans = process(stacks)
    print("Part1", ans)

    ans = process(stacks, p2=True)
    print("Part2", ans)

if __name__ == "__main__":
    for file in input_files:
        print("\n" + file)
        with open(file) as fd:
            # NOTE: it's important to not strip() the input today
            inp = fd.read()

        main(inp)
