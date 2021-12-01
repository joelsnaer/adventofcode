with open("input.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

counter = 1

for x in range(len(lines)-1):
    if (lines[x] < lines[x+1]):
        counter += 1
print(counter)
