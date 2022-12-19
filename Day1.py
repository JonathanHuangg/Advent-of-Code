file = open('Day1Input.txt', "r")
lines = file.readlines()
max = -1
currentCount = 0
count = 0
totals = []

#Part 1
for Line in lines:
    if len(Line.strip()) == 0:
        totals.append(int(currentCount))
        if currentCount > max:
            max = currentCount
            currentCount = 0
        currentCount = 0
    else:
        currentCount += int(Line.strip())

if currentCount > max:
    max = currentCount
    currentCount = 0

print("Part 1 Max: " + str(max))

totals.append(int(currentCount))
totals.sort()

print("Part 2 Max: " + str(totals[-1] + totals[-2] + totals[-3]))

#Topics Covered: Indexing, file reader





