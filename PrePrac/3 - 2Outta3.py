def functionA(k):
    ongoing = 1
    for x in range(k):
        num = x + 2
        ongoing = ongoing * (((num)*(num)*(num)-1)/((num)*(num)*(num)+1))
    return(ongoing)

def functionB():
    for y in range(10000):
        print(functionA(y+1))
        if functionA(y+1) <= 0.6666667:
            print(y)
            print(y+1)
            print(functionA(y))
            return
        
functionB()