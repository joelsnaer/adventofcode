with open("input.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
lines = lines[0].split(',')

fish = [0, 0, 0, 0, 0, 0, 0, 0, 0]
old = 0
zero = 0
for value in lines:
    fish[int(value)] += 1

for x in range(256):
    for count in range(len(fish)):
        if count == 0:
            zero = fish[count]
        else:
            fish[count - 1] = fish[count]
            if count == 8:
                fish[8] = zero
                fish[6] += zero

print(sum(fish))