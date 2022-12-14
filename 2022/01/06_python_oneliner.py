
(lambda z: print([sum(z[-1:]), sum(z[-3:])]))(sorted([sum(int(n) for n in x.splitlines()) for x in open(0).read().strip().split("\n\n")]))
