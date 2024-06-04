def GenStuff(n,s,R):
    possibleCombos = []
    numbPosCombos = s^n

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

    possibleCombos2 = []

    for x in possibleCombos:
        thisSum = 0
        for y in x:
            thisSum = thisSum + y
        if(thisSum == s):
            possibleCombos2.append(x)

    # COMBO CHECKER
    possibleCombos3 = []
    for x in possibleCombos2:
        Throw = False
        for y in x:
            OneDupe = False
            for z in x:
                if(y == z and OneDupe == False):
                    OneDupe = True
                elif(y == z and OneDupe == True):
                    Throw = True
        if(Throw == False):
            possibleCombos3.append(x)
    print(possibleCombos3)

GenStuff(3,6,5)