def InitGen(n,s):
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

# gen all combos of n
# Check totals
# check ratio

# gen combos of multipes
# check duplicates
# check asending

print(InitGen(3,6))