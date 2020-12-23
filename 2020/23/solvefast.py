"""
Added a faster solution for part2.
On my computer it runs in 0.5s on pypy and <5s on cpython 3.8.3
"""

from array import array


def p2b():
    arr = array("i", [0 for _ in range(1_000_000 + 1)])

    # This is my input, adjust here if you want to run it on yours. :)
    numbers = (6, 5, 3, 4, 2, 7, 9, 1, 8)
    for curr, _next in zip(numbers, numbers[1:]):
        arr[curr] = _next

    arr[numbers[-1]] = 10

    for r in range(10, 1_000_000 + 1):
        arr[r] = r + 1

    arr[1_000_000] = numbers[0]

    current = numbers[0]

    for i in range(10_000_000):
        pick = current - 1 or 1_000_000
        n1 = arr[current]
        n2 = arr[n1]
        n3 = arr[n2]

        while pick in [n1, n2, n3]:
            pick -= 1

        oldpick = arr[pick]
        arr[pick] = n1

        arr[current] = arr[n3]
        current = arr[n3]

        arr[n3] = oldpick

    ff = arr[1]
    print(ff * arr[ff])


p2b()
