# cook your dish here

import math
for _ in range(int(input())):
    size, money = [int(x) for x in input().split()]
    inputList = list(map(int, input().split()))
    count = 0
    #cost = 0
    inputList.sort()
    i = 0
    while(inputList[i] <= money and i < size-1):
        #cost = cost + inputList[i]
        money -= inputList[i]
        i += 1
        count += 1

    if i < size:
        inputList[i] = math.ceil(inputList[i]/2)
        if inputList[i] <= money:
            count += 1

    print(count)



