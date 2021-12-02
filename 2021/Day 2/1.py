with open("input.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

horizontal = 0
depth = 0

for x in lines:
    t = x.split(' ')
    if t[0] == 'forward':
        horizontal += int(t[1])
    elif t[0] == 'up':
        depth -= int(t[1])
    elif t[0] == 'down':
        depth += int(t[1])

print(horizontal * depth)
