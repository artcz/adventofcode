inp = open("input").read().strip().splitlines()


inp = [int(x) for x in inp]


def p1():
    for i in inp:
        for j in inp:
            if i != j and i + j == 2020:
                print(i * j)
                return


p1()


def p2():
    for i in inp:
        for j in inp:
            for k in inp:
                if i != j != k and i + j + k == 2020:
                    print(i * j * k)
                    return


p2()
