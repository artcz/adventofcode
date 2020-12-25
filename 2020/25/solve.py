card_key, door_key = [int(x) for x in open("input").read().strip().splitlines()]
mod = 20201227


def gen(subject):
    curr = 1
    while True:
        curr *= subject
        curr %= mod
        yield curr


for i, x in enumerate(gen(7), 1):
    if x == card_key:
        card_loop = i
        break

for i, x in enumerate(gen(7), 1):
    if x == door_key:
        door_loop = i
        break


print(card_loop, door_loop)


for i, x in enumerate(gen(card_key), 1):
    if i == door_loop:
        break

print(i, x)
