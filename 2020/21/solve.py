import itertools
from collections import defaultdict

lines = open("input").read().strip().splitlines()

print("--- Day21 ---")


def parse(lines):
    INGs = defaultdict(int)

    foods = []
    for line in lines:
        ingr, alergens = line.split("(contains ")
        ingr = ingr.split()
        alergens = alergens.strip(")").split(", ")
        foods.append((ingr, alergens))

        for ing in ingr:
            INGs[ing] += 1

    return foods, INGs


def p1():
    foods, INGs = parse(lines)

    matches = defaultdict(lambda: INGs.keys())
    for ingr, alergs in foods:
        for alg in alergs:
            matches[alg] &= set(ingr)

    matches = set(itertools.chain(*matches.values()))
    nomatches = INGs.keys() - matches

    ans = 0
    for n in nomatches:
        ans += INGs[n]

    print(ans)


def p2():
    foods, INGs = parse(lines)

    matches = defaultdict(lambda: INGs.keys())
    for ingr, alergs in foods:
        for alg in alergs:
            matches[alg] &= set(ingr)

    mapping = {}

    # This will produce multiple matches so now, we need to use the skills
    # developed in one of the previous days, and solve the sudoku. :)
    while any(len(v) != 0 for k, v in matches.items()):

        for k, v in matches.items():
            if len(v) != 1:
                continue

            val = v.pop()
            mapping[val] = k

            for k2, v2 in matches.items():
                if k2 != k:
                    matches[k2] -= {val}

    ans = sorted([(k, v) for k, v in mapping.items()], key=lambda x: x[1])
    ans = [x[0] for x in ans]
    print(",".join(ans))


print("\nPart1\n")
p1()
print("\nPart2\n")
p2()
print("\n---- EOD ----")
