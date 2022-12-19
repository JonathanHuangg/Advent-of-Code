file = open("Day3Input.txt", "r")
lines = file.readlines()
totalPoints = 0
#takes in string a and string b
def findRepeat(a, b):
    for x in range(len(a)):
        for y in range(len(b)):
            if a[x] == b[y]:
                return a[x]
#takes in a letter
def givePrio(prio):
    asciiP = ord(prio)
    if (prio.isupper()):
        asciiP -= 38
    else:
        asciiP -= 96
    return asciiP

#Part 1
for Line in lines:
    Line = Line.strip()
    a = Line[0: int(len(Line)/2)]
    b = Line[int(len(Line)/2):]
    prio = findRepeat(a, b)

    totalPoints += givePrio(prio)

print("Part 1: " + str(totalPoints))
        
#Part 2
totalPoints = 0
count = 0

for x in range(0, len(lines), 3):
    line1 = lines[x].strip()
    line2 = lines[x + 1].strip()
    line3 = lines[x + 2].strip()

    set1 = set(line1)
    set2 = set(line2)
    set3 = set(line3)

    resultSet = set1.intersection(set2)
    resultSet = resultSet.intersection(set3)
    resultList = list(resultSet)
    totalPoints += givePrio(resultList[0])


print("Part 2: " + totalPoints)

#Topics Covered: searching in O(n^2), sets and lists

