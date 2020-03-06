import math

def factors(number):
    list = set()
    for i in range(1, int(math.sqrt(number))+1):
        if(number % i == 0):
            list.add(i)
            list.add(int(number/i))
    return list

trianguleNumber = 0
i = 0
while(True):
    i += 1
    trianguleNumber += i
    
    list = factors(trianguleNumber)
    
    if len(list) > 500:
        print(i)
        print(trianguleNumber)
        print(len(list))
        print(list)
        break
