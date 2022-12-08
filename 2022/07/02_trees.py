from dataclasses import dataclass, field
from typing import Optional

input_files = [
    "test",
    "input",
]


@dataclass
class Node:
    name: str
    size: int = 0
    parent: Optional["Node"] = None
    children: list["Node"] = field(default_factory=list)
    is_file: bool = False

    def __str__(self):
        parent = self.parent.name if self.parent else "None"
        return f"{parent} >> {self.name}"

    def add(self, x):
        self.children.append(x)

    def update_dir_sizes(self):
        if not self.children:
            return

        for c in self.children:
            c.update_dir_sizes()

        self.size = sum(c.size for c in self.children)


def main(inp):
    root = Node("/", 0)
    node = root

    lines = inp.splitlines()
    for _, line in enumerate(lines):
        x = line.split()
        assert node

        if len(x) == 3:
            assert line.startswith("$ cd")

            if x[2] == "..":
                node = node.parent
            else:
                for c in node.children:
                    if c.name == x[2]:
                        node = c
                        break

        elif len(x) == 2:
            if x[1] == "ls":
                continue

            elif x[0].isdigit():
                size, fname = x[0], x[1]
                node.add(
                    Node(
                        name=fname,
                        is_file=True,
                        parent=node,
                        size=int(size),
                    )
                )

            elif x[0] == "dir":
                node.add(
                    Node(
                        name=x[1],
                        is_file=False,
                        parent=node,
                    )
                )

    root.update_dir_sizes()

    def p1(node):
        if node.is_file:
            return 0

        # NOTE: This is not a base case
        # if (not node.is_file) and node.size <= 100_000:
        #     return node.size

        ans = node.size if node.size <= 100_000 else 0
        for ch in node.children:
            ans += p1(ch)

        return ans

    ans = p1(root)
    print("Part1", ans)

    total = 70000000
    available = total - root.size
    target = 30000000 - available

    ans = [1e9]

    def p2(node):
        if not node.is_file and node.size > target:
            ans[0] = min(ans[0], node.size)

        for ch in node.children:
            p2(ch)

    p2(root)
    print("Part2", ans[0])


if __name__ == "__main__":
    for file in input_files:
        print("\n" + file)
        with open(file) as fd:
            inp = fd.read().strip()

        main(inp)
