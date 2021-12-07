with open("input.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
lines = lines[0].split(',')

currentSum = 0
minSum = 9223372036854775807
minNumber = 0

for x in range(int(max(lines))):
    for line in lines:
        currentSum += abs(int(line) - x) * (abs(int(line) - x) + 1) // 2
    if currentSum < minSum:
        minSum = currentSum
        minNumber = x

    currentSum = 0

print(minSum)
print(minNumber)