with open("input.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

gamma = 0
epsilon = 0
gammaresult = ''
epsilonresult = ''
counter1 = 0
counter0 = 0

for x in range(12):
    for line in lines:
        if line[x] == '0':
            counter0 += 1
        else:
            counter1 += 1
    if counter0 > counter1:
        gammaresult += '0'
        epsilonresult += '1'
    else:
        gammaresult += '1'
        epsilonresult += '0'
    counter1 = 0
    counter0 = 0

print(gammaresult)
print(epsilonresult)