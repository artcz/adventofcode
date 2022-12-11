import math
from collections import deque
from copy import deepcopy
from functools import reduce

input_files = [
    "test",
    "input",
]

def rect(inp):
    def play(arange):
        return math.prod(x["insp"]for x  in sorted(reduce( lambda a, b:(
        [([{**a[0][zi],"temp":(a[0][a[0][zi][([lambda r: r//3 ,lambda y:
        y,][b<0](a[0][zi]["op"](a[0][zi]["items"][0])))% a[0] [zi]["div"
        ]==0]]["items"].append(([lambda r:r//3,lambda y: y,][b< 0](a[0][
        zi]["op"](a[0][zi]["items"][0])))%a[1])),"insp":a[0][zi][ "insp"
        ]+count,"items": (a[0][zi]["items"], a[0][zi]["items"].pop(0))[0
        ],}for count in range(1, len(a[0][zi]["items"]) + 1)][-1]if len(
        a[0][zi]["items"]) else a[0][zi])for zi in range(len(a[0]))], a[
        1]),arange,reduce(lambda a,b:(a[0]+[b],a[1]* b["div"]),[{{"Star"
        "ting items":"items","Operation":"op", "Test":"div","If true":1,
        "If false":0,}.get(k, k):({"Starting items": lambda: [int(x) for
        x in v.split(",")],"Operation":lambda:eval(f"lambda old:{v[6:]}"
        ),"Test":lambda:int(v.split()[-1]), "If true":lambda:int(v[-1]),
        "If false":lambda:int(    # @artcz Advent of Code, 2022, Day 11.
        v[-1]),}.get(k,lambda:())()) for k,v in[[x.strip() for x in line
        .strip().split(":")] for line in para.splitlines() if"Mon"not in
        line]}|{"insp":0,"temp":None}for m, para in enumerate(inp.split(
        "\n\n" ))], ([], 1), ))[ 0 ], key = lambda x: -x["insp"] )[:2] )

    print(play(range(20)))
    print(play(range(-1, -10_001, -1)))


def main(inp):
    mod = 1
    M = {}
    for para in inp.split("\n\n"):
        for line in para.splitlines():
            if "Mon" in line:
                N = int(line[-2])

            if "Star" in line:
                items = [int(x) for x in line[18:].split(", ")]

            if "Op" in line:
                op = eval(f"lambda old: {line[18:]}")

            if "div" in line:
                div = int(line.split()[-1])

            if "true" in line:
                true = int(line[-1])

            if "false" in line:
                false = int(line[-1])

        M[N] = {
            "items": deque(items),
            "op": op,
            "div": div,
            True: true,
            False: false,
            "inspected": 0,
        }

        mod *= div

    def play(M, rounds, p1=True):
        for _ in range(rounds):
            for v in M.values():
                while v["items"]:
                    item = v["items"].popleft()
                    item = v["op"](item)
                    if p1:
                        item //= 3

                    test = item % v["div"] == 0
                    M[v[test]]["items"].append(item % mod)
                    v["inspected"] += 1

        ans = sorted([x["inspected"] for x in M.values()])[-2:]
        return math.prod(ans)

    M1 = deepcopy(M)
    ans = play(M1, 20)
    print("Part1", ans)

    M2 = deepcopy(M)
    ans = play(M2, 10_000, p1=False)
    print("Part2", ans)


if __name__ == "__main__":
    print("\n" * 60)
    for file in input_files:
        print("\n" + file)
        with open(file) as fd:
            inp = fd.read().strip()

        main(inp)
        rect(inp)
