#Rock(1) Paper(2) Scissor(3)
#A          B         C
#X          Y         Z
#Lost(0)   Draw(3)    Win(6)

def compareRest(char):
    if char == "X":
        return 1
    elif char == "Y":
        return 2
    elif char == "Z":
        return 3

file = open("Day2Input.txt", "r")
lines = file.readlines()
totalPoints = 0
asciiGap = ord("X") - ord("A") 

for Line in lines:
    Line = Line.strip()
    theirMove = ord(Line[0]) 
    yourMove = ord(Line[2])
    difference = yourMove - (theirMove + asciiGap)
    if (difference < 0):
        difference += 3
    if difference == 0:
        totalPoints += (3 + compareRest(Line[2]))
    elif difference == 1:
        totalPoints += (6 + compareRest(Line[2]))
    else:
        totalPoints += (compareRest(Line[2]))
print("Part 1: " + str(totalPoints))

#Part 2
#Lose     Draw       Win
# X        Y          Z
totalPoints = 0
theirMove = {
    "A": 0,
    "B": 1,
    "C": 2
}
yourMove = {
    "X": -1,
    "Y": 0,
    "Z": 1
}
winnings = [1, 2, 3]

for Line in lines:
    Line = Line.strip()
    if Line[2] == "X":
        totalPoints += winnings[theirMove[Line[0]] + yourMove["X"]]
    elif Line[2] == "Y":
        totalPoints += (winnings[theirMove[Line[0]] + yourMove["Y"]] + 3)
    else:
        index = theirMove[Line[0]] + yourMove["Z"]
        if (index == 3):
            index = 0
        totalPoints += (winnings[index] + 6)
print(totalPoints)

#Ideas Covered: Ascii numbers with logic, dictionaries

    
        
