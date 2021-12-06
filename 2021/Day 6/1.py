with open("input.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
lines = lines[0].split(',')


for x in range(80):
    for count, value in enumerate(lines):
        if value == 0:
            lines[count] = 6
            lines.append(9)
        else:
            lines[count] = int(value) - 1

print(len(lines))
