for _ in range(int(input())):
    size = int(input())
    inputList = list(map(int, input().split()))
    count_pos, count_neg = 0,0

    for i in range(0,len((inputList))):
        if inputList[i] == 1:
            count_pos+=1
        else:
            count_neg+=1

    if len(inputList)%2 == 0:
        if count_neg == count_pos:
            print("Yes")
        elif (abs(count_pos - count_neg)) == 2:
            if count_neg % 2 == 0:
                print("Yes")
            else:
                print("No")
        else:
            print("No")
    else:
        if abs(count_pos - count_neg) == 1:
            print("Yes")
        else:
            print("No")
