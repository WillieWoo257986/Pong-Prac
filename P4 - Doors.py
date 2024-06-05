doors = []

for i in range(64):
    doors.append(False)

for x in range(64):
    for y in range(64):
        if((y+1)%(x+1) == 0):
            if(doors[y] == False):
                doors[y] = True
            else:
                doors[y] = False

outputString = ""

for z in range(64):
    if(doors[z] == True):
        outputString = outputString + str(z+1) +  " "

print(outputString)