with open("input.txt") as f:
    games = f.read().splitlines()

result = 0
for i, x in enumerate(games):
    hands = x.split(": ")[1].split("; ")
    for hand in hands:
        m = {"red": 0, "green": 0, "blue": 0}
        for game in hand.split(", "):
            a, b = game.split()
            m[b] = int(a)
        if m["red"] > 12 or m["green"] > 13 or m["blue"] > 14:
            break
    else:
        result += i + 1

print("Part 1", result)

result = 0
for x in games:
    power = 1
    hands = x.split(": ")[1].split("; ")
    min_set = {"red": 0, "green": 0, "blue": 0}
    for hand in hands:
        m = {"red": 0, "green": 0, "blue": 0}
        for game in hand.split(", "):
            a, b = game.split()
            m[b] = int(a)
        for k, v in min_set.items():
            min_set[k] = max(min_set[k], m[k])
    for value in min_set.values():
        power *= value
    result += power

print("Part 2", result)