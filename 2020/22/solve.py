from collections import deque

# Read the input
players = open("test").read().strip().split('\n\n')
players = open("input").read().strip().split('\n\n')

print("--- Day22 ---")


def part1():
    player1, player2 = [p.splitlines()[1:] for p in players]

    P1 = deque(int(x) for x in player1)
    P2 = deque(int(x) for x in player2)

    while P1 and P2:
        card1 = P1.popleft()
        card2 = P2.popleft()

        if card1 > card2:
            P1.append(card1)
            P1.append(card2)

        elif card2 > card1:
            P2.append(card2)
            P2.append(card1)

    winner = P1 or P2

    ans = 0
    for i, j in enumerate(list(winner)[::-1], 1):
        ans += (i * j)

    print(ans)


def part2():
    player1, player2 = [p.splitlines()[1:] for p in players]

    # Using lists for Part2 because the card decks are short enough, so that
    # there's no big performance gain on the puzzle's input, but the code is
    # nicer because we don't need to convert back and forth between list and
    # deque to do the slicing.
    P1 = [int(x) for x in player1]
    P2 = [int(x) for x in player2]

    def game(P1, P2):
        SEEN = set()

        while P1 and P2:
            if (tuple(P1), tuple(P2)) in SEEN:
                return True, P1

            SEEN.add((tuple(P1), tuple(P2)))

            card1 = P1.pop(0)
            card2 = P2.pop(0)

            if card1 <= len(P1) and card2 <= len(P2):
                p1wins, _ = game(P1[:card1], P2[:card2])
            else:
                p1wins = card1 > card2

            if p1wins:
                P1 += [card1, card2]
            else:
                P2 += [card2, card1]

        return (True, P1) if P1 else (False, P2)

    _, winner = game(P1, P2)

    ans = sum(i * j for i, j in enumerate(winner[::-1], 1))
    print(ans)


print("Part1\n")
part1()
print("\nPart2\n")
part2()
print("\n---- EOD ----")
