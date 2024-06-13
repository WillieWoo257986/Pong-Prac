numactors = 5
finalString = ""

numberRows = 2 ** numactors

LOL = list()
for a in range(numberRows):
    LOL.append([])

for b in range(numberRows):
    for c in range(numactors):
        LOL[b].append([])

for x in range(numactors):
    unitlenth = 2 ** (x+1)
    unitleft = 2 ** (x)
    status = True
    for y in range(numberRows):
        if(status == False):
            LOL[y][x] = "X"
            unitleft = unitleft - 1
        else:
            LOL[y][x] = "-"
            unitleft = unitleft - 1
        if(unitleft == 0):
            unitleft = unitlenth
            if(status == False):
                status = True
            else:
                status = False

print(LOL)

# time to get words

