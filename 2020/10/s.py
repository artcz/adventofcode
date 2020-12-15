from functools import lru_cache

lines = open("input").read().strip().splitlines()

print("--- Day10 ---")


def p1():
    numbers = sorted([int(x) for x in lines])
    numbers += [numbers[-1] + 3]
    ones, threes = 0, 0
    last = 0
    for n in numbers:
        if n - last == 1:
            ones += 1
        elif n - last == 3:
            threes += 1

        last = n

    print(threes * ones)


def p2a():
    """
    Proper, fast, DP solution
    """
    numbers = sorted([int(x) for x in lines])
    numbers = [0] + numbers

    partials = [sum(n + x in set(numbers) for x in range(1, 3 + 1)) for n in numbers]

    @lru_cache
    def find(i):
        p = partials[i]
        if p == 0:
            return 1

        out = 0
        for j in range(1, p + 1):
            out += find(i + j)

        return out

    print(find(0))


def p2b():
    """
    correct but too slow, basically a queue/stack-based bruteforce
    """

    # Same as above for p2a
    numbers = sorted([int(x) for x in lines])
    numbers = [0] + numbers

    partials = [sum(n + x in set(numbers) for x in range(1, 3 + 1)) for n in numbers]

    # NOTE: this could be deque() with popleft() below for a proper queue
    # In this case poping from the top seems to be good enough, so regular list
    # is enough. :)
    Q = []
    Q.append(0)
    found = 0
    while Q:
        i = Q.pop()
        p = partials[i]

        if p == 0:
            found += 1
            continue

        while p > 0:
            Q.append(i + p)
            p -= 1

    print("ANS", found)


print("Part1")
p1()
print("Part2")
p2a()
print("---- EOD ----")
