with open("input.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

counter = 1

for x in range(len(lines)-4):
    if (int(lines[x]) + int(lines[x+1]) + int(lines[x+2]) < int(lines[x+1]) + int(lines[x+2]) + int(lines[x+3])):
        counter += 1
print(counter)
