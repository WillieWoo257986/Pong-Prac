input = '''20
racecar
racing car
Tumut
a
stressed was I ere I saw desserts
Straw? No, too stupid a fad; I put soot on warts
Was it a car or a cab I saw?
Ed, I saw Harpo Marx ram Oprah W. aside.
Yes, Mel Gibson is a casino's big lemon.
Mr Owl ate my metallic worm.
Go hang a salami, I'm a lasagna hog!
On a clover, if alive, erupts a vast, pure evil; a fire volcano.
Dennis, Nell, Edna, Leo, Noel and Ellen sinned.
A man, a plan, a cat, a ham, a yak, a yam, a bat, a canal--Panama!
Steven, I left an oily lion at feline vets.
Put Eliot's toilet up.
Marg, let's send a sadness telegram!
Yawn....Madonna fan? No damn way!!
Red rum, sir, is murder!
'Reviled did I live,' said I, 'as evil I did deliver.' '''
# remove puniation, capital letters

OG = input.split("\n")

input = input.replace("`","")
input = input.replace("!","")
input = input.replace("&","")
input = input.replace("*","")
input = input.replace(",","")
input = input.replace(".","")
input = input.replace("?","")
input = input.replace("/","")
input = input.replace("'","")
input = input.replace(";","")
input = input.replace(":","")
input = input.replace('"',"")
input = input.replace(" ","")

input = input.lower()

wordsAsList = input.split("\n")

print(wordsAsList)

backwardList = []

for x in range(len(wordsAsList)- 1):
    z = x + 1
    wordSplit = list(wordsAsList[z])
    backwards = []
    backwardsStr = ""
    for y in range(len(wordSplit)):
        backwards.append(wordSplit[-(y+1)])
    backwardsStr = ''.join(backwards)
    backwardList.append(backwardsStr)

print(backwardList)

outputString = ""

for a in range(len(wordsAsList) - 1):
    if(wordsAsList[a+1] == backwardList[a]):
        outputString = outputString + 'Yes "' + OG[a+1] + '"\n'
    else:
        outputString = outputString + 'No "' + OG[a+1] + '"\n'

print(outputString) 