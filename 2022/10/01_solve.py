from functools import reduce

input_files = [
    "test",
    "input",
]


def golf(inp):

    print(
        sum(
            i * x
            for i, x in enumerate(
                reduce(
                    lambda a, b: a
                    + [a[-1] if b[0] == "n" else a[-1] + int(b.split()[1])]
                    * (2 if b[0] == "a" else 1),
                    inp.splitlines()[:-2],
                    [1, 1],
                ),
                start=1,
            )
            if i in range(20, 220 + 1, 40)
        )
    )

    print(
        "\n".join(
            "".join(line)
            for line in reduce(
                lambda a, b: (
                    [[str(int(a[0][0]) + (b[3]*b[4] if b[3] % 40 == 20 else 0))]]
                    + a[1: b[0]+1]
                    + [a[b[0]+1][: b[1]] + [("#" if b[2] else " ")] + a[b[0] + 1][b[1] + 1 :]]
                    + a[b[0] + 2 :]
                ),
                (
                    (t // 40, t % 40, abs(x - (t % 40)) < 2, t+1, x)
                    for t, x in enumerate(
                        reduce(
                            lambda a, b: a
                            + [a[-1] if b[0] == "n" else a[-1] + int(b.split()[1])]
                            * (2 if b[0] == "a" else 1),
                            inp.splitlines()[:-2],
                            [1, 1],
                        )
                    )
                ),
                [["0"]] + [["" for _ in range(40)] for _ in range(6)],
            )
        )
    )


def main(inp):
    lines = inp.splitlines()

    X = 1
    ptr = 0
    wait = 0
    tick = 0
    ans = {}
    log = []

    while ptr < len(lines):
        tick += 1

        log.append(X)
        if tick in [20, 60, 100, 140, 180, 220]:
            ans[tick] = X

        line = lines[ptr]

        if line == "noop":
            ptr += 1
            continue

        _, arg = line.split()
        arg = int(arg)

        if not wait:
            wait = 1
            continue
        else:
            X += arg
            wait = 0

        ptr += 1

    ans = sum(k * v for k, v in ans.items())
    print(ans)

    W = 40
    H = 6
    G = [[" " for _ in range(W)] for _ in range(H)]

    for t, x in enumerate(log):
        if abs(x - (t % W)) < 2:
            G[t // W][t % W] = "#"

    for line in G:
        print("".join(line))


if __name__ == "__main__":
    print("\n" * 60)
    for file in input_files:
        print("\n" + file)
        with open(file) as fd:
            inp = fd.read().strip()

        print("Original:")
        main(inp)
        print("\nAs reducer:")
        golf(inp)
