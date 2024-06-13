inputString = '''34
a
ant
bee
bellow
boustrophedonically
cat
determinism
dinosaur
emu
facetiously
ghost
ghastliness
junk
junket
knotty
llama
mossy
neocolonialism
opossum
psst
queen
racoon
scarecrow
schoolboy
schoolgirl
schoolteacher
terminus
tummy
tumultuous
vaccination
wandering
xylophones
youthfulness
zeppelins'''
outputString = ""
inputConvert = inputString.split("\n")
numberWords = int(inputConvert[0])

letterData = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
vowelData = ["a","e","i","o","u"]

def findType(word, letterData, vowelData):
    wordSplit = list(word)
    isL = True
    isV = True

    letterNum = []
    vowelNum = []


    # test test
    for x in range(len(wordSplit)):
        for y in range(len(letterData)):
            if(wordSplit[x] == letterData[y]):
                letterNum.append(y)
        for z in range(len(vowelData)):
            if(wordSplit[x] == vowelData[z]):
                vowelNum.append(z)
    print(letterNum)
    print(vowelNum)

    # accending check

    for i in range(len(letterNum)-1):
        if(letterNum[i] > letterNum[i+1]):
            isL = False

    for i in range(len(vowelNum)-1):
        if(vowelNum[i] > vowelNum[i+1]):
            isV = False

    if(isL == True):
        return "L"
    elif(isV == True):
        return "V"
    else:
        return "N"

for a in range(numberWords):
    findType(inputConvert[a+1],letterData,vowelData)
    outputString = outputString + findType(inputConvert[a+1],letterData,vowelData) + " " + inputConvert[a+1] + "\n"

print(outputString)