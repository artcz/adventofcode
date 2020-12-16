from collections import defaultdict

batches = open("input").read().strip().split("\n\n")


print("\nDay 16", "-" * 78, "\n")


def parse_validators(validations):
    validators = {}
    Vs = []

    for line in validations.splitlines():
        name, things = line.split(": ")
        things = things.split(" or ")

        v0 = [int(x) for x in things[0].split("-")]
        v1 = [int(x) for x in things[1].split("-")]

        # Make it easier to validate with any() below, without chaining
        Vs.append(v0)
        Vs.append(v1)

        validators[name] = (v0, v1)

    return Vs, validators


def p1():
    validations, myticket, othertickets = batches

    Vs, _ = parse_validators(validations)

    wrong = []
    for i, ticket in enumerate(othertickets.splitlines()[1:]):
        fields = [int(x) for x in ticket.split(",")]
        for f in fields:
            for v in Vs:
                if v[0] <= f <= v[1]:
                    break
            else:
                wrong.append(f)

    print(sum(wrong))


def p2():
    validations, myticket, othertickets = batches

    Vs, validators = parse_validators(validations)

    valid_tickets = []
    for i, ticket in enumerate(othertickets.splitlines()[1:]):
        fields = [int(x) for x in ticket.split(",")]
        valid = True
        for f in fields:
            if any(v[0] <= f <= v[1] for v in Vs):
                valid = valid and True
            else:
                valid = False

        if valid:
            valid_tickets.append(fields)

    # This is the best idea I could come up with xD
    G = defaultdict(set)
    for i, row in enumerate(valid_tickets):
        for j, column in enumerate(row):
            for k, v in validators.items():
                if v[0][0] <= column <= v[0][1] or v[1][0] <= column <= v[1][1]:
                    G[i, j].add(k)

    myticket = myticket.splitlines()[1]
    myticket = [int(x) for x in myticket.split(",")]

    options = defaultdict(set)
    for c in range(len(myticket)):
        valid = validators.keys()
        for r in range(len(valid_tickets)):
            valid = valid & G[r, c]

        for k in valid:
            options[k].add(c)

    positions = {}
    while any(options.values()):
        for o in options:
            if not options[o]:
                continue

            if len(options[o]) == 1:
                val = options[o].pop()
                positions[o] = val

                for o2 in options:
                    options[o2] = options[o2] - {val}

    positions = sorted([(k, v) for k, v in positions.items()], key=lambda x: x[1])
    positions = [v for k, v in positions if k.startswith("departure")]

    ans = 1
    for i in positions:
        ans *= myticket[i]

    print(ans)


print("Part1", "-" * 79)
print()
p1()
print()
print("\nPart2", "-" * 79)
print()
p2()
print("\n---- EOD ----")
