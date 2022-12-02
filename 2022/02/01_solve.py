"""
I originally solved it by doing lots of ifs, just like below.
Instead of compressing it to a modulo solution, I just added some fancy objects
to make the ifs more readable.
"""
import sys
from dataclasses import dataclass


@dataclass
class Piece:
    chars: str
    score: int

    def __eq__(self, oth):
        return self.score == oth

    def __contains__(self, oth):
        return oth in self.chars

    def __add__(self, oth):
        return oth + self.score


@dataclass
class State:
    char: str
    score: int

    def __contains__(self, oth):
        return oth in self.char

    def __add__(self, oth):
        return oth + self.score


def main(inp):
    lines = inp.splitlines()

    rock = Piece("AX", 1)
    paper = Piece("BY", 2)
    sci = Piece("CZ", 3)

    lost = State("X", 0)
    draw = State("Y", 3)
    wins = State("Z", 6)  # wins instead of win for nicer alignement :)

    ans = 0
    for line in lines:
        a, b = line.split()
        if a in rock:
            if b in rock: ans += rock + draw
            if b in paper: ans += paper + wins
            if b in sci: ans += sci + lost

        elif a in paper:
            if b in rock: ans += rock + lost
            if b in paper: ans += paper + draw
            if b in sci: ans += sci + wins

        elif a in sci:
            if b in rock: ans += rock + wins
            if b in paper: ans += paper + lost
            if b in sci: ans += sci + draw

    print("Part1", ans)

    ans = 0
    for line in lines:
        a, b = line.split()
        if a in rock:
            if b in lost: ans += lost + sci
            if b in draw: ans += draw + rock
            if b in wins: ans += wins + paper

        elif a in paper:
            if b in lost: ans += lost + rock
            if b in draw: ans += draw + paper
            if b in wins: ans += wins + sci

        elif a in sci:
            if b in lost: ans += lost + paper
            if b in draw: ans += draw + sci
            if b in wins: ans += wins + rock

    print("Part2", ans)


if __name__ == "__main__":
    file = sys.argv[1]
    with open(file) as fd:
        inp = fd.read().strip()
        main(inp)
