def splitMultiDates(input):
    dateArray = input.split("\n")
    return dateArray

def splitInput(input):
    inputList = list(str(input))
    day = inputList[0] + inputList[1]
    month = inputList[3] + inputList[4]
    year = inputList[6] + inputList[7] + inputList[8] + inputList[9]
    return([day,month,year])

def addDigit(inputNum, isYear):
    if(isYear != True):
        # 11 check
        if(inputNum % 11 == 0):
            return inputNum
    
    inputList = list(str(inputNum))
    runningTotal = 0
    for x in range(len(inputList)):
        runningTotal = runningTotal + int(inputList[x])
    
    return runningTotal

inputedText = "04/02/2000\n20/03/1997\n16/10/2001\n29/07/1965\n11/01/1974\n18/05/1970\n29/11/1901\n15/11/1976\n08/08/2002"
dateArray = splitMultiDates(inputedText)
print(dateArray)

for a in range(len(dateArray)):
    inputedText = dateArray[a]
    converted = splitInput(inputedText)
    day = int(converted[0])
    month = int(converted[1])
    year = int(converted[2])

    totals = addDigit(addDigit(day, False), False) + addDigit(addDigit(month, False), False) + addDigit(addDigit(year, True), False)
    final = addDigit(addDigit(totals, False), False)
    print(str(final) + " " + inputedText)