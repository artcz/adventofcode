lines = open("input").read().strip().splitlines()

print("--- Day08 ---")


def p1():
    ins = []
    for line in lines:
        line = line.split()
        op, arg = line
        arg = int(arg)
        ins.append((op, arg))

    i = 0
    Is = set()
    acc = 0
    while True:
        if i in Is:
            break
        Is.add(i)

        op, arg = ins[i]

        if op == "acc":
            acc += arg

        elif op == "jmp":
            i += arg
            continue

        i += 1

    print(acc)


def p2():
    ins = []
    for line in lines:
        line = line.split()
        op, arg = line
        arg = int(arg)
        ins.append((op, arg))

    def run(ins, times=10000):
        i = 0
        acc = 0
        counter = 0
        while True:
            counter += 1
            if counter > times:
                return

            try:
                op, arg = ins[i]
            except IndexError:
                print(acc)
                return

            if op == "acc":
                acc += arg

            elif op == "jmp":
                i += arg
                continue

            i += 1

    for i, _in in enumerate(ins):
        op, arg = _in
        if op == "jmp":
            newins = ins[:i] + [("nop", arg)] + ins[i + 1 :]
        elif op == "nop":
            newins = ins[:i] + [("jmp", arg)] + ins[i + 1 :]
        else:
            continue

        run(newins)


print("Part1", end="=> ")
p1()
print("Part2", end="=> ")
p2()
print("---- EOD ----")
