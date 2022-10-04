for _ in range(int(input())):
    x = int(input())
    inputList = list(map(int, input().split()))
    min_n = abs(inputList[0])
    max_n = abs(inputList[1])
    sumEven = 0
    sumOdd = 0

    for i in range(0,len(inputList)):
        if(i%2==0):
            sumEven+=abs(inputList[i])
            if abs(inputList[i])<min_n:
                min_n = abs(inputList[i])
        else:
            sumOdd+=abs(inputList[i])
            if abs(inputList[i])>max_n:
                max_n = abs(inputList[i])
    
    if (sumEven-sumOdd) < (sumEven-sumOdd+2*(max_n-min_n)):
        print(sumEven-sumOdd+2*(max_n-min_n))
        
    else:
        print(sumEven-sumOdd)
