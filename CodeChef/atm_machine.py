
for _ in range(int(input())):
    size, money = [int(x) for x in input().split()]
    inputList = list(map(int, input().split()))
    temp = ""
    for i in range(0,size):
        if money - inputList[i]>=0:
            temp+="1"
            money -= inputList[i]

        else:
           temp+="0"

    print(temp)