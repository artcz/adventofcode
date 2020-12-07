from collections import defaultdict, deque

lines = open("input").read().strip().splitlines()

print("--- Day07 ---")


def p1():
    colors = defaultdict(set)

    for line in lines:
        bag, content = line.split("contain")
        if "," in content:
            content = [c.strip() for c in content.split(",")]
        else:
            content = [content.strip()]

        # Removes the word 'bag/bags'
        bag = " ".join(bag.split()[:-1])
        content = [" ".join(c.split()[:-1]) for c in content]

        # colors[node] = {parent1, parent2}
        for cc in content:
            bag = " ".join([b for b in bag.split() if not b.isdigit()])
            cc = " ".join([c for c in cc.split() if not c.isdigit()])
            colors[cc].add(bag)

    SEEN = {}
    Q = deque()

    for item in colors["shiny gold"]:
        Q.append(item)

    while Q:
        item = Q.popleft()
        SEEN[item] = True
        for i in colors[item]:
            Q.append(i)

    print(len(SEEN))


def p2():
    BAGS = defaultdict(list)

    for line in lines:
        bag, content = line.split("contain")
        bag = bag.strip()

        if "," in content:
            content = [c.strip() for c in content.split(",")]
        else:
            content = [content.strip()]

        # Removes the word 'bag/bags'
        bag = " ".join(bag.split()[:-1])
        content = [" ".join(c.split()[:-1]) for c in content]

        # BAGS[node] = [children1, children2]
        BAGS[bag].extend(content)

    SEEN = defaultdict(int)
    Q = deque()

    for item in BAGS["shiny gold"]:
        num, rest = item.split(maxsplit=1)
        Q.append((int(num), rest))

    while Q:
        prev, item = Q.popleft()
        SEEN[item] += prev
        for it in BAGS[item]:
            if "no other" in it:
                continue

            num, rest = it.split(maxsplit=1)
            Q.append((prev * int(num), rest))

    print(sum(SEEN.values()))


print("Part1", end="=> ")
p1()
print("Part2", end="=> ")
p2()
print("---- EOD ----")
