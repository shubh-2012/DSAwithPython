
import math

for _ in range(int(input())):
    size = int(input())
    inputList = list(map(int, input().split()))
    count_pair,count_pair1,count_pair2 = 0,0,0
    count_pos, count_neg = 0, 0
    for i in range(0,len(inputList)):
        if inputList[i]>0:
            count_pos += 1
        if inputList[i]<0:
            count_neg += 1
    if count_neg<2 and count_pos>1:
        count_pair1 = (math.factorial(count_pos)// (math.factorial(count_pos-2) * 2))
    if count_pos<2 and count_neg>1:
        count_pair2 = (math.factorial(count_neg)// (math.factorial(count_neg-2) * 2))
    if count_neg>1 and count_pos>1:
         count_pair1 = (math.factorial(count_pos)// (math.factorial(count_pos-2) * 2))
         count_pair2 = (math.factorial(count_neg)// (math.factorial(count_neg-2) * 2))

    count_pair = count_pair1 + count_pair2

    print(count_pair)
