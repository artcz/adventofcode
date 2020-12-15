import itertools
from collections import deque

lines = open("input").read().strip().splitlines()


print("--- Day09 ---")


def p1():
    SIZE = 25
    numbers = [int(x) for x in lines]
    lastN = deque(numbers[:SIZE], maxlen=SIZE)
    for current in numbers[SIZE:]:
        for c in itertools.combinations(lastN, 2):
            if sum(c) == current:
                break
        else:
            print(current)
            return current

        lastN.append(current)


def p2():
    target = p1()
    numbers = [int(x) for x in lines]
    temp = deque([])
    for current in numbers:

        if sum(temp) == target:
            print(min(temp) + max(temp))
            return

        if sum(temp) < target:
            temp.append(current)

        if sum(temp) > target:
            while sum(temp) > target:
                temp.popleft()


print("Part1")
p1()
print("Part2")
p2()
print("---- EOD ----")
