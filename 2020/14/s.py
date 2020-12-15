from collections import deque

lines = open("input").read().strip().splitlines()

print("\nDay 14", "=" * 79)


def p1():
    mem = {}
    for line in lines:
        op, val = line.split(' = ')

        if op == 'mask':
            mask = val
            continue

        adr = op[4:-1]
        asbin = format(int(val), "036b")

        newval = [(b if m == 'X' else m) for b, m in zip(asbin, mask)]
        mem[adr] = ''.join(newval)

    print(sum(int(x, 2) for x in mem.values()))


def p2():
    mem = {}

    for line in lines:
        op, val = line.split(' = ')
        if op == 'mask':
            mask = val
            continue

        adr = op[4:-1]
        asbin = format(int(adr), "036b")

        # Seed with zero, and then seek until you find things of lenghts n+1.
        # neither prefix nor mask require padding that way, the final product
        # will have a leading zero. That leading zero is irrelevant because we
        # cast to int() later anyway.

        SEEN = []
        Q = deque()
        Q.append(['0'])
        while Q:
            prefix = Q.popleft()
            i = len(prefix) - 1

            if len(prefix) == len(mask) + 1:
                SEEN.append(''.join(prefix))

            elif mask[i] == '1':
                Q.append(prefix + ['1'])

            elif mask[i] == '0':
                Q.append(prefix + [asbin[i]])

            elif mask[i] == 'X':
                Q.append(prefix + ['1'])
                Q.append(prefix + ['0'])

        for s in SEEN:
            mem[int(s, 2)] = int(val)

    print(sum(mem.values()))


print("Part1", "-" * 80)
print("")
p1()
print("")
print("Part2", "-" * 80)
print("")
p2()
print("")
print("---- EOD ----")
