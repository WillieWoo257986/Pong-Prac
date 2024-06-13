height = 7
width = 4.5

toplength = float((width * 4) + 1)

finalstring = ""

for a in range(int(toplength)):
    finalstring = finalstring + "_"

def Row(width, x):
    lengthremaining = width
    rowstring = "|"
    if(x % 2 != 0):
        rowstring = rowstring + "_|"
        lengthremaining = lengthremaining - 0.5
    for y in range(int(lengthremaining) + 1):
        if(lengthremaining > 0.5 and lengthremaining != 0):
            rowstring = rowstring + "___|"
            lengthremaining = lengthremaining - 1
        elif(lengthremaining != 0):
            rowstring = rowstring + "_|"
            lengthremaining = lengthremaining - 0.5
    return rowstring

for x in range(height):
    finalstring = finalstring + "\n" + Row(width, x)
    
print(finalstring)