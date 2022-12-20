file = open("Day4Input.txt", "r")
lines = file.readlines()

#Part 1
count = 0
count2 = 0
for Line in lines:
    Line = Line.strip()
    start = Line.split(",")
    q1 = start[0][0:start[0].index("-")]
    q2 = start[0][start[0].index("-") + 1:]
    q3 = start[1][0:start[1].index("-")]
    q4 = start[1][start[1].index("-") + 1:]

    q1 = int(q1)
    q2 = int(q2)
    q3 = int(q3)
    q4 = int(q4)


    if (q1 <= q3 and q2 >= q4): 
        count += 1
    elif (q1 >= q3 and q2 <= q4):
        count += 1
    
    if (q3 >= q1 and q3 <= q2):
        count2 += 1
    elif (q1 >= q3 and q1 <= q4):
        count2 += 1

print(count)
print(count2)

    

    




