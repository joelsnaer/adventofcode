with open("input.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    

gen = 0
scrub = 0
counter1 = 0
counter0 = 0



for num in range(12):
    for line in lines:
        if line[num] == '0':
            counter0 += 1
        else:
            counter1 += 1
    if counter0 > counter1:
        newlist = [x for x in lines if x[num] != '0']
    else:
        newlist = [x for x in lines if x[num] != '1']
    counter1 = 0
    counter0 = 0
    lines = newlist
    if (len(newlist) == 1):
        gen = newlist[0]
        break


# Uses same array so comment out the piece of code u don't want to use
for num in range(12):
    for line in lines:
        if line[num] == '0':
            counter0 += 1
        else:
            counter1 += 1
    if counter0 > counter1:
        newlist = [x for x in lines if x[num] != '1']
    else:
        newlist = [x for x in lines if x[num] != '0']
    counter1 = 0
    counter0 = 0
    lines = newlist
    if (len(newlist) == 1):
        scrub = newlist[0]
        break


print(gen)
print(scrub)
