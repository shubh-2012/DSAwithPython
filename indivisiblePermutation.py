for _ in range(int(input())):
    size = int(input())

    for i in range(1,size+1):
        if i == 1:
            print(2,end=" ")
        elif i == size:
            print(1,end=" ")
        else:
            print(i+1,end=" ")
