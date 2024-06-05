n = 3 # Number of tasks
s = 6 # Sum of points
R = 10 # Ratio of highest to lowest scoring point

def initGen(n,s):
    possibleCombos = []

    for a in range(s):
        if(n >= 2):
            for b in range(s):
                if(n >= 3):
                    for c in range(s):
                        if(n >= 4):
                            for d in range(s):
                                if(n >= 5):
                                    for e in range(s):
                                        if(n >= 6):
                                            for f in range(s):
                                                possibleCombos.append([a+1,b+1,c+1,d+1,e+1,f+1])
                                        else:
                                            possibleCombos.append([a+1,b+1,c+1,d+1,e+1])
                                else:
                                    possibleCombos.append([a+1,b+1,c+1,d+1])
                        else:
                            possibleCombos.append([a+1,b+1,c+1])
                else:
                    possibleCombos.append([a+1,b+1])
        else:
            possibleCombos.append([a+1])
    return(possibleCombos)

def checkTotals(n, s, input):
    outputList = []
    for x in range(len(input)):
        currentTotal = 0
        for y in range(n):
            currentTotal = currentTotal + input[x][y]
        if(currentTotal == s):
            outputList.append(input[x])

    return outputList


# gen all combos of n
# Check totals
# check asending
# check ratio

# gen combos of multipes
# check duplicates

print(checkTotals(n,s,initGen(n,s)))