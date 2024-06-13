a = 1
b = 1
c = 31
d = 1

repeat = 0
string = 0
cycle = 0

dictionay = {}
dictionay[d] = d

current_val = d

def nextValue(dictionay,current_val,a,b,c):
    next_val = (a * current_val*current_val + b) % c
    if next_val in dictionay:
        return [next_val, True]
    else:
        dictionay[next_val] = next_val
        return [next_val, False]
    
def findStringCycle(a,b,c,d,repeat):
    current_val = d
    counter = 0
    string = 0
    cycle = 0

    repeatOnce = False

    for y in range(100):
        current_val = (a * current_val*current_val + b) % c
        counter = counter + 1
        if(current_val == repeat and repeatOnce == False):
            string = counter
            repeatOnce = True
        elif(current_val == repeat and repeatOnce == True):
            cycle = counter - string
            return [string, cycle]
            

def main(a,b,c,d,dictionay,current_val):
    for x in range(100):
        back = nextValue(dictionay,current_val,a,b,c)
        current_val = back[0]
        if(back[1] == True):
            repeat = current_val
            data = findStringCycle(a,b,c,d,repeat)
            string = data[0]
            cycle =  data[1]
            return [repeat, string, cycle]

data = main(a,b,c,d,dictionay,current_val)
print("repeat = " + str(data[0]) + ", string = " + str(data[1]) + ", cycle = " + str(data[2]))
