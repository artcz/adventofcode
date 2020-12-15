from operator import mul
from sympy.ntheory.modular import crt

lines = open("input").read().strip().splitlines()


def p1():
    timestamp = int(lines[0])
    desc = lines[1].split(",")

    buses = [int(x) for x in desc if x != "x"]

    bs = []
    for b in buses:
        bs.append((b - timestamp % b, b))

    mi = min(bs)
    print(mul(*mi))


def p2naive():
    """Good for small inputs"""
    desc = lines[1].split(",")
    buses = [(i, int(x)) for i, x in enumerate(desc) if x != "x"]

    t = 0
    while True:
        if all((t + i) % b == 0 for i, b in buses):
            print("p2add:", t)
            break

        t += buses[0][1]


def p2crt():
    desc = lines[1].split(",")
    buses = [(i, int(x)) for i, x in enumerate(desc) if x != "x"]

    mods = [b[1] - b[0] for b in buses]
    divs = [b[1] for b in buses]

    print("p2crt:", crt(divs, mods)[0])


p1()
p2crt()
# p2naive()
