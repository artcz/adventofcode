from collections import deque

print("--- Day23 ---")

FILENAME = "test"
FILENAME = "input"


def p1():
    """
    Part 1 solved using, what I thought would be a smart solution with
    deque.rotate, unfortunately it required major updates for part2, but
    leaving here as is for reference
    """
    numbers = [int(x) for x in open(FILENAME).read().strip()]
    numbers = deque(numbers)

    for i in range(100):
        pick = numbers[0] - 1

        # Rotate right to, to move the first item and put it at the end, thus
        # the first three elements after this operation should be the ones we
        # need to pick.
        numbers.rotate(-1)

        temp = []
        for _ in range(3):
            temp.append(numbers.popleft())

        if pick < min(numbers):
            pick = max(numbers)

        while pick in temp:
            if pick < min(numbers):
                pick = max(numbers)
                break

            pick -= 1

        destination = numbers.index(pick)

        # Rotate to the position where we should be inserting the numbers
        numbers.rotate(-destination - 1)

        for _ in range(3):
            numbers.appendleft(temp.pop())

        # Rotate back to the correct position
        numbers.rotate(destination + 1)

    numbers.rotate(-numbers.index(1))
    print("".join(str(x) for x in numbers))


def p2():
    """
    Part2 required a reimplementation from scratch, because the cleverness of
    part1 made it mostly O(n) in few places. :)

    * O(n) for index()
    * O(n) for min/max

    Using linkedlist (implemented as a simple dict) instead, using the fact
    that the numbers are continuuous to replace min/max with a non-O(n)
    alternative.
    """
    numbers = [int(x) for x in open(FILENAME).read().strip()]
    LL = {}

    for r in range(max(numbers) + 1, 1_000_000 + 1):
        numbers.append(r)

    for curr, _next in zip(numbers, numbers[1:]):
        LL[curr] = _next

    # Wrap it back to the first number
    LL[numbers[-1]] = numbers[0]

    # this minn/maxx is only needed if we wanted to test with a different range
    # than in the puzzle description. otherwise the minn is always going to be
    # 1 and maxx should be 1_000_000
    minn = min(numbers)
    maxx = max(numbers)

    current = numbers[0]

    for i in range(10_000_000):
        pick = current - 1
        n1 = LL[current]
        n2 = LL[n1]
        n3 = LL[n2]
        n4 = LL[n3]

        while pick in {n1, n2, n3}:
            pick -= 1

        # To avoid O(n) min max, we can use the fact that the numbers are
        # always the same, the only difference in max/min might be if we
        # picked up those numbers.
        # Also we can use the fact the numbers are [1..n] without any blanks
        # (except for the picked up numbers)
        if pick < minn:
            pick = maxx
            while pick in {n1, n2, n3}:
                pick -= 1

        # save what pick used to point at, and point it to n1 instead
        oldpick = LL[pick]
        LL[pick] = n1

        # make current point at whatever n3 was pointing at
        LL[current] = LL[n3]

        # n3 now points at whatever the pick was pointing at before
        LL[n3] = oldpick

        # new current is whatever the n3 was pointing at.
        current = n4

    ff = LL[1]
    print(ff * LL[ff])


def print_list(LL, start):
    """Used for debugging, left here for reference"""
    LL = dict(LL)
    cur = start
    while LL:
        cur = LL.pop(cur)
        print(cur, end="")

    print()


print("Part1\n")
p1()
print("\nPart2\n")
p2()
print("\n---- EOD ----")
