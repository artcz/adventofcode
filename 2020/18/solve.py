import operator

lines = open("input").read().strip().splitlines()

print("\nDay 17", "-" * 78, "\n")


def stackeval(stack):
    op = None
    n = int(stack[0])

    for s in stack[1:]:
        if s == "*":
            op = operator.mul
        elif s == "+":
            op = operator.add
        else:
            n = op(n, int(s))

    return n


def parse(expr, i, evalfunc):
    stack = []
    while i < len(expr):
        ch = expr[i]

        if ch == ")":
            return evalfunc(stack), i

        elif ch == "(":
            val, i = parse(expr, i + 1, evalfunc)
            stack.append(val)

        else:
            stack.append(ch)

        i += 1

    return evalfunc(stack)


def stackeval_p2(stack):
    """
    Hack: First eval all additions, then use regular stackeval on the rest
    """
    pos = 0

    while "+" in stack:
        if stack[pos] == "+":
            arg1, op, arg2 = stack[pos - 1 : pos + 2]
            arg1, arg2 = int(arg1), int(arg2)
            stack = stack[: pos - 1] + [arg1 + arg2] + stack[pos + 2 :]
            pos = 0
        else:
            pos += 1

    # NOTE: this part is optional, but it shows that more operators could be
    # added here. Eventually while all operators are evaluated the stack should
    # be len == 1. However, if there's one operator with higher priority than
    # the rest, we could simply pass this to the original stackeval to deal
    # with the rest of the stack.
    # Because the puzzle is using only + and * this entire part is optional.
    while "*" in stack:
        if stack[pos] == "*":
            arg1, op, arg2 = stack[pos - 1 : pos + 2]
            arg1, arg2 = int(arg1), int(arg2)
            stack = stack[: pos - 1] + [arg1 * arg2] + stack[pos + 2 :]
            pos = 0
        else:
            pos += 1

    # NOTE: This assertion is only true if we implement all the available
    # operators in this function.
    assert len(stack) == 1

    return stackeval(stack)


def p1():
    ans = 0
    for line in lines:
        line = line.replace(" ", "")
        ans += parse(line, 0, stackeval)

    print()
    print("ANSP1", ans)


def p2():
    ans = 0
    for line in lines:
        line = line.replace(" ", "")
        ans += parse(line, 0, stackeval_p2)

    print()
    print("ANSP2", ans)


print("Part1", "-" * 79)
print()
p1()
print()
print("\nPart2", "-" * 79)
print()
p2()
print("\n---- EOD ----")
